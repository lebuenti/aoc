<?php

function multi_array_key_exists($array, $keyRow, $keyColumn) {
    if (!array_key_exists($keyRow, $array)) {
        return false;
    }
    return array_key_exists($keyColumn, $array[$keyRow]);
}

function beauty_coordinates_printer($array) {
    echo PHP_EOL;
    foreach ($array as $line) {
        echo '[ ';

        reset($line);
        $firstKey = key($line);
        for ($i = 0; $i < $firstKey; $i++) {
            echo '., ';
        }

        foreach ($line as $cell) {
            echo $cell, ', ';
        }
        echo ' ]', PHP_EOL;
    }
    echo PHP_EOL;
}

function part1() {
    $area = [];

    foreach (file('./inputs/3.txt') as $line) {
        $exploded = explode('@ ', $line);
        $exploded2 = explode(': ', $exploded[1]);

        $id = substr($exploded[0], 1, 1);

        $point = [
            'x' => explode(',', $exploded2[0])[0],
            'y' => explode(',', $exploded2[0])[1],
        ];
        $size = [
            'w' => explode('x', $exploded2[1])[0],
            'h' => explode('x', $exploded2[1])[1],
        ];

        for ($x = $point['x']; $x < $point['x'] + $size['w']; $x++) {
            for ($y = $point['y']; $y < $point['y'] + $size['h']; $y++) {
                if (!multi_array_key_exists($area, $y, $x)) {
                    $area[$y][$x] = $id;
                    continue;
                } else {
                    $area[$y][$x] = 'X';
                }
            }
        }

        ksort($area);
    }

    // beauty_coordinates_printer($area);

    $counter = array_reduce(
        $area,
        fn($acc, $curr) => $acc +
            array_reduce(
                $curr,
                fn($acc1, $curr1) => $curr1 === 'X' ? $acc1 + 1 : $acc1,
                0
            ),
        0
    );

    return $counter;
}

echo "part 1: ", part1(), PHP_EOL;

?>
