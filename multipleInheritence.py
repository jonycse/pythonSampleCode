'''
Python support multiple inheritance. For multiple inheritance we need to know MRO(Method Resolution Order)
'''
class Arithmetic(object):
    def add_num(self,a,b):
        print a+b

class String(object):
    def add_num(self,a,b):
        print a-b

    def print_string_upper(self,data):
        print data.upper()

class Common(Arithmetic,String):
    def print_class_c(self):
        print "This is C"



print Common.mro()

mih=Common()
mih.add_num(2,3)
mih.print_string_upper("bangladesh")
mih.print_class_c()





O = object
class F(O): pass
class E(O): pass
class D(O): pass
class C(D,F): pass
class B(E,D): pass
class A(B,C): pass

print A.mro()
print C.mro()



