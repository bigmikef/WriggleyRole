import pytest
from wriggley_roll.calc import inc


def test_inc_3d6_234():
    set_of_dice = [2, 3, 4]
    result = inc(set_of_dice=set_of_dice, num_faces=6)
    assert result
    assert set_of_dice == [3, 3, 4]


def test_inc_3d6_534():
    set_of_dice = [5, 3, 4]
    result = inc(set_of_dice=set_of_dice, num_faces=6)
    assert result
    assert set_of_dice == [6, 3, 4]


def test_inc_3d6_634():
    set_of_dice = [6, 3, 4]
    result = inc(set_of_dice=set_of_dice, num_faces=6)
    assert result
    assert set_of_dice == [1, 4, 4]


def test_inc_3d6_664():
    set_of_dice = [6, 6, 4]
    result = inc(set_of_dice=set_of_dice, num_faces=6)
    assert result
    assert set_of_dice == [1, 1, 5]


def test_inc_3d6_666():
    set_of_dice = [6, 6, 6]
    result = inc(set_of_dice=set_of_dice, num_faces=6)
    assert not result
    assert set_of_dice == [1, 1, 1]
