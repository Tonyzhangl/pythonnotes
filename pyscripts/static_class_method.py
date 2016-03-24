#coding=utf-8

class Fruit(object):
    total = 0

    def __init__(self, area="", category="", batch=""):
        self.area = area
        self.category = category
        self.batch = batch

    @staticmethod
    def init_product_staticmethod(product_info):
        area, category, batch = map(int, product_info.split('-'))
        fruit = Fruit(area, category, batch)
        return fruit

    @classmethod
    def init_product_classmethod(cls, product_info):  #类似于工厂方法，构建出一个类的实例。
        area, category, batch = map(int, product_info.split('-'))
        fruit = cls(area, category, batch)
        return fruit


class Apple(Fruit):
    pass

class Orange(Fruit):
    pass


app1 = Apple(1-2-3)
print 'app1 is instance of Apple:'+str(isinstance(app1, Apple))
org1 = Orange.init_product_staticmethod("1-2-3")
print 'org1 is instance of Orange:'+str(isinstance(org1, Orange))
org2 = Orange.init_product_classmethod("1-2-3")
print 'org2 is instance of Orange:'+str(isinstance(org2, Orange))
