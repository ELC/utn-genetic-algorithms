"""Console Utilities"""

from os import system as system_call
from platform import system as system_name

def clear_screen():
    """Clears the terminal screen."""
    if system_name().lower() == "windows":
        command = "cls"
    else:
        command = "clear"

    system_call(command)
