from collections import deque

dq = deque([1,2,3])
print dq

dq.append(4) # add end of the deque
dq.appendleft(5) # add beginning of the deque

print dq

print dq.pop()
print dq.popleft()
print dq

dq.extend([22,33,44]) # add multiple element to end of existing deque
dq.extendleft([444,333]) # add multiple element to beginning of existing deque
print dq

print 22 in dq # search in deque

dq.rotate(1)
print "Right rotate:",dq
dq.rotate(-1)
print "Left rotate:",dq

