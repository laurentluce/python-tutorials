import time
import urllib2
import threading
import random

class Producer(threading.Thread):
    """
    Produces random integers to a list
    """

    def __init__(self, integers, event):
        """
        Constructor.

        @param integers list of integers
        @param event event synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.event = event
    
    def run(self):
        """
        Thread run method. Append random integers to the integers list
        at random time.
        """
        for i in range(10):
            integer = random.randint(0, 256)
            self.integers.append(integer) 
            print '%d appended to list by %s' % (integer, self.name)
            print 'event set by %s' % self.name
            self.event.set()
            print 'event cleared by %s' % self.name
            self.event.clear()

class Consumer(threading.Thread):
    """
    Consumes random integers from a list
    """

    def __init__(self, integers, event):
        """
        Constructor.

        @param integers list of integers
        @param event event synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.event = event
    
    def run(self):
        """
        Thread run method. Consumes integers from list
        """
        while True:
            self.event.wait()
            integer = self.integers.pop()
            print '%d popped from list by %s' % (integer, self.name)

def main():
    integers = []
    event = threading.Event()
    t1 = Producer(integers, event)
    t2 = Consumer(integers, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
 
