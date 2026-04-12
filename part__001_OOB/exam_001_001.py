class Class1:
    class_var = 'shared variable'

    def __init__(self):
        self.a = "a"
        Class1.class_var = "changed shared variable" # you have to use Class1 to change class variable
    
    def method1(self):
        pass

inst1 = Class1()

# Print types

print(Class1.__class__) # <class 'type'>
print(inst1.__class__) # <class '__main__.Class1'>
print(inst1.a.__class__) # <class 'str'>
print(inst1.method1.__class__) # <class 'method'>

# =================================================

inst1.other_attr = "other" # you can add attributes to an instance outside  of class definition

print(inst1.__dict__) # instance attributes {'a': 'a', 'other_attr': 'other'}

print(Class1.__dict__) # class attributes {'__module__': '__main__', '__firstlineno__': 1, 'class_var': 'changed shared variable', '__init__': <function Class1.__init__ at 0x7d0255e3b420>, 'method1': <function Class1.method1 at 0x7d0255e3b4c0>, '__static_attributes__': ('a',), '__dict__': <attribute '__dict__' of 'Class1' objects>, '__weakref__': <attribute '__weakref__' of 'Class1' objects>, '__doc__': None}

inst2 = Class1()
inst2.class_var = "changed value" # this will create an instance variable, not change the class variable

# =================================================

class SuperClass1:
    counter = 0

    def __init__(self):
        SuperClass1.counter += 1

class SubClass1(SuperClass1):
    def __init__(self):
        super().__init__()

class SubClass2(SuperClass1):
    def __init__(self):
        super().__init__()

super_class1 = SuperClass1()
sub_class1 = SubClass1()
sub_class2 = SubClass2()

print(SuperClass1.counter) # 3, because we have created 3 instances of SuperClass1 (including subclasses)
print(SubClass1.counter) # 3
print(SubClass2.counter) # 3

# =================================================

len("") # get a number of elements of a tuple, list, dictionary, or characters in a string

# __ = dunder = double underscore, used for special methods in Python (e.g., __init__, __str__, __len__, etc.)

print(20 + 10 == (20).__add__(10))
print("Hello " + "World" == "Hello ".__add__("World"))

class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    def __add__(self, other): # special purpose method, define how to add instances of class, does't work without it
        return self.weight + other.weight


p1 = Person(30, 40, 50)
p2 = Person(35, 45, 55)

print(p1 + p2)

print(dir(p1)) # returns a list of the attributes and methods of the object - works with strings, lists, dictionaries, etc.
print(help(p1)) # used to display the documentation (if delivered!) of modules, functions, classes, and keywords - works with strings, lists, dictionaries, etc.

# for more magic methods check magic_methods_XX.png files