a=[1,2,3]
b=[4,5,6]

z=zip(a,b)
print z

ai,bi=zip(*z)
print ai
print bi

print "-"*25

a=[1,2]
b=[4,5,6]

z=zip(a,b)
print z

ai,bi=zip(*z)
print ai
print bi

print "."*25

a=[1,2,4]
b=[4,5]

z=zip(a,b)
print z

ai,bi=zip(*z)
print ai
print bi