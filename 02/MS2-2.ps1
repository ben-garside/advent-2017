$s = Get-Content .\day2-1.txt
$checkSum = 0

function Sort-Array ($line) {
    $array = $line -split "\s+"
    $sorted = @()
    for ($i=0; $i -lt $array.Length; $i++)
    {
        $sorted += [convert]::ToInt32($array[$i], 10)       
    }
    return ($sorted | Sort-Object)    
}

function Divide-Even ($array) {
    
    $sheetSum = 0
    for ($c=0; $c -lt $array.Length; $c++)
    {
        $divisor = $array[$c]    
        for ($d = ($c + 1); $d -lt $array.Length; $d++)
        {
            $dividend = $array[$d]
            if( $dividend % $divisor -eq 0)
            {
                Write-Host "Dividend = " $dividend
                Write-Host "Divisor = " $divisor
                $answer = $dividend / $divisor
                $sheetSum = $sheetSum + $answer
                Write-Host $answer
            }
        }
    }
    return $sheetSum
    
}
    

foreach($entry in $s)
{
    # Write each line to console
    # Write-Host $entry
    $sortedEntry = Sort-Array($entry)
    Write-Host "Sorted Array: " $sortedEntry
    $checkSum += Divide-Even($sortedEntry)
    # Calculate the difference between min and max value on a row and write to console.
}
Write-Host "Check Sum = " $checkSum
