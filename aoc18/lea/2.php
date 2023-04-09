<?php

function part1() {
    $amounts = [];
    $ids = [];

    foreach (file('./inputs/2.txt') as $line) {
        $chars = count_chars($line, 1);

        //Delete entries that occur only once.
        while (($key = array_search(1, $chars)) !== false) {
            unset($chars[$key]);
        }

        $unique = array_unique($chars);

        if (sizeof($unique) === 0) {
            continue;
        }

        array_push($ids, $line);

        foreach ($unique as $char) {
            $amounts[$char] = array_key_exists($char, $amounts) ? $amounts[$char] + 1 : 1;
        }

    }
    return [array_reduce($amounts, fn($acc, $curr) => $acc * $curr, 1), $ids];
}

function part2($ids) {
    for ($i = 0; $i < sizeof($ids); $i++) {
        for ($j = 0; $j < sizeof($ids); $j++) {

            if ($j === $i) {
                continue;
            }

            $counter = 0;
            $index = -1;
            for ($k = 0; $k < strlen($ids[$i]); $k++) {
                if ($ids[$i][$k] !== $ids[$j][$k]) {
                    $counter++;
                    $index = $k;
                }
                if ($counter > 1) {
                    break;
                }
            }

            if ($counter === 1) {
                return substr_replace($ids[$i], '', $index, 1);
            }
        }
    }
}

$res = part1();

echo "part 1: ", $res[0], PHP_EOL;
echo part2($res[1]), PHP_EOL;

?>