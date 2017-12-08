xquery version "1.0-ml";
import module namespace functx = "http://www.functx.com" at "/MarkLogic/functx/functx-1.0-nodoc-2007-01.xqy";

declare variable $MB-SEQ := (:(0, 2, 7, 0):)(0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11);
declare variable $MB-SIZE := fn:count($MB-SEQ);
declare variable $MB-MAP := map:new();
declare variable $STEPS := 0;
declare variable $MEM-BLOCKS-PATTERNS := ();

declare function local:print-map()
{
  fn:string-join(
    for $key at $pos in functx:sort(map:keys($MB-MAP))
    let $item := map:get($MB-MAP, xs:string($key))
    return xs:string($item)
  , " ")
};

declare function local:map-to-seq()
{
  let $keys := functx:sort(map:keys($MB-MAP))
  return 
  (
    xdmp:set($MB-SEQ, $keys ! map:get($MB-MAP, .))
  )
};

declare function local:seq-to-map()
{
  let $map := map:map()
  let $_ := (
    for $item at $pos in $MB-SEQ
    return map:put($map, xs:string($pos), $item)
    )
  return (
    xdmp:set($MB-MAP, $map)
  )
};

declare function local:update-map($loc)
{
  let $loc-s := xs:string($loc)
  let $loc-v := map:get($MB-MAP, $loc-s)
  return
  (
    map:put($MB-MAP, $loc-s, $loc-v + 1)
  )
};

declare function local:hash-map()
{
  xdmp:md5(local:print-map())
};

declare function local:move-mem-blocks()
{
  local:map-to-seq()
  ,
  let $max-value := fn:max($MB-SEQ)
  let $max-value-loc := fn:index-of($MB-SEQ, $max-value)[1]
  let $start-fill-loc := $max-value-loc + 1 (:if ($max-value-loc + 1 le $MB-SIZE) then ( $max-value-loc + 1 ) else ( 1 ):)
  let $_ := map:put($MB-MAP, xs:string($max-value-loc), 0)
  let $run-further := fn:true()
  let $run := 
    for $index in 1 to $max-value
    return
     if ($run-further and fn:count($MEM-BLOCKS-PATTERNS) eq fn:count(fn:distinct-values($MEM-BLOCKS-PATTERNS)))
     then (
      if ($start-fill-loc eq 1 or $start-fill-loc lt $MB-SIZE)
      then (
        local:update-map($start-fill-loc)
        ,
        xdmp:set($start-fill-loc, ($start-fill-loc + 1))
        ,
        xdmp:set($MEM-BLOCKS-PATTERNS, ($MEM-BLOCKS-PATTERNS, local:hash-map()))
        
      )
      else if ($start-fill-loc eq $MB-SIZE)
      then (
        local:update-map($start-fill-loc)
        ,
        xdmp:set($start-fill-loc, 1)
        ,
        xdmp:set($MEM-BLOCKS-PATTERNS, ($MEM-BLOCKS-PATTERNS, local:hash-map()))
        
      )
      else if ($start-fill-loc gt $MB-SIZE) 
      then (
        xdmp:set($start-fill-loc, 1)
        ,
        local:update-map($start-fill-loc)
        ,
        xdmp:set($start-fill-loc, 2)
        ,
        xdmp:set($MEM-BLOCKS-PATTERNS, ($MEM-BLOCKS-PATTERNS, local:hash-map()))
        
      )
      else ()
      ) else ( xdmp:set($run-further, fn:false()))
   (:let $hash := local:hash-map():)
   return 
   (
     (:"Max: "||$max-value||"; Max-loc: "||$max-value-loc||", Hashes: "||fn:string-join($MEM-BLOCKS-PATTERNS, ","),
     "Current hash: "||$hash,$run,:)
     
     if ($run-further (:fn:count($MEM-BLOCKS-PATTERNS) eq fn:count(fn:distinct-values($MEM-BLOCKS-PATTERNS)):))
     then (
       xdmp:set($STEPS, $STEPS + 1)
       ,
       (:,
       $STEPS || " Step Completed"
       ,:)
       local:move-mem-blocks()
       
     )
     else ( 
       "DONE" )
   )
};


local:seq-to-map()
,
local:move-mem-blocks()
(:,
local:print-map():)
,
"Memory blocks distributed in " || $STEPS || " steps" 
