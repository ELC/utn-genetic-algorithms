"""Utilities module, support functions"""

import matplotlib.pyplot as plt
from numpy.random import randint

def get_random_prob(precision=2):
    """Return a random probability (between 0 and 1) with given precision."""
    toplimit = 10 ** precision
    percentage = randint(0, toplimit)
    prob = percentage / toplimit
    return prob

def get_random_number(start, end):
    """Return a random probability (between 0 and 1) with given precision."""
    number = randint(start, end)
    return number

def dec_bin(number):
    """ Convert X from Decimal to Binary."""
    return bin(number)[2:]

def find_bigger(array, value):
    """Given a value and a sorted array, find the closest bigger element."""
    for i, j in enumerate(array):
        if value <= j:
            return i
