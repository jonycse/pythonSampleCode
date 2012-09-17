class Shop(object):
    def __init__(self, item_factory = None):
        self.item_factory=item_factory

    def get_item_description(self):
        item=self.item_factory.get_item()
        print "Item model ",self.item_factory.model()
        print "Item name ",item.name()
        print "Item color ",self.item_factory.color()



class Shoes(object):
    def name(self):
        return "Shoes"
    def __str__(self):
        return "Shoes"

class Mobile(object):
    def name(self):
        return "Nokia"
    def __str__(self):
        return "Nokia"

class ShoesFactory(object):
    def get_item(self):
        return Shoes()
    def model(self):
        return "MEN101"
    def color(self):
        return "Black"

class MobileFactory(object):
    def get_item(self):
        return Mobile()
    def model(self):
        return "NOK404"
    def color(self):
        return "Black deep"

shopShoes=Shop(ShoesFactory())
shopShoes.get_item_description()
print "*"*30
shopMobile=Shop(MobileFactory())
shopMobile.get_item_description()