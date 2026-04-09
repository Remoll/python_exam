# def print(self, *args, sep=' ', end='\n', file=None): # this is how print is declared

def combiner(a, b, *args, c=20, **kwargs):
    super_combiner(c, *args, **kwargs) # are used to denote that args and kwargs when pass them father

def super_combiner(my_c, *my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_c:', my_c)
    print('my_kwargs', my_kwargs)

combiner(1, '1', 1, 1, c=2, argument1=1, argument2='1')


print(("a", "b", "c"))
print(*("a", "b", "c")) # asterisks * are used to denote that args and kwargs
