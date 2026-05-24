# Type hinting
def my_func(arg1: str) -> str:
    return arg1

# Docstrings
# descriptions and explanations for all public modules, files, functions, classes, and methods

# In the case of packages, these should be documented too, and you can write package docstrings in the module docstring of the __init__.py

# docstrings are accesible by __doc__ or help(my_func_02) which is more descriptive

def my_func_02(arg: str):
    # """My docstring."""

    """Multiline docstring

    some desc:\n
    :args: str > some string lalala

    test
    """
    
    r"""raw string docstring \n"""
    
    u"""Unicode string, usefull in python 2, in python 3 strings are unicode by default"""
    
    return arg

# linter - find issues - Pycodestyle
# fixer - fix issues - Black