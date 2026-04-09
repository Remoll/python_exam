class Class1:
    def __init__(self):
        self.public_attr = "it's public"
        self.__private_attr = "it's private"
    
    @property # getter
    def private_attr(self):
        return self.__private_attr
    
    @private_attr.setter
    def private_attr(self, new_value):
        print("you're changing private attr")
        self.__private_attr = new_value

    @private_attr.deleter
    def private_attr(self):
        print("you trying to delete private value - will be reset instead")
        self.__private_attr = "it's private"
    
instance1 = Class1()
# print(instance1.__private_attr) # 'Class1' object has no attribute '__private_attr'. Did you mean: 'private_attr'?
print(instance1.private_attr)
instance1.private_attr = "changed value"
print(instance1.private_attr)
del instance1.private_attr
print(instance1.private_attr)

print('===============================')

print(instance1.public_attr)
instance1.public_attr = "changed value"
print(instance1.public_attr)
del instance1.public_attr
try:
    print(instance1.public_attr)
except:
    print('you cannot print deleted attr')

print('===============================')
print('===============================')

class Class2(Class1):
    pass

instance2 = Class2()
# print(instance2.__private_attr) # 'Class2' object has no attribute '__private_attr'. Did you mean: 'private_attr'?
print(instance2.private_attr)
instance2.private_attr = "changed value"
print(instance2.private_attr)
del instance2.private_attr
print(instance2.private_attr)

print('===============================')

print(instance2.public_attr)
instance2.public_attr = "changed value"
print(instance2.public_attr)
del instance2.public_attr
try:
    print(instance2.public_attr)
except:
    print('you cannot print deleted attr')