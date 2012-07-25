import time
import threading
import random
import Queue

class Producer(threading.Thread):
    """
    Produces random integers to a list
    """

    def __init__(self, queue):
        """
        Constructor.

        @param integers list of integers
        @param queue queue synchronization object
        """
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        """
        Thread run method. Append random integers to the integers
        list at random time.
        """
        while True:
            integer = random.randint(0, 256)
            self.queue.put(integer) 
            print '%d put to queue by %s' % (integer, self.name)
            time.sleep(1)

class Consumer(threading.Thread):
    """
    Consumes random integers from a list
    """

    def __init__(self, queue):
        """
        Constructor.

        @param integers list of integers
        @param queue queue synchronization object
        """
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        """
        Thread run method. Consumes integers from list
        """
        while True:
            integer = self.queue.get()
            print '%d popped from list by %s' % (integer, self.name)
            self.queue.task_done()

def main():
    integers = []
    queue = Queue.Queue()
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
 
