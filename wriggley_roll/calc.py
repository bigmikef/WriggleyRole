#!/usr/bin/env python3
import sys
from enum import Enum
from tabulate import tabulate
from dataclasses import dataclass
from numpy import arange


class AutoNumber(Enum):
    def __new__(cls, *args):  # this is the only change from above
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj


class DC(AutoNumber):
    def __init__(self, prob: float = 0.0, per: float = 0.0) -> None:
        super().__init__()
        self.probability = prob
        self.percentage = per

    def __str__(self) -> str:
        return f"{self.name} - {self.percentage}"

    VERY_EASY = (0.90, 90.0)
    EASY = (0.75, 75.0)
    MODERATE = (0.50, 50.0)
    HARD = (0.25, 25.0)
    VERY_HARD = (0.10, 10.0)
    NEARLY_IMPOSSIBLE = (0.005, 0.5)


@dataclass
class ProbabiltityScore:
    num_at_or_higher: int
    num_elements: int
    prob: float


def prob_succusful_dc(dc: int, roll_list: list[int]) -> float:
    num_at_of_higher = 0
    for _i in roll_list:
        if _i >= dc:
            num_at_of_higher += 1
    return num_at_of_higher / roll_list.__len__()


def join_roll_list(faces: int, roll_list: list[int]) -> list[int]:
    ret = []
    for _i in range(1, faces + 1):
        for _l in roll_list:
            ret.append(_i + _l)
    return ret


def roll_die(faces: int) -> list[int]:
    return arange(1, faces + 1).tolist()


def inc(set_of_dice: list[int], num_faces: int) -> bool:
    return inc(set_of_dice, 0, num_faces)


def inc(set_of_dice: list[int], num_faces: int) -> bool:
    for r in range(set_of_dice.__len__()):
        next_num_found = False
        while set_of_dice[r] < num_faces:
            set_of_dice[r] += 1
            next_num_found = True
            break
        if next_num_found:
            break
        else:
            set_of_dice[r] = 1
    # print(f"r={r} -- {set_of_dice}")
    if r == set_of_dice.__len__() - 1:
        return False
    return True


def roll_dice(num: int, faces: int) -> list[int]:
    a_roll = [1 for i in range(0, num)]
    ret = [sum(a_roll)]
    while inc(a_roll, faces):
        ret.append(sum(a_roll))
    return ret


def prob(score: int, roll_list: list[int]) -> ProbabiltityScore:
    num_at_or_higher = [_i for _i in roll_list if _i >= score]
    card_higher = num_at_or_higher.__len__()
    return ProbabiltityScore(
        num_at_or_higher=card_higher,
        num_elements=roll_list.__len__(),
        prob=card_higher / roll_list.__len__(),
    )


def prob_table(num_players: tuple[int, int], faces: int) -> dict[int, dict[int, int]]:
    roll_lists: dict[int, list[int]] = {}
    for num_dice in range(1, num_players[1] + 1):
        print(f"starting dice count {num_dice}")
        roll_lists[num_dice] = roll_dice(num_dice, faces)
        print(f"done")

    prob_lists: dict[int, dict[int, int]] = {}
    for num_dice in range(num_players[0], num_players[1] + 1):

        die_prob_list: dict[int, int] = {}
        for dc in range(1, (faces * num_dice) + 1):
            die_prob_list[dc] = prob_succusful_dc(dc, roll_list=roll_lists[num_dice])
            print(f"num_dice={num_dice} dc({dc})")
        prob_lists[num_dice] = die_prob_list

    return prob_lists


def table_prob_list(
    num_players: int, faces: int, prob_lists: dict[int, dict[int, int]]
):

    data: list[list[str]] = []
    for num_die in range(1, num_players + 1):
        data_row: list[any] = []
        data_row.extend([0 for dc in prob_lists[num_die].keys()])
        print(f"data_row:{data_row}")
        for dc, prob in prob_lists[num_die].items():
            print(f"num_die:{num_die} dc:{dc}")
            data_row[dc - 1] = prob
        list: list[any] = [num_die]
        list.extend(data_row)
        print(f"list:{list}")
        data.append(list)

    header = ["Players"]
    header.extend([str(i) for i in range(1, (faces * num_players) + 1)])
    print(f"data:{data}")
    print(tabulate(data, headers=header))


def get_stuff():
    min_players = 3
    max_players = 8
    faces = 20
    prob_matrix = prob_table(num_players=(min_players, max_players), faces=faces)
    scores_table: dict[int, dict[DC, (int, float)]] = {}
    for num_players in sorted(prob_matrix.keys()):
        result_row: dict[DC, (int, str)] = {}
        prob_row = prob_matrix[num_players]
        for _dc_level in list(DC):
            for rolled_score in sorted(prob_row.keys()):
                if _dc_level.probability >= prob_row[rolled_score]:
                    _prob = f"{prob_row[rolled_score] * 100:.2f}%"
                    result_row[_dc_level] = (
                        rolled_score,
                        _prob,
                    )
                    break  # current iteration over rolled_scores for _dc_level
        scores_table[num_players] = result_row

    print(f"scores_table:{scores_table}")
    header = ["Players"]
    header.extend([i for i in list(DC)])
    data = []
    for num_players in scores_table.keys():
        data_row = [num_players]
        for dc in list(DC):
            data_row.append(scores_table[num_players][dc])
        data.append(data_row)

    print(tabulate(data, headers=header))


def main() -> int:
    # prob_table(2, 20)
    get_stuff()


if __name__ == "__main__":
    sys.exit(main())
