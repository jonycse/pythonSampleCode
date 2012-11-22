class MakeMeal:

    def prepare(self):  pass
    def cook(self): pass
    def eat(self):  pass

    def go(self):
        self.prepare()
        self.cook()
        self.eat()

class MakePizza(MakeMeal):

    def prepare(self):
        print "Prepare Pizza"

    def cook(self):
        print "Cook Pizza"

    def eat(self):
        print "Eat Pizza"

class MakeTea(MakeMeal):

    def prepare(self):
        print "Prepare Tea"

    def cook(self):
        print "Cook Tea"

    def eat(self):
        print "Eat Tea"

makePizza = MakePizza()
makePizza.go()

print 25*"+"

makeTea = MakeTea()
makeTea.go()