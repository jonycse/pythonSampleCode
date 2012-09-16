class Singleton:
    __single = None
    def __init__( self ):
        if Singleton.__single:
            raise Singleton.__single
        Singleton.__single = self



class Child( Singleton ):
    def __init__( self, name ):
        Singleton.__init__( self )
        self.__name = name
    def name( self ):
        return self.__name


cha=Child("Child name is gee")
print(cha.name())

chb=Child("Child name is geeNEW")
print(chb.name())