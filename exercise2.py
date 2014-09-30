#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Sam Novak and Jodie Church'

__copyright__ = "2014 Sam Novak and Jodie Church"
__license__ = "MIT License"

__status__ = "Prototype"


def checksum(upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """
    # check type of input
    if type(upc) is str:
        # check length of string
        if len(upc) != 12:
            # raise ValueError if not 12
            raise ValueError("UPC must be 12 characters")
    else:
        # raise TypeError if not string
        raise TypeError("Invalid type passed as parameter")

    # convert string to array the list function
    upc_list = list(upc)

    # begin calculation for UPC checksum
    # initialize variable for the sum of odd numbers
    odd_sum = 0
    for digit in upc_list[0::2]:  # loop through every other digit in list starting from first item
        odd_sum += int(digit)  # add integer value of digit to odd_sum

    # initialize variable for the sum of even numbers
    even_sum = 0
    for digit in upc_list[1:11:2]:  # loop through every other digit in list starting from second item
        even_sum += int(digit)  # add integer value of digit to even_sum

    # perform multiplication, addition, and modulo operations
    check_sum = (even_sum + (odd_sum * 3)) % 10

    # condition operation if check_cum i
    if check_sum != 0:
        check_sum = 10 - check_sum

    if check_sum == int(upc_list[11]):
        return True
    else:
        return False
