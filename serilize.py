import pickle

class Student(object):
    marks=None
    def __init__(self,n='name'):
        self.name=n
    def setMark(self,m=0):
        self.marks=m
    def getMark(self):
        return self.marks
    def getName(self):
        return self.name


sa=Student("AJZ")
sa.setMark(10)
pickleData=pickle.dumps(sa)

sb=pickle.loads(pickleData)
print sb.getName()



