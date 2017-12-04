xquery version "1.0-ml";

let $loc := 277678
let $nums := for $n in (1 to xs:integer(fn:ceiling(math:sqrt($loc)))) return $n
let $max-corner :=  (($nums)[. eq 1 or . mod 2 eq 1] ! .)[fn:last()]
let $max-corner-pow := math:pow($max-corner, 2)
let $center-half := fn:floor($max-corner div 2) + 1
let $diff := $max-corner-pow - $loc
let $dist-from-max-corner := $max-corner - 1
return 
(
"Max corner:" || $max-corner || '- Its square: ' || $max-corner-pow || ' - Diff to Location: ' || $diff
,
"Distance from block " || $loc || " to 1st block is " || $dist-from-max-corner - $diff
)
