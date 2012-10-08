class MyDecorator(object):
    def __init__(self, f):
        self.doSomethingCopy=f
        print "This line will call on decoration"

    def __call__(self,p,q):
        print "This line will work when we call the function 'doSomething' "
        self.doSomethingCopy(p+1,q+1)

@MyDecorator
def doSomething(a,b):
    print "I am doing something"
    print "A ",a," B ",b


doSomething(3,4)