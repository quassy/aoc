from typing import List, Tuple

from src.baseday import BaseDay


class Day(BaseDay):
    input_type = List[Tuple[str, int]]

    def __init__(self) -> None:
        super().__init__(__file__)

    def transform_input(self, input_list: List[str]) -> input_type:
        return [(d.split()[0], int(d.split()[1])) for d in input_list]

    def part1(self, l: input_type) -> int:
        horizontal = sum(f[1] for f in l if f[0] == "forward")
        vertical = sum(f[1] for f in l if f[0] == "down") - sum(f[1] for f in l if f[0] == "up")
        return horizontal * vertical

    def part2(self, l: input_type) -> int:
        aim = 0
        horizontal = 0
        vertical = 0
        for d in l:
            if d[0] == "down":
                aim += d[1]
            elif d[0] == "up":
                aim -= d[1]
            elif d[0] == "forward":
                horizontal += d[1]
                vertical += d[1] * aim
        return horizontal * vertical


if __name__ == "__main__":
    try:
        day = Day()
        day.test_part1(150)
        day.main_part1(2091984)
        day.test_part2(900)
        day.main_part2(2086261056)

        day.time_part1()
        day.time_part2()
    except KeyboardInterrupt:
        print("Interrupted by user.")
