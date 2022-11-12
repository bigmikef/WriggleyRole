import pytest
from wriggley_roll.calc import roll_die


def test_roll_die_d6():
    assert roll_die(6) == [1, 2, 3, 4, 5, 6]


# def test_roll_dice_2d6():
#    assert roll_dice('2d6') == [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 11, 11, 12]
