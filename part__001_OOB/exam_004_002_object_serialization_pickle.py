# object serialization = object structure into a stream of bytes
# deserialization

# The following types can be pickled:
# - None, booleans;
# - integers, floating-point numbers, complex numbers;
# - strings, bytes, bytearrays;
# - tuples, lists, sets, and dictionaries containing pickleable objects;
# - objects, including objects with references to other objects (remember to avoid cycles!)
# - references to functions and classes, but not their definitions.

import pickle

a_dict = dict()
a_dict['EUR'] = {'code':'Euro', 'symbol': '€'}
a_dict['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
a_dict['USD'] = {'code':'US dollar', 'symbol': '$'}
a_dict['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}

a_list = ['a', 123, [10, 100, 1000]]

# write and load using files

with open('multidata.pckl', 'wb') as file_out: 
    pickle.dump(a_dict, file_out)
    pickle.dump(a_list, file_out)

with open('multidata.pckl', 'rb') as file_in: # you need to remember objects order
    data1 = pickle.load(file_in)
    data2 = pickle.load(file_in)

print(type(data1))
print(data1)
print(type(data2))
print(data2)

# =============================================

# writes and load using variable - you can send in via network or to database

a_list = ['a', 123, [10, 100, 1000]]
bytes = pickle.dumps(a_list)
print('Intermediate object type, used to preserve data:', type(bytes))

# now pass 'bytes' to appropriate driver

# therefore when you receive a bytes object from an appropriate driver you can deserialize it
b_list = pickle.loads(bytes)
print('A type of deserialized object:', type(b_list))
print('Contents:', b_list)

# Pickle can fail if an object cannot be pickled or if the data structure is too deeply recursive.
# Functions and classes are saved by name, not by their code or data.
# When you load the pickle file, the same function or class must be available in the environment, or an AttributeError can happen
# if you try ro unpickel function or class, but in your namespace there is nodefinitions for it you got AttributeError
# code should already know the function/class definition