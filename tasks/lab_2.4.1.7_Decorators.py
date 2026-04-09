from datetime import datetime

def print_timestamp(func):
    timestamp = datetime.now()
    string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    print(string_timestamp)
    def wraper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        print("decorator still works")
        if (func_result != None):
            return func_result
    return wraper

@print_timestamp
def print_name(name):
    print(name)

print_name("Adam")

@print_timestamp
def print_names(*args, **kwargs):
    print(args, kwargs['name'])

print_names("Jan", "Karol", "Beata", name = "Edward", surname = "Kowalski")

@print_timestamp
def add_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add_numbers(1,3,4,5,6,67,7,2312))

print('========================')

def dec_with_args(*args, **kwargs):
    print(args, kwargs)
    def wraper(func):
        def inner_wraper(*args, **kwargs):
            func_result = func(*args, **kwargs)
            if (func_result != None):
                return func_result
        return inner_wraper
    print('dec_with_args still works')
    return wraper

@dec_with_args("1", 2, number = 3 )
def print_something(*args, **kwargs):
    print(args, kwargs)
    return args, kwargs

print(print_something("S", 0, thing = "THING"))