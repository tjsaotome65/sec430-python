"""
File: threadsafetranscript.py
Project 10.10
This module defines a thread-safe Transcript class.
"""

from transcript import Transcript
from sharedcell import SharedCell

class ThreadSafeTranscript(object):
    """This class represents a thread-safe transcript."""

    def __init__(self):
        """Wrap a new transcript in a shared cell for
        thread-safety."""
        transcript = Transcript()
        self.cell = SharedCell(transcript)

    def __str__(self):
        """Returns the string rep of the transcript."""
        return self.cell.read(lambda transcript: str(transcript))

    def add(self, message):
        """Adds message to transcript."""
        return self.cell.write(lambda transcript: transcript.add(message))
