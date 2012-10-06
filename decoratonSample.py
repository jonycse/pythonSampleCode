from pprint import pprint

def mydeco(*kwargs):
    return True


def accept(f):
    def sub(*args):
        s=0
        for n in args:
            s+=n
        return s
    return sub


@accept
def add(a,b):
    return a+b


print add(2,3)
print add(2,5,3,10)