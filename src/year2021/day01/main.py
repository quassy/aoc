from typing import List

from src.baseday import BaseDay


class Day(BaseDay):
    input_type = List[int]

    def __init__(self) -> None:
        super().__init__(__file__)

    def transform_input(self, input_list: List[str]) -> input_type:
        return [int(d) for d in input_list]

    @staticmethod
    def part1(l: input_type) -> int:
        return sum(1 for k, v in enumerate(l[:-1]) if v < l[k + 1])

    @staticmethod
    def part2(l: input_type, window: int = 3) -> int:
        return sum(1 for k, v in enumerate(l[:-window]) if v < l[k + window])


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
