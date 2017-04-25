"""Target Function"""

from  exercise1.logic.settings_manager import Settings 

def target(number):
    """Define a Target function."""
    exp = Settings.get_chromosome_bits() 
    coef = (2**exp) - 1 
    return (number / coef) ** 2
