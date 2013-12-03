class CarState:
    def current_speed(self):    pass

class CityMode(CarState):
    def current_speed(self):
        print "Max sped 60 mile per hour, City mode"

class HighwayMode(CarState):
    def current_speed(self):
        print "Max speed 150 mile per hour, Highway mode"
