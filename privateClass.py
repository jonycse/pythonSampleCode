
class MyClass():

    def myPublicFunction(self):
        print "I am public function"

    def __myPrivateFunction(self):
        print "I am private function"


class _MyPrivateClass():

    def myPrivateFunction(self):
        print "I am private function of class _MyPrivateClass"