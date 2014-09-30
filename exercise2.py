#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Sam Novak and Jodie Church'

__copyright__ = "2014 Sam Novak and Jodie Church"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def checksum (upc):
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
    # raise TypeError if not string
    if type(upc) is str:
        # check length of string
        # raise ValueError if not 12
        if len(upc) != 12:
            raise ValueError("UPC must be 12 characters")
    else:
        raise TypeError("Invalid type passed as parameter")
    # convert string to array
    # hint: use the list function
    upc_list = list(upc)
    print(upc_list)

    # generate checksum using the first 11 digits provided
    # check against the the twelfth digit

    # return True if they are equal, False otherwise

    return False

checksum('03600029145x')