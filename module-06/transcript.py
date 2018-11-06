"""
File: transcript.py
Project 10.10
This module defines the Transcript class.
"""

class Transcript(object):
    """This class represents transcript of chat messages."""

    def __init__(self):
        """Creates a list of messages."""
        self.messages = ["No messages yet!\n"]

    def __str__(self):
        """Returns the join of all messages,
        separated by newlines."""
        return '\n'.join(self.messages)

    def add(self, message):
        """Adds message to list of messages."""
        self.messages.append(message)
