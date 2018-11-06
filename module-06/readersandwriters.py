"""
File: readersandwriters.py
Demonstrates shared data synchonization for the readers and writers
problem.
To be completed in the programing projects.
"""

import time, random
from threading import Thread
from sharedcell import SharedCell
from counter import Counter

class Writer(Thread):
    """Increments a counter in a shared cell."""

    def __init__(self, cell, number):
        Thread.__init__(self, name = "Writer" + str(number))
        self.cell = cell

    def run(self):
        """Sleep for a random interval and then increment
        the counter in the cell."""
        print("%s starting up" % self.getName())
        time.sleep(random.randint(1, 4))
        # write, using counter's increment
        # value = ?
        print("%s is done incrementing to %d" % \
              (self.getName(), value))

class Reader(Thread):
    """Reads the value of a counter in a shared cell."""

    def __init__(self, cell, number):
        Thread.__init__(self, name = "Reader" + str(number))
        self.cell = cell

    def run(self):
        """Sleep for a random interval and then get
        the value of the counter in the cell."""
        print("%s starting up" % self.getName())
        time.sleep(random.randint(1, 4))
        # read, using counter's getValue
        # value = ?
        print("%s is done getting %d" % (self.getName(), value))

def main():
    """Creates a shared cell on a Counter object, and reader and
    writer threads to increment it and observe its value."""
    counter = Counter()
    cell = SharedCell(counter)
    threads = []
    print("Creating reader threads.")
    for i in range(1, 5):
        threads.append(Reader(cell, i))
    print("Creating writer threads.")
    for i in range(1, 3):
        threads.append(Writer(cell, i))
    print("Starting the threads.")
    for thread in threads:
        thread.start()
    
if __name__ == "__main__":
    main()

