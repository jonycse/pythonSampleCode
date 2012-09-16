class MyClass(object): pass

class SubClassA(MyClass): pass
class SubClassB(MyClass): pass
class SubClassC(MyClass): pass

print([cls.__name__ for cls in vars()['MyClass'].__subclasses__()])

