"""
File: threadsafesavingsaccount.py
This module defines a thread-safe SavingsAccount class.

This example uses decorator to add functionality of thread safe object to existing SavingsAccount object

"""

from savingsaccount import SavingsAccount
from sharedcell import SharedCell


class ThreadSafeSavingsAccount:
    """This class represents a thread-safe savings account
    with the owner's name, PIN, and balance."""

    def __init__(self, name, pin, balance = 0.0):
        """Wrap a new account in a shared cell for thread-safety."""
        account = SavingsAccount(name, pin, balance)
        self.cell = SharedCell(account)

    def __str__(self):
        """Returns the string rep of the account."""
        return self.cell.read(lambda account: str(account))

    def getBalance(self):
        """Returns the current balance."""
        return self.cell.read(lambda account: account.getBalance())

    def getName(self):
        """Returns the current name."""
        return self.cell.read(lambda account: account.getName())

    def getPin(self):
        """Returns the current pin."""
        return self.cell.read(lambda account: account.getPin())

    def deposit(self, amount):
        """If the amount is valid, adds it
        to the balance and returns None;
        otherwise, returns an error message."""
        return self.cell.write(lambda account: account.deposit(amount))

    # Other methods are exercises

