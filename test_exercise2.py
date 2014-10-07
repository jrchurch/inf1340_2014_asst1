#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = "Sam Novak and Jodie Church"

__copyright__ = "2014 Sam Novak and Jodie Church"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

# imports one per line
import pytest
from exercise2 import checksum


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000841") is False
    assert checksum("123456789123") is False


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0)  # Test float
        checksum(786936224306)  # Test Integer

    with pytest.raises(ValueError):
        checksum("1")  # test length of input
        checksum("1234567890")

