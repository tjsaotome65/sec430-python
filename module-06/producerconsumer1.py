"""
File: producerconsumer1.py

Producer-consumer demo with no synchronization.
Producer and consumer both access shared data a given number
of times. They sleep a random interval before each access.
The data must be produced before it is consumed, and be produced
and consumed just once.
However, on some runs, the producer and consumer may access the
data out of order.
"""

import time, random
from threading import Thread, currentThread

class SharedCell(object):
    """Shared data for the producer/consumer problem."""
    
    def __init__(self):
        """Data undefined at startup."""
        self.data = -1

    def setData(self, data):
        """Producer's method to write to shared data."""
        print("%s setting data to %d" % \
              (currentThread().getName(), data))
        self.data = data

    def getData(self):
        """Consumer's method to read from shared data."""
        print("%s accessing data %d" % \
              (currentThread().getName(), self.data))
        return self.data

class Producer(Thread):
    """A producer of data in a shared cell."""

    def __init__(self, cell, accessCount, sleepMax):
        """Create a producer with the given shared cell,
        number of accesses, and maximum sleep interval."""
        Thread.__init__(self, name = "Producer")
        self.accessCount = accessCount
        self.cell = cell
        self.sleepMax = sleepMax

    def run(self):
        """Resets the data in the cell and goes to sleep,
        the given number of times."""
        print("%s starting up" % self.getName())
        for count in range(self.accessCount):
            time.sleep(random.randint(1, self.sleepMax))
            self.cell.setData(count + 1)
        print("%s is done producing\n" % self.getName())

class Consumer(Thread):
    """A consumer of data in a shared cell."""

    def __init__(self, cell, accessCount, sleepMax):
        """Create a consumer with the given shared cell,
        number of accesses, and maximum sleep interval."""
        Thread.__init__(self, name = "Consumer")
        self.accessCount = accessCount
        self.cell = cell
        self.sleepMax = sleepMax

    def run(self):
        """Announce start-up, sleep and write to shared
        cell the given number of times, and announce
        completion."""
        print("%s starting up\n" % self.getName())
        for count in range(self.accessCount):
            time.sleep(random.randint(1, self.sleepMax))
            value = self.cell.getData()
        print("%s is done consuming\n" % self.getName())

def main():
    accessCount = int(input("Enter the number of accesses: "))
    sleepMax = 4
    cell = SharedCell()
    p = Producer(cell, accessCount, sleepMax)
    c = Consumer(cell, accessCount, sleepMax)
    print("Starting the threads")
    p.start()
    c.start()

main()
