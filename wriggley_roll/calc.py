#!/usr/bin/env python3
import sys
from tabulate import tabulate
from dataclasses import dataclass
from numpy import arange


@dataclass
class ProbabiltityScore:
    num_at_or_higher: int
    num_elements: int
    prob: float


def join_roll_list(faces: int, roll_list: list[int]) -> list[int]:
    ret = []
    for _i in range(1, faces + 1):
        for _l in roll_list:
            ret.append(_i + _l)
    return ret


def roll_die(faces: int) -> list[int]:
    return arange(1, faces + 1).tolist()


def roll_dice(num: int, faces: int) -> list[int]:
    if num > 1:
        return sorted(join_roll_list(faces=faces, roll_list=roll_dice(num - 1, faces)))
    else:
        return roll_die(faces)


def prob(score: int, roll_list: list[int]) -> ProbabiltityScore:
    num_at_or_higher = [_i for _i in roll_list if _i >= score]
    card_higher = num_at_or_higher.__len__()
    return ProbabiltityScore(
        num_at_or_higher=card_higher,
        num_elements=roll_list.__len__(),
        prob=card_higher / roll_list.__len__(),
    )


def main() -> int:
    # for num_dice in range(1, 11):#
    return 0


if __name__ == "__main__":
    sys.exit(main())
