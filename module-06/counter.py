"""
File: counter.py
"""

class Counter(object):
    """Models a counter."""

    # Constructor
    def __init__(self):
        """Sets up the counter."""
        self.reset()

    # Mutator methods
    def reset(self):
        """Returns the counter to 0."""
        self.value = 0

    def increment(self, amount = 1):
        """Adds amount to the counter."""
        self.value += amount
        return self.value

    def decrement(self, amount = 1):
        """Subtracts amount from the counter."""
        self.value -= amount

    # Accessor methods
    def getValue(self):
        """Returns the counter's value."""
        return self.value

    def __str__(self):
        """Returns the string representation of the counter."""
        return str(self.value)

    def __eq__(self, other):
        """Returns True if self equals other or False otherwise."""
        if self is other: return True
        if type(self) != type(other): return False
        return self.value == other._value
                
