from typing import List

import numpy as np

from src.baseday import BaseDay


class Day(BaseDay):
    input_type = np.ndarray

    def __init__(self) -> None:
        super().__init__(__file__)

    def transform_input(self, input_list: List[str]) -> input_type:
        return np.array([list(b) for b in input_list], dtype="int")

    def part1(self, l: input_type) -> int:
        sums = l.sum(axis=0)
        gamma = ""
        for s in sums:
            if s > l.shape[0] // 2:
                gamma += "1"
            elif s < l.shape[0] // 2:
                gamma += "0"
        gamma = int(gamma, base=2)
        epsilon = 2 ** l.shape[1] - 1 - gamma
        return gamma * epsilon

    def part2(self, l: input_type) -> int:
        for col in range(l.shape[1] - 1, 0 - 1, -1):
            l = l[l[:, col].argsort(kind="mergesort")]

        oxy = None
        row_oxy_start = 0
        row_oxy_end = l.shape[0]
        co2 = None
        row_co2_start = 0
        row_co2_end = l.shape[0]
        for col in range(0, l.shape[1]):
            ones_oxy = int(np.sum(l[row_oxy_start:row_oxy_end, col]))
            zeroes_oxy = (row_oxy_end - row_oxy_start) - ones_oxy

            if oxy is None:
                # Are at least half of numbers in this column 1?
                if ones_oxy >= zeroes_oxy:
                    # Then use the majority: the second part with 1s of this column
                    row_oxy_start += zeroes_oxy
                else:
                    # Else use majority: the first part with 0s of this column
                    row_oxy_end -= ones_oxy

                if row_oxy_end - row_oxy_start == 1:
                    oxy = l[row_oxy_start:row_oxy_end, :][0]
                    oxy = int(str(oxy)[1::2], base=2)

            ones_co2 = int(np.sum(l[row_co2_start:row_co2_end, col]))
            zeroes_co2 = (row_co2_end - row_co2_start) - ones_co2

            if co2 is None:
                # Are at least half of numbers in this column 1?
                if ones_co2 >= zeroes_co2:
                    # The use the minority: the first part with 0s of this column
                    row_co2_end -= ones_co2
                else:
                    # Else use the minority: the second part with 1s of this column
                    row_co2_start += zeroes_co2

                if row_co2_end - row_co2_start == 1:
                    co2 = l[row_co2_start:row_co2_end, :][0]
                    co2 = int(str(co2)[1::2], base=2)

        return oxy * co2


if __name__ == "__main__":
    try:
        day = Day()
        day.test_part1(198)
        day.main_part1(3895776)
        day.test_part2(230)
        day.main_part2(7928162)
    except KeyboardInterrupt:
        print("Interrupted by user.")
