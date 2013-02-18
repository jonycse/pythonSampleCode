from collections import namedtuple

Point = namedtuple('Point', ['x' ,'y'])

p1=Point(1, 2)
p2=Point(6, 4)

print p1
print p2
print "p1[0]",p1[0],"p1[1]",p1[1]
print "p2.x",p2.x,"p2.y",p2.y