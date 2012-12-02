
from collections import deque

myDequeue = deque()

myDequeue.append(5) # insert element at back
myDequeue.appendleft(9) # insert element at front
myDequeue.append(55)
myDequeue.appendleft(99)
print myDequeue

print myDequeue.pop() # remove last element
print myDequeue
print myDequeue.popleft() # remove first element
print myDequeue
print myDequeue[-1] # last element
print myDequeue[0] # fist element

