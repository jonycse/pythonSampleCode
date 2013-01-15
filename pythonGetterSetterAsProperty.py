class MyClass(object):
    def __init__(self):
        self.__name = "" # define private variable
        self.__id = 0 # define private variable

    def setName(self, name):
        self.__name = name
    def setId(self, id):
        self.__id = id
    def getName(self):
        return self.__name
    def getId(self):
        return self.__id

    idGS = property(getId, setId) # declare getter setter property for id



a = MyClass()
a.setName("Python")
a.idGS=5

print "Name ", a.getName()
print "Id ", a.idGS

