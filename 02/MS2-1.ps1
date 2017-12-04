$s = Get-Content .\day2-1.txt
$sum = 0

function Split-Lines ($line) {
    $array = $line -split "\s+"
    $min = [convert]::ToInt32($array[0], 10)
    $max = [convert]::ToInt32($array[0], 10)
    for ($i=1; $i -lt $array.Length; $i++)
    {
        $num = [convert]::ToInt32($array[$i], 10)
        if( $num -gt $max)
        {
            $max = $num
        }
        if( $num -lt $min)
        {
            $min = $num
        }
    }
    return ($max - $min)
}

foreach($entry in $s)
{
    # Write each line to console
    Write-Host $entry
    # Calculate the difference between min and max value on a row and write to console.
    $diff = Split-Lines($entry)    
    Write-Host "Diff = " $diff
    # Calculate the checksum by adding min and max values on a row.
    $sum = $sum + $diff
}
Write-Host "Checksum = " $sum
