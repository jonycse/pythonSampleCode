class MyClass():

    @staticmethod
    def myStaticFunction():
        print "I am static method"

    @classmethod
    def myClassFunction(cls):
        print "I am class method"
        print cls

    def anyFunction(self):
        print "I am any function"

MyClass.myStaticFunction()
MyClass.myClassFunction()
MyClass.anyFunction()