#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

"""

__author__ = 'Sam Novak and Jodie Church'

__copyright__ = "2014 Sam Novak and Jodie Church"
__license__ = "MIT License"

__status__ = "Prototype"


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    letter_grade_to_gpa = {
        'A+': 4.0,
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'FZ': 0.0
    }

    percent_grade_to_letter = {
        (90, 100): 'A+',
        (85, 89): 'A',
        (80, 84): 'A-',
        (77, 79): 'B+',
        (73, 76): 'B',
        (70, 72): 'B-',
        (0, 69): 'FZ'
    }

    if type(grade) is str:
        # convert grade to uppercase
        grade = grade.upper()
        # check if inputted grade exists as key in the letter to grade dictionary
        if grade in letter_grade_to_gpa:
            # return the value of the key
            return letter_grade_to_gpa[grade]
        else:
            # if letter grade is not in dictionary
            raise ValueError("Accepted letter grades are: A+, A, A-, B+, B, B-, FZ")
    elif type(grade) is int:
        # check if inputted grade is within 1 - 100 inclusive
        if grade in range(0, 101):
            # loop through conversion dictionary
            for percent_range, letter_grade in percent_grade_to_letter.items():
                # check if grade is between hi/low in key
                if grade in range(percent_range[0], percent_range[1]+1):
                    # return the value of key that the grade falls within
                    return letter_grade_to_gpa[letter_grade]
        else:
            # if integer input is not between 0 - 100
            raise ValueError("Number grades must be in the range of 0 to 100")

    else:
        # if neither string nor integer is inputted raise a TypeError exception
        raise TypeError("Invalid type passed as parameter")

