import inspect
import os
from os import PathLike
from pathlib import Path
from typing import List, Optional


class BaseDay:
    def __init__(self, file: PathLike) -> None:
        path = Path(file).parent.resolve()
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

    def part1(self, input_list: list) -> int:
        pass

    def part2(self, input_list: list) -> int:
        pass
