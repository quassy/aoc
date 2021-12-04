from typing import List

from src.baseday import BaseDay


class Day(BaseDay):
    input_type = List[int]

    def __init__(self) -> None:
        super().__init__(__file__)

    def transform_input(self, input_list: List[str]) -> input_type:
        return [int(d.replace("\n", "")) for d in input_list]

    def part1(self, l: input_type) -> int:
        return 0

    def part2(self, l: input_type) -> int:
        return 0


if __name__ == "__main__":
    try:
        day = Day()
        day.test_part1(198)
        day.test_part2()
        day.main_part1()
        day.main_part2()
    except KeyboardInterrupt:
        print("Interrupted by user.")
