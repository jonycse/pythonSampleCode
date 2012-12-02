#DA_Queue.py

from collections import deque
class MyQueue:
    queue = deque()

    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if len(self.queue):
            return self.queue.popleft()
        print "Impossible"


myQueue = MyQueue()
myQueue.enqueue(8)
myQueue.enqueue(4)
print myQueue.queue
myQueue.dequeue()
myQueue.dequeue()
print myQueue.queue
myQueue.dequeue()
print myQueue.queue

