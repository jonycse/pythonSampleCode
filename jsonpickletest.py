import jsonpickle


class Subclass(object):
    subclass_value=10
    def my_fun(self):
        print "this is myfun from Subclass"

class MainClass(object):
    mainclass_data='This is main class data'
    mainclass_value=5
    sc=Subclass()


obj=MainClass()
pickle=jsonpickle.encode(obj,max_depth=1)
unpickleObject=jsonpickle.decode(pickle)

unpickleObject.sc.my_fun()
print unpickleObject.mainclass_data