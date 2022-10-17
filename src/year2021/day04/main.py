from copy import deepcopy
from typing import List, Tuple

import numpy as np

from src.baseday import BaseDay


class Day(BaseDay):
    input_type = Tuple[List[int], List[np.ndarray]]

    def __init__(self) -> None:
        super().__init__(__file__)

    def transform_input(self, input_list: List[str]) -> input_type:
        draws = [int(s) for s in input_list[0].split(",")]

        boards = []
        for block in range(2, len(input_list), 6):
            boards.append(
                np.array(
                    [
                        np.fromstring(input_list[block + 0], dtype=int, sep=" "),
                        np.fromstring(input_list[block + 1], dtype=int, sep=" "),
                        np.fromstring(input_list[block + 2], dtype=int, sep=" "),
                        np.fromstring(input_list[block + 3], dtype=int, sep=" "),
                        np.fromstring(input_list[block + 4], dtype=int, sep=" "),
                    ]
                )
            )

        return draws, boards

    @staticmethod
    def part1(l: input_type) -> int:
        draws, boards = deepcopy(l)
        for draw in draws:
            for i, _ in enumerate(boards):
                boards[i] = np.where(boards[i] == draw, -1, boards[i])
                if -5 in np.sum(boards[i], axis=0) or -5 in np.sum(boards[i], axis=1):
                    boards[i] = np.where(boards[i] == -1, 0, boards[i])
                    return int(np.sum(boards[i]) * draw)
        else:
            raise Exception("No winner?")


    @staticmethod
    def part2(l: input_type) -> int:
        draws, boards = deepcopy(l)
        for draw in draws:
            for i, _ in enumerate(boards):
                boards[i] = np.where(boards[i] == draw, -1, boards[i])
                if -5 in np.sum(boards[i], axis=0) or -5 in np.sum(boards[i], axis=1):
                    boards[i] = np.where(boards[i] == -1, 0, boards[i])
                    winner = int(np.sum(boards[i]) * draw)
                    if winner == 1272:
                        print(i)
                        print(draw)
                    del boards[i]
        return winner


if __name__ == "__main__":
    try:
        day = Day()
        day.test_part1(4512)
        day.main_part1(58838)
        day.test_part2(1924)
        day.main_part2()

        day.time_part1()
        # day.time_part2()
    except KeyboardInterrupt:
        print("Interrupted by user.")
