# PEP 8 is still evolving as new, additional conventions are being identified and included in it, and at the same time some old conventions are being identified as obsolete and discouraged from being followed.
# Indentation: four spaces per indentation level, spaces rather than tabs
# Mixing tabs and spaces for indentation is not allowed - keep consistency with code
# TabError exception: “TabError: inconsistent use of tabs and spaces in indentation”.

# Continuation lines are allowed if using parentheses/brackets/braces:
my_list_one = [
    1, 2, 3,
    4, 5, 6,
    ]

a = my_function_name(a, b, c,
                       d, e, f)


my_list_one = [
    1, 2, 3,
    4, 5, 6,
    ]

a = my_function_name(a, b, c,
                       d, e, f)

# limit all lines to a maximum of 79 characters
# break before binary operators

# two blank lines to surround top-level function and class definitions
# a single blank line to surround method definitions inside a class
# blank lines in functions in order to indicate logical sections

# imports be on separate lines, Still, it’s correct to make a one-line import using the from … import … syntax:
from subprocess import Popen, PIPE
# If possible, use absolute imports, avoid using wildcard imports

# You should always put imports at the beginning of your script, between module comments/docstrings and module globals and constants, respecting the following order:

#     Standard library imports;
#     Related third-party imports;
#     Local application/library specific imports.

# Make sure you insert a blank line to separate each of the above groups of imports

# "" vs '' avoid using backslashes:
# - if your string contains single-quote characters, it’s recommended that you use double-quoted strings;
# - if your string contains double-quote characters, it’s recommended that you use single-quoted strings.
# In the case of triple-quoted strings, PEP 8 recommends that you always use double-quote characters to maintain consistency with the docstring convention detailed in PEP 257

# avoid using too much whitespace
# do not use excessive whitespace immediately inside parentheses/brackets/braces, or immediately before a comma/semicolon/colon

# not use excessive whitespace:
# - after a trailing comma followed by a closing parenthesis, or
# - immediately before an opening parenthesis that marks the beginning of the argument list of a function invocation, or
# - immediately before an opening parenthesis that marks the beginning of indexing/slicing.

# Don’t use more than one space before and after operators
# Surround binary operators with a single space on both sides.
# However, if in your code there are operators that have different priorities,
# you may wish to consider adding spacing around the low(est) priority operators only
# Don’t surround the = operator with spaces if it’s used to indicate a keyword argument/default value

# Comments
# Write comments that will not contradict the code or mislead the reader. They’re much worse than no comment at all.
# Update your comments when your program gets updated.
# Write comments as complete sentences (capitalize the first word if it’s not an identifier, and end your sentence with a full stop).
# When writing block comments with multi-sentence comments, use two spaces after each full stop ending a sentence, except after the final sentence.
# Write comments in English (unless you are 100% sure that the code will never be read by people who don’t speak your language.)
# Comments should consist of no more than 72 characters per line (but you know that already).

# Block comments - use them to explain sections of code rather than particular lines:
# - should refer to the code that follows them;
# - should be indented to the same level as the code they describe.
# When writing block comments, start each line with # followed by a single space,
# and separate paragraphs by a line that contains the # symbol only

# Inline comments - written on the same line as your statements, provide further explanation to a single line of code or a single statement:
# - separated by two (or more) spaces from the statement they address;
# - used sparingly.

# Python naming conventions are, unfortunately, not fully consistent throughout the Python library.
# However, it is recommended that new modules and packages be written in compliance
# with the PEP 8 naming recommendations (unless an existing library follows a different style,
# in which case internal consistency is the preferred solution).

# mysamplename – lowercase
# my_sample_name – lowercase with underscores (snake_case)
# MYSAMPLENAME – uppercase
# MY_SAMPLE_NAME – uppercase with underscores (SNAKE_CASE)
# MySampleName – CamelCase (also known as capitalized words, StudlyCaps, or CapWords)
# A short note: when you use acronyms, you should capitalize all the letters that make up the acronym, e.g., HTTPServerError
# mySampleName – mixed case, which actually differs from CamelCase only by having an initial lowercase character
# My_Sample_Name – capitalized words with underscores (considered ugly by PEP 8)
# _my_sample_name – a name that starts with a single leading underscore indicates a weak "internal use", e.g., the instruction from SAMPLE import * will not import objects whose names start with an underscore.
# my_sample_name_ -– a single trailing underscore is used by convention in order to avoid any conflicts with Python keywords, e.g., class_
# __my_sample_name – a name that starts with a double leading underscore is used for class attributes where it invokes name mangling, e.g., inside the class MySampleClass, __room will become _MySampleClass__room
# __my_sample_name__ – a name that starts and ends with a double underscore is used for "magic" objects and attributes that reside in user-controlled namespaces, e.g., __init__, __import__, or __file__. You shouldn't create such names, but only use them as documented.

# variable, function, method, module - snake_case
# class, exception (which is calss) - CamelCase
# constant - SNAKE_CASE
# package - lowercase
# Type variable - CamelCase

# make comparisons to the None object with the use of 'is' or 'is not'
# also for Boolean, but even better just 'if something' not 'if something is True'
# for readability purposes, use the 'is not' operator instead of 'not … is'
# Avoid using if x: to express if x is not None: when you want to check if a given variable or argument set to None by default has been assigned a different value.
# when you want to “catch" an exception, refer to specific exceptions rather than use the bare except:
try:
    import my_module
except ImportError:
    my_module = None
# when checking for prefixes or suffixes, use the ''.startswith() and ''.endswith() string methods, as they’re cleaner and less error prone. Generally, it’s better to use string methods over importing the string module:
# Bad:
if name[:4] == 'Adam':
    # do something

# Good:
if name.startswith('Adam'):
    # do something
