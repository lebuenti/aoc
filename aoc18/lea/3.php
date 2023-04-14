<?php

function multi_array_key_exists($array, $keyRow, $keyColumn) {
    if (!array_key_exists($keyRow, $array)) {
        return false;
    }
    return array_key_exists($keyColumn, $array[$keyRow]);
}

function beauty_multi_array_printer($array) {
    echo PHP_EOL;
    foreach($array as $line) {
        // print("[ ");
        echo "[ ";
        foreach ($line as $cell) {
            echo $cell, ", ";
        }
        echo " ]", PHP_EOL;
    }
    echo PHP_EOL;
}

$area = [];
$overlaps_ids = [];

foreach (file('./inputs/3_example.txt') as $line) {
    $exploded = explode('@ ', $line);
    $exploded2 = explode(': ', $exploded[1]);

    $id = substr($exploded[0], 1);

    $point = [
        "x" => explode(",", $exploded2[0])[0],
        "y" => explode(",", $exploded2[0])[1]
    ];

    $size = [
        "w" => explode("x", $exploded2[1])[0],
        "h" => explode("x", $exploded2[1])[1]
    ];

    for ($i = $point["x"]; $i <= $point["x"] + $size["w"]; $i++) {

        for ($j = $point["y"]; $j <= $point["y"] + $size["h"]; $j++) {

            if (multi_array_key_exists($area, $i, $j)) {
                array_push($overlaps_ids, $id);

                if (array_search($area[$i][$j], $overlaps_ids) === false) {
                    array_push($overlaps_ids, $area[$i][$j]);
                }


            } else {
                $area[$i][$j] = $id;
            }

        }
    }

    

    // array_key_exists()

    // echo $id, " --", $point["x"], " --", $point["y"], " --", $size["w"], " --", $size["h"];



}
print("area");
// print_r($area);
beauty_multi_array_printer($area);
print("overlaps_ids");
    print_r($overlaps_ids);
    // beauty_multi_array_printer()

?>