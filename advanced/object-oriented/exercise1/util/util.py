"""Utilities module, support functions"""

from numpy.random import randint
from numpy.random import choice

"""##################################"""
"""Random Number Generation Functions"""
"""##################################"""

def get_random_number_string(length, binary=False):
    """Generate a random number either from decimal or binary,
        depending on the parameter binary"""
    if binary:
        return get_random_number_string_binary(length)
    else:
        return get_random_number_string_decimal(length)

def get_random_number_string_binary(length):
    """Return a random number from binary"""
    list_string = []
    for _ in range(length):
        random_bit = get_random_number(0, 1)
        char_random_bit = str(random_bit)
        list_string.append(char_random_bit)
    string = "".join(list_string)
    return string

def get_random_number_string_decimal(length):
    """Return a random number from decimal"""
    maximum = 2 ** length - 1
    dec_gene = get_random_number(0, maximum)
    bin_gene = dec_to_bin(dec_gene)
    gene = _fill(bin_gene, length)
    return gene

def get_random_number(start, end):
    """Return a random number between the given start and end"""
    number = randint(start, end+1)
    return number

def _fill(raw, length, neutral="0"):
    """Given a string, fill the the given neutral character until it reaches
        the given length"""
    raw_gene = list(raw)
    while len(raw_gene) < length:
        raw_gene.insert(0, neutral)
    filled_gene = "".join(raw_gene)
    return filled_gene

"""####################"""
"""Conversion Functions"""
"""####################"""

def dec_to_bin(number):
    """Convert a given number from Decimal to Binary."""
    return bin(number)[2:]

def bin_to_dec(number):
    """Convert a given number from Binary to Decimal."""
    return int(number, 2)

"""############################"""
"""Array manipulation Functions"""
"""############################"""

def get_next_two(array):
    """Yields the next two elements of an array"""
    get_next = _get_next(array)
    length = len(array) // 2
    for _ in range(length):
        yield next(get_next), next(get_next)

def _get_next(array):
    for element in array:
        yield element

def choose_n_elements_from_narray(array, weight):
    return choice(array, p=weight) 

"""#####################"""
"""Probability functions"""
"""#####################"""

def get_random_prob(precision=2):
    """Return a random probability (between 0 and 1) with given precision."""
    toplimit = 10 ** precision
    percentage = get_random_number(0, toplimit)
    prob = percentage / toplimit
    return prob

def get_precision(number):
    """Given a number, return how many digits after the decimal point has"""
    test_safe_number = number + 1
    string = str(test_safe_number)
    decimal_places = string[::-1].find('.')
    return decimal_places
