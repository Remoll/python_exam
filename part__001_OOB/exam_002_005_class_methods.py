# a class method requires 'cls' as the first parameter and a static method does not;
# a class method has the ability to access the state or methods of the class, and a static method does not;
# a class method is decorated by '@classmethod' and a static method by '@staticmethod';
# a class method can be used as an alternative way to create objects, and a static method is only a utility method. 

# Class method
# can by used as alternative constructor

class Class1:
    instances_counter = 0

    def __init__(self):
        Class1.instances_counter += 1
    
    @classmethod
    def get_instance_counter(cls):
        return cls.instances_counter
        # return Class1.instances_counter
        # Of course, you can use the reference to Class1.instances_counter,
        # but this will be inconsistent with the convention
        # and the code loses its effectiveness in communicating its own meaning.
    
print(Class1.get_instance_counter())
Class1()
print(Class1.get_instance_counter())
Class1()
print(Class1.get_instance_counter())
print(Class1.get_instance_counter())

# Static methods
# Static methods do not have the ability to modify the state of objects or classes,
# because they lack the parameters that would allow this.

class KowalskiFamily:
    def __init__(self, person):
        self.name = person['name']
        self.surname = person['surname']
    
    @staticmethod
    def is_surname_valid(surname):
        return surname == "Kowalski"
    
people = [{'name': 'Jan', 'surname': 'Nowak'}, {'name': 'Adam', 'surname': 'Kowalski'}, {'name': 'Jowisia', 'surname': 'Kowalski'}]

instances = []

for person in people:
    if (KowalskiFamily.is_surname_valid(person["surname"])):
        instances.append(KowalskiFamily(person))

for i in instances:
    print('{} {}'.format(i.name, i.surname))