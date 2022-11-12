import pytest
from wriggley_roll.calc import roll_die, roll_dice, prob


def test_prob_of_a_12():
    roll_list = roll_dice(num=2, faces=6)
    result = prob(score=12, roll_list=roll_list)
    assert result.num_at_or_higher == 1
    assert result.num_elements == 36
    assert result.prob == 1/36
    
def test_prob_of_a_10():
    roll_list = roll_dice(num=2, faces=6)
    result = prob(score=10, roll_list=roll_list)
    assert result.num_at_or_higher == 6
    assert result.num_elements == 36
    assert result.prob == 1/6

def test_roll_die_d6():
    assert roll_die(6) == [1, 2, 3, 4, 5, 6]


def test_roll_dice_2d6():
    assert roll_dice(num=2, faces=6) == [
        2,
        3,
        3,
        4,
        4,
        4,
        5,
        5,
        5,
        5,
        6,
        6,
        6,
        6,
        6,
        7,
        7,
        7,
        7,
        7,
        7,
        8,
        8,
        8,
        8,
        8,
        9,
        9,
        9,
        9,
        10,
        10,
        10,
        11,
        11,
        12,
    ]
