<?php

class BaseDay {
    protected int $repeat_count = 1000;

    public function __construct(string $path) {
        $this->test_input = $this->transform_input(file($path."/test_input.txt", FILE_IGNORE_NEW_LINES));
        $this->input = $this->transform_input(file($path."/input.txt", FILE_IGNORE_NEW_LINES));
    }

    public function transform_input(array $input_list): array {
        return $input_list;
    }

    public function test_part1(?int $test_output = 0): void {
        echo(__FUNCTION__.": ");
        echo($this->part1($this->test_input)."\n");
        if ($test_output)
            assert($this->part1($this->test_input) == $test_output);
    }

    public function test_part2(?int $test_output = 0): void {
        echo(__FUNCTION__.": ");
        echo($this->part2($this->test_input)."\n");
        if ($test_output)
            assert($this->part2($this->test_input) == $test_output);
    }

    public function main_part1(?int $main_output = 0): void {
        echo(__FUNCTION__.": ");
        echo($this->part1($this->input)."\n");
        if ($main_output)
            assert($this->part1($this->input) == $main_output);
    }

    public function main_part2(?int $main_output = 0): void {
        echo(__FUNCTION__.": ");
        echo($this->part2($this->input)."\n");
        if ($main_output)
            assert($this->part2($this->input) == $main_output);
    }

    # @time_func(repeat_count)
    public function time_part1(): void {
        $this->part1($this->input);
    }

    # @time_func(repeat_count)
    public function time_part2(): void {
        $this->part2($this->input);
    }

    public function part1(array $input_list): int {
        return 0;
    }

    public function part2(array $input_list): int {
        return 0;
    }

}
