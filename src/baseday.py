import inspect
import os
from os import PathLike
from pathlib import Path
from typing import List, Optional

from src.time import time_func


class BaseDay:
    repeat_count = 1000

    def __init__(self, file: PathLike) -> None:
        path = Path(file).parent.resolve()

        self.test_input = (path / "test_input.txt").read_text()
        self.input = (path / "input.txt").read_text()

        with open(os.path.join(path, "test_input.txt")) as f:
            self.test_input = self.transform_input(f.read().splitlines())
        with open(os.path.join(path, "input.txt")) as f:
            self.input = self.transform_input(f.read().splitlines())

    def transform_input(self, input_list: List[str]) -> list:
        return input_list

    def test_part1(self, test_output: Optional[int] = None) -> None:
        print(inspect.stack()[0][3], end=": ")
        print(self.part1(self.test_input))
        if test_output:
            assert self.part1(self.test_input) == test_output

    def test_part2(self, test_output: Optional[int] = None) -> None:
        print(inspect.stack()[0][3], end=": ")
        print(self.part2(self.test_input))
        if test_output:
            assert self.part2(self.test_input) == test_output

    def main_part1(self, main_output: Optional[int] = None) -> None:
        print(inspect.stack()[0][3], end=": ")
        print(self.part1(self.input))
        if main_output:
            assert self.part1(self.input) == main_output

    def main_part2(self, main_output: Optional[int] = None) -> None:
        print(inspect.stack()[0][3], end=": ")
        print(self.part2(self.input))
        if main_output:
            assert self.part2(self.input) == main_output

    @time_func(repeat_count)
    def time_part1(self) -> None:
        self.part1(self.input)

    @time_func(repeat_count)
    def time_part2(self) -> None:
        self.part2(self.input)

    @staticmethod
    def part1(input_list: list) -> int:
        pass

    @staticmethod
    def part2(input_list: list) -> int:
        pass
