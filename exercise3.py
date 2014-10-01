#!/usr/bin/env python3

"""
    Determine the winner of Rock, Paper, Scissors game.

    This module contains one function decide_rps. It accepts two parameters
    which must be strings. The strings must be either Rock, Paper, or Scissors.
    All other inputs will result in an error.

    Assignment 1, Exercise 3, INF1340 Fall 2014
"""

__author__ = "Sam Novak and Jodie Church"

__copyright__ = "2014 Sam Novak and Jodie Church"
__license__ = "MIT License"

__status__ = "Prototype"


def decide_rps(player1, player2):

    """
    Returns the winning player number based on a game of rock, paper, scissors.

    :param:
        player1 (string): accepted values are Rock, Paper, Scissors
        player2 (string): accepted values are Rock, Paper, Scissors

    :return:
        integer:
            Value is 0 if it’s a tie game, 1 if Player1 wins, and 2 if Player2 wins

    :raises:
        TypeError if parameter is not a string
        ValueError if parameter is not one of Rock, Paper, or Scissors
    """
    accepted_input = ["Rock", "Paper", "Scissors"]

    game_rules = {
        ("Rock", "Paper"): 2,
        ("Rock", "Scissors"): 1,
        ("Paper", "Rock"): 1,
        ("Paper", "Scissors"): 2,
        ("Scissors", "Rock"): 2,
        ("Scissors", "Paper"): 1,
    }
    # check input type for both player1 and player2 input
    if type(player1) is str and type(player2) is str:
        # check to see if inputted strings match accepted input list
        if player1 in accepted_input and player2 in accepted_input:
            # if parameters are the same return 0, a tie.
            if player1 == player2:
                return 0
            # if parameters do not match
            else:
                current_game = (player1, player2)  # create tuple with parameters
                return game_rules[current_game]  # return value from the key that matches tuple for the current game
        else:
            # raise ValueError either payer1 or player2 parameters are not in accepted values
            raise ValueError("Accepted letter grades are: Rock, Paper, Scissors")
    else:
        # raise TypeError if not string
        raise TypeError("Invalid type passed as parameter")
