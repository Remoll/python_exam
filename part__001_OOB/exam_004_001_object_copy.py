import copy

string1 = "value" # string1 is LABEL for a object
string2 = string1
print(id(string1)) # returns the 'identity' of an object
print(id(string2)) # the same id

# ================================================

list0 = ["test"]
print(list0 == ["test"]) # True
print(list0 is ["test"]) # False

# list shallow copy
list1 = [["a"]]
list2 = list1[:]
list2 = list(list1)
list2 = copy.copy(list1)

# dict shallow copy
dict1 = {'a': 'a', 'b': 'b'}
dict2 = dict(dict1)

# deep copy
list3 = [["c"]]
list4 = copy.deepcopy(list2)
dict3 = {'a': 'a', 'b': 'b'}
dict4 = copy.deepcopy(dict3)

# =====================================

class Example:
    def __init__(self):
        self.properties = ["112", "997"]
        print("Hello from __init__()")

a_example = Example()
# __init__ is not executed for the b_example object as the deepcopy function copies an already initialized object
b_example = copy.deepcopy(a_example)
