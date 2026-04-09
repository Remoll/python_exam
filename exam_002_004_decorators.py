def simple_decorator(function):
    print('decorator works')
    return function

@simple_decorator
def simple_function():
    print("simple function")

simple_function()

# ==============================================

def decorator_for_function_with_args(own_function):
    print("decorator_for_function_with_args works")
    def internal_wrapper(*args, **kwargs):
        own_function(*args, **kwargs)
        print('Decorator is still operating')

    return internal_wrapper


@decorator_for_function_with_args
def combiner(*args, **kwargs):
    print("simple function with args: ", args, kwargs)

combiner('a', 'b', exec='yes')

# =============================================

def decorator_with_args_for_function_with_args(dec_arg):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print("decorator_with_args_for_function_with_args works, with arg: ", dec_arg)
            our_function(*args)
        return internal_wrapper
    return wrapper

@decorator_with_args_for_function_with_args('arg_1')
def pack_books(*args):
    print("We'll pack books:", args)

@decorator_with_args_for_function_with_args('arg_2')
def pack_toys(*args):
    print("We'll pack toys:", args)

@decorator_with_args_for_function_with_args('arg_3')
def pack_fruits(*args):
    print("We'll pack fruits:", args)

pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')

# ===================================================

def first_decorator(func):
    print("first_decorator works: ", func)
    return func

def second_decorator(func):
    print("secons_decorator works: ", func)
    return func

@first_decorator
@second_decorator
def simple_func():
    print("simple_function works")

simple_func()

# ===================================================

# STACKED DECORATORS

# the call sequence will look like the following:

# 1. the outer_decorator is called to call the inner_decorator, then the inner_decorator calls your function;
# 2. when your function ends it execution, the inner_decorator takes over control, and after it finishes its execution, the outer_decorator is able to finish its job.

# @outer_decorator
# @inner_decorator
# def function():
#     pass

# abcd = subject_matter_function()

# is equal

# subject_matter_function = outer_decorator(inner_decorator(subject_matter_function())))
# abcd = subject_matter_function()

# ===================================================

# CLASS DECORATORS

class SimpleDecorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print("class decorator is working")
        self.func(*args, **kwargs)
        print("class decorator still working")

@SimpleDecorator
def print_somthing(a, *args, **kwargs):
    print(a, args, kwargs)

print_somthing("A", "S", 0, thing = 'thing')

# ===================================================

class DecoratorsWithArgs:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    
    def __call__(self, func):
        def wraper(*args, **kwargs):
            print('DecoratorsWithArgs is working', self.args, self.kwargs)
            func(*args, **kwargs)
            print('DecoratorsWithArgs is still working')
        return wraper

@DecoratorsWithArgs([1,2,3], "a", 0, 'b', name = 'jan')
def print_somthing(a, *args, **kwargs):
    print(a, args, kwargs)

print_somthing("A", "S", 0, thing = 'thing')

# ====================================================

def decorator_for_class(class_):
    class_.__getattr__orig = class_.__getattribute__

    def new_getattr(self, name):
        if name == 'some_attribute':
            print('some_attribute was called')
        return class_.__getattr__orig(self, name)

    class_.__getattribute__ = new_getattr
    return class_

@decorator_for_class
class SimpleClass:
    def __init__(self, some_attribute, other_attribute):
        self.some_attribute = some_attribute
        self.other_attribute = other_attribute
    
SimpleClass(1, 2).some_attribute
SimpleClass(3, 4).other_attribute
SimpleClass(5, 6).some_attribute
