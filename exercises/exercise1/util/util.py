"""Utilities module, support functions"""

from numpy.random import randint
from numpy.random import choice

def get_random_prob(precision=2):
    """Return a random probability (between 0 and 1) with given precision."""
    toplimit = 10 ** precision
    percentage = get_random_number(0, toplimit)
    prob = percentage / toplimit
    return prob

def get_random_number_string(length, binary=False):
    if binary:
        return get_random_number_string_binary(length)
    else:
        return get_random_number_string_decimal(length)

def get_random_number_string_binary(length):
    list_string = []
    for _ in range(length):
        random_bit = get_random_number(0, 1)
        char_random_bit = str(random_bit)
        list_string.append(char_random_bit)
    string = "".join(list_string)
    return string

def get_random_number_string_decimal(length):
    maximum = 2 ** length - 1
    dec_gene = get_random_number(0, maximum)
    bin_gene = dec_bin(dec_gene)
    gene = _fill(bin_gene, length)
    return gene

def get_random_number(start, end):
    """Return a random probability (between 0 and 1) with given precision."""
    number = randint(start, end+1)
    return number

def dec_bin(number):
    """ Convert X from Decimal to Binary."""
    return bin(number)[2:]

def _fill(raw, lenght, neutral="0"):
    raw_gene = list(raw)
    while len(raw_gene) < lenght:
        raw_gene.insert(0, neutral)
    filled_gene = "".join(raw_gene)
    return filled_gene

def get_next_two(array):
    """Yields the next two elements of an array"""
    get_next = _get_next(array)
    lenght = len(array) // 2
    for _ in range(lenght):
        yield next(get_next), next(get_next)

def _get_next(array):
    for element in array:
        yield element





def get_precision(number):
    test_safe_number = number + 1
    string = str(test_safe_number)
    decimal_places = string[::-1].find('.')
    return decimal_places

def choose_n_elements_from_narray(array, weight=None):
    if weight is None:
        element = choice(array)
    else:
        element = choice(array, p=weight)    
    return element
