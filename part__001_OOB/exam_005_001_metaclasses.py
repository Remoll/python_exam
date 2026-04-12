# class object >>is instance of>> class >>is instanceof>> metaclass

# type is a class that generates classes defined by a programmer;
# metaclasses are subclasses of the type class.

# you can use type() function with 3 args tp create class

class SuperClass01():
    def method01(self):
        print('method01 called')

new_class = type('MyClass', (SuperClass01, ), { 'attribute01': 'value' })

instance01 = new_class()

print(instance01)
print(type(instance01))
print(type(new_class))
print(instance01.method01)
print(instance01.attribute01)

# arguments:
# 1: class name (__name__)
# 2: tuple of the base classes from which the newly created class is inherited (__bases__)
# 3: dictionary containing method definitions and variables for the class body (__dict__)

# ================================================

# implement our own metaclass

class MyMetaclass(type): # must derived from type
    def __new__(mcs, name, bases, dictionary): # 'mcs' refers to the class – it’s just a convention
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.custom_attribute = 'my custom attribute'
        return obj

class My_Object(metaclass=MyMetaclass):
    pass

print(My_Object.__dict__)

# ===================================================

def greetings(self):
    print('Just a greeting function, but it could be something more serious like a check sum')

class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        if 'greetings' not in dictionary:
            dictionary['greetings'] = greetings
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj

class My_Class1(metaclass=My_Meta):
    pass

class My_Class2(metaclass=My_Meta):
    def greetings(self):
        print('We are ready to greet you!')

myobj1 = My_Class1()
myobj1.greetings()
myobj2 = My_Class2()
myobj2.greetings()

