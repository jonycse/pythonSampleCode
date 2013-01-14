class MyClass():
    def __init__(self):
        self.__name = "" # define private variable
        self.__id = 0

    def setName(self, name):
        self.__name = name
    def setId(self, id):
        self.__id = id
    def getName(self):
        return self.__name
    def getId(self):
        return self.__id



a = MyClass()
a.setName("TEst name")
a.setId(1)


print "name ", a.getName()
print "Id ", a.getId()


#print a.__name__author__ = 'user'
