class Arithmetic(object):
    pass

def arithmetic_function_add(cls):
    def sampleFunction(self,a,b):
        return a+b
    sampleFunction.__name__ = "addNum"
    setattr(cls,sampleFunction.__name__,sampleFunction)

arithmetic_function_add(Arithmetic)

arithmetic=Arithmetic()
print arithmetic.addNum(5,6)
