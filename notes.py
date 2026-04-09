# comment

bool1 = True
bool2 = False
type(bool1)

str1 = "text1"
str2 = 'text2'
str3 = "text3" * 10
type(str1)
str1[0]
str1[1:3] # slice
str1[:3] # slice for 0
str1[3:] # slice to the end
str1[-1] # last char
str1[1:-1]
# str1[0] = "text3" throw error
"t" in str1
print('SmArTpHoNe'.lower())
print('SmArTpHoNe'.upper())
print("happy birthday".capitalize())
print("Bee".find("e"))
len(str1)

int1 = 1
int2 = 2 + 2
int3 = -1
type(int1)

# print("string" + 1) - string + int = error

float1 = 1.5
float2 = 4/2 # int / int = float
float3 = -2.6
type(float1)

input1 = input() # always strig
print(input1)

int("2") # convert string to integer
float(2) # convert integer to float
str(2.5) # convert float to string

# operation with integer and float gives float

5 < 9
5 <= 9
5 == 9
5 != 9

x = 1
x += 5

True and False
True or False

range(2,5)

for i in range(10):
    print('hello' + str(i))

iterable_list = [1, 2, 3]
for i in iterable_list:
    print(str(i))

for i in "string":
    print(i)

for i in range(3):
    if i == 2:
        break

for i in range(3):
    if i == 1:
        continue # break current loop iteration
    print(str(i))

counter = 5
while counter > 0:
    counter = counter - 1

while counter > 0:
    counter = counter - 1
    if counter == 4:
        break

while counter > 0:
    counter = counter - 1
    if counter == 2:
        continue # break current loop iteration
    print(counter)

if False:
    print('if')
elif False:
    print('elif')
else:
    print('else')

if True: print('if')

test = 1
list1 = ["item1", 1, 1.2, test] # list
print(list1)
list1[0]
list1[0] = "item2"
list1[1:2] # slice
list1[:2] # slice from 0
list1[2:] # slice to the end
list1[-1] # last item
list1[1:-1]
"item1" in list1
len(list1)
list1.append("next item")
list1.insert(2, "third item")
list1.pop(0) # remove item on index
sum([1, 2, 3])
max([1, 2, 3])
min([1, 2, 3])
sorted([2, 1, 3])
sorted(["a", "c", "b"])
sorted([1, 2, 3], reverse = True)

print("string", 1, 1.2)

def function1 (arg1='default1', arg2='default2'):
    print(arg1)
    return arg1, arg2

x, y = function1('arg1') # need to be defined first

function_variable = function1

function_variable('arg1')

def dynamic_args(fixed_arg, *args): # *args is recived as tuple
    for arg in args:
        print(arg)

def display_info(fixed_arg, *args, **kwargs): # **kwargs is a dictionary
    #kwargs.items() returns the key:value pairs
    for key, value in kwargs.items():
        print(key, ":", value)

display_info(name="Alice", age=30, city="New York")

# In Python, functions that operate with other functions — that is, take another function as an argument or return a function -  are called Higher-Order Functions. They are particularly useful for processing various functions and returning specific results

# Pure function = same return for the input, no side effects like print, no user input

lambda1 = lambda arg1, arg2: arg1 + arg2 # lambda is anonymous function and don't need name
lambda1("arg1", "arg2")
lambda2 = (lambda arg1, arg2: arg1 + arg2)(1,2) # add arguments on the fly
lambda2 == 1+2 # True

names = ["name1", "name2", "name3"]
def capitalize(name):
    return name.capitalize()
map1 = map(capitalize, names)
list_from_map = list(map1)

map_from_lambda = map(lambda name : name.capitalize(), names)

filtered_list = list(filter(lambda name : name == "name1", names))

# works for map also, for any iterable data types
filtered_dict = dict(filter(lambda item : item[1] < 90,{"item1": 1, "item2": 91, "item3": 45}))

# usage of lambda
def mult(n):
    return lambda a : a * n
doubler = mult(2)
tripler = mult(3)
print(doubler(5))
print(tripler(5))

# Inpure function

tuple1 = (1, "string", 1.2) # immutable compare to list
tuple1.count("string")
len(tuple1)
max(tuple1)
min(tuple1)
int_t, string_t, float_t = tuple1
int_t_2, *list_from_string_and_float = tuple1

set1 = {1, "string", 1.2} # unordered, can't have duplicates
set1.add("forth item")
set1.remove("forth item")
set1.clear() # remove all items
set2 = set1.union({1,3}) # returns merged sets without duplicates
set3 = set1.difference(set2) # returns a set containing elements that are only in the first set and not in the second

dictionary1 = {
    "key1": "value1",
    "key1": 1 # overrides duplicated key
}

dictionary1["key1"]
dictionary1["key1"] = "value2"
dictionary1.get("key1")
dictionary1.keys()
dictionary1.values()
dictionary1.items() # returns all the key:value pairs in a dictionary
dictionary1.update({"key1": "value3"}, {"new_key": "new value"})
dictionary1.pop("key1")
"key1" in dictionary1
"value1" in dictionary1.values()

for key in dictionary1:
    print(key)

for value in dictionary1.values():
    print(value)

nums = [x*2 for x in range(1,51)] # list comprehension - shortcut for loop and add items to list

users = ["Brandon", "Emma", "Brian", "Sophia", "Bella", "Ethan", "Ava", "Benjamin", "Mia", "Chloe"]

group = [x for x in users if x[0] == "B"]

prices = [250, 300, "240", 400]
try:
    total = sum(prices)
    print(total)
except TypeError:
    print("TypeError:")
except IndexError:
    print("IndexError:")
except NameError:
    print("NameError")
except SyntaxError:
    print("SyntaxError")
except ValueError:
    print("ValueError")
except:
    print("any error")
else:
    print("only on succes")
finally:
    print("always displayed")
print("Happy Shopping")

invalid_value = 5
if invalid_value < 6:
    raise ValueError("error body")
if invalid_value < 6:
    raise ValueError

# decorator
def uppercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

@uppercase
def greet():
    return "Welcome!"

# Using the decorated function
print(greet())

class Class1:
    def __init__(self, parameter1):
        self.parameter1 = parameter1
        self._protected_parameter = 1 # protected just by convenction
        self.__private_parameter = 2 # private, needs getter method
    
    def method1(self):
        print(self.parameter1)

    def _protected_method(self): # protected just by convenction
        print(1)

    def __private_method(self): # not accesible outside the class
        print(2)

    @classmethod
    def class_method1(cls, arg1):
        print(arg1)
    
    @staticmethod
    def static_method1(arg1):
        print(arg1)

instance1 = Class1("parameter1")

instance1.parameter1

instance1.method1()

instance1._Class1__private_parameter # name mangling - allow acces to private

Class1.class_method1("arg1")
instance1.class_method1("arg1") # also works with instances

Class1.static_method1("arg1")

class Subclass1(Class1):
    def __init__(self, parameter1, parameter2):
        super().__init__(parameter1)
        self.parameter2 = parameter2
    
    def method1(self):
        super().method1()
        print("additional bahavior") 