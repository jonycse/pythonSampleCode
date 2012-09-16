class MyClass():

    def myPublicFunction(self):
        print "I am public function"

    def __myPrivateFunction(self):
        print "I am private function"


myClass= MyClass()
myClass.myPublicFunction()
#myClass.__myPrivateFunction # This is will not work, __myPrivateFunction is a private method