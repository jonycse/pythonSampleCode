'''
For implementing single tone we need to override the "__new__" method of class
'''

class SingletonObject(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonObject, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def set_name(self,name):
        self.__name=name # name is private
    def get_name(self):
        return self.__name

    def set_home(self,home):
        self.home=home # home is public


if __name__ == '__main__':
    ob1=SingletonObject()
    ob1.set_name("test name")
    ob2=SingletonObject()
    ob2.set_home("BD")

    print ob1.get_name()
    print ob2.get_name()

    print ob1.home
    print ob2.home
