from typing import List

from src.baseday import BaseDay


class Day(BaseDay):
    input_type = List[int]

    def __init__(self) -> None:
        super().__init__(__file__)

    def transform_input(self, input_list: List[str]) -> input_type:
        return [int(d.replace("\n", "")) for d in input_list]

    def part1(self, l: input_type) -> int:
        return sum(1 for k, v in enumerate(l[:-1]) if l[k] < l[k + 1])

    def part2(self, l: input_type, window: int = 3) -> int:
        return sum(
            1
            for k, v in enumerate(l[:-window])
            if sum(l[k : k + window]) < sum(l[k + 1 : k + 1 + window])
        )


if __name__ == "__main__":
    try:
        day = Day()
        day.test_part1(7)
        day.test_part2(5)
        day.main_part1(1692)
        day.main_part2(1724)
    except KeyboardInterrupt:
        print("Interrupted by user.")
