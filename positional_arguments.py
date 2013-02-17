def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print add(1)
print add(1,4,5)
print add(9,3)
print add(2.9,5,3,8)
