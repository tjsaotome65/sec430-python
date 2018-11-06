"""
File: sleepythreads.py
Illustrates concurrency with multiple threads.
"""

import random, time
from threading import Thread

class SleepyThread(Thread):
    """Represents a sleepy thread."""

    def __init__(self, number, sleepMax):
        """Create a thread with the given name 
        and a random sleep interval less than the maximum. """
        Thread.__init__(self, name = "Thread " + str(number))
        self.sleepInterval = random.randint(1, sleepMax)

    def run(self):
        """Print the thread's name and sleep interval and sleep
        for that interval. Print the name again at wakeup. """
        print("%s starting, with sleep interval: %d seconds" % \
              (self.getName(), self.sleepInterval))
        time.sleep(self.sleepInterval)
        print("%s waking up" % self.getName())

def main():
    """Create the user's number of threads with sleep
    intervals less than the user's maximum. Then start
    the threads"""
    numThreads = int(input("Enter the number of threads: "))
    sleepMax = int(input("Enter the maximum sleep time: "))
    threadList = []
    for count in range(numThreads):
        threadList.append(SleepyThread(count + 1, sleepMax))
    for thread in threadList: thread.start()

if __name__ == "__main__":
    main()
