from collections import OrderedDict
d = OrderedDict()

d[3]=5
d[1]=6
d[20]=9
d["cse"]=77

print d

del d[1]
d[1] = 123

print d
print d[1]
print d["cse"]