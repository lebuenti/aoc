<?php

function part2() {
    $frequency = 0;
    $frequencies = array();

    while (true) {
        foreach (file('./inputs/1.txt') as $line) {
            if ($line[0] === '+') {
                $frequency += intval(substr($line, 1));
            } else if ($line[0] === '-') {
                $frequency -= intval(substr($line, 1));
            }

            if (in_array($frequency, $frequencies)) {
                return $frequency;
            }
            array_push($frequencies, $frequency);
        }
    }
}

echo "part 1: ", array_reduce(
    file('./inputs/1.txt'),
    fn($acc, $curr) => $acc + intval($curr),
    0
), PHP_EOL;

echo "part 2: ", part2(), PHP_EOL;

?>