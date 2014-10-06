#!/usr/bin/env python3

import pytest
from exercise3 import decide_rps


def test_rules():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Paper", "Rock") == 1
    assert decide_rps("Paper", "Scissors") == 2
    assert decide_rps("Scissors", "Rock") == 2
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("rock", "scissors") == 1  # lowercase test


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        decide_rps(3, 4)
        decide_rps(121)

    with pytest.raises(ValueError):
        decide_rps("Rocks", "Paper")
        decide_rps("Papers", "Scissors")


test_rules()
test_input()