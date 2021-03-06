from typing import List

import numpy as np
from numba import jit

from src.baseday import BaseDay


class Day(BaseDay):
    input_type = np.ndarray

    def __init__(self) -> None:
        super().__init__(__file__)

    def transform_input(self, input_list: List[str]) -> input_type:
        return np.array([int(d) for d in input_list])

    @staticmethod
    @jit
    def part1(l: input_type) -> int:
        return sum([1 for k, v in enumerate(l[:-1]) if l[k] < l[k + 1]])

    @staticmethod
    def part2(l: input_type, window: int = 3) -> int:
        l = [sum(l[i : i + window]) for i, v in enumerate(l[: -window + 1])] if window > 1 else l
        return sum(1 for k, v in enumerate(l[:-1]) if l[k] < l[k + 1])


if __name__ == "__main__":
    try:
        day = Day()
        day.test_part1(7)
        day.main_part1(1692)
        day.test_part2(5)
        day.main_part2(1724)

        day.time_part1()
        day.time_part2()
    except KeyboardInterrupt:
        print("Interrupted by user.")
