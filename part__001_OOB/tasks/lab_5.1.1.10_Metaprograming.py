import time

def get_instantiation_time(self):
    return self.instantiation_time

class LogginMetaclass(type):
    instantiation_time = []
    classesList = []
    def __new__(mcl, name, base, dictionary):
        obj = super().__new__(mcl, name, base, dictionary)
        mcl.instantiation_time.append(time.time())
        mcl.get_instantiation_time = get_instantiation_time
        mcl.classesList.append(mcl)
        return obj
    
class SomeClass(metaclass=LogginMetaclass):
    pass

class SomeClass2(metaclass=LogginMetaclass):
    pass

instance = SomeClass()

print(SomeClass.classesList)
print(SomeClass.get_instantiation_time())
