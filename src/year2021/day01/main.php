<?php

require_once("./src/baseday.php");

class Day extends BaseDay {

    public function __construct() {
        parent::__construct(__DIR__);
    }

    public function transform_input(array $input_list): array {
        return array_map('intval', $input_list);
    }

    public function part1(array $l): int {
        $count = 0;
        foreach ($l as $key => $value) {
            if ($key == count($l)-1)
                break;
            if ($l[$key] < $l[$key+1])
                $count++;
        }
        return $count;
    }

    public function part2(array $l, ?int $window = 3): int {
        $count = 0;
        foreach ($l as $key => $value) {
            if ($key == count($l)-$window)
                break;
            if (array_sum(array_slice($l, $key, $window)) < array_sum(array_slice($l, $key+1, $window)))
                $count++;
        }
        return $count;
    }
}


if (!debug_backtrace()) {
    $day = new Day();
    $day->test_part1(7);
    $day->main_part1(1692);
    $day->test_part2(5);
    $day->main_part2(1724);

    $day->time_part1();
    $day->time_part2();
}
