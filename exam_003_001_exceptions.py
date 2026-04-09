try:
    import abcdefghijk

except ImportError as e:
    print(e)
    print(e.args)
    print(e.name)
    print(e.path)

print('=======================')

try:
    print(int('a'))
except ValueError as e_variable:
    print(e_variable)
    print(e_variable.args)

print('=======================')

try:
    b'\x80'.decode("utf-8")
except UnicodeError as e:
    print(e)
    print(e.encoding)
    print(e.reason)
    print(e.object)
    print(e.start)
    print(e.end)

# ======================================
# Chained exceptions
# the __context__ attribute, which is inherent for implicitly chained exceptions;
# the __cause__ attribute, which is inherent for explicitly chained exceptions.

a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    try:
        # the following line is a developer mistake - they wanted to print progress as 1/10	but wrote 1/0
        print(1 / 0)
    except ZeroDivisionError as f:
        print('Inner exception (f):', f)
        print('Outer exception (e):', e)
        print('Outer exception referenced:', f.__context__)
        print('Is it the same object:', f.__context__ is e)

print('=======================')

class RocketNotReadyError(Exception):
    pass

def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e

def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100 / 0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e

crew = ['John', 'Mary', 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))

print('=======================')
# ===============================================

import traceback

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


crew = ['John', 'Mary', 'Mike']

print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print(f.__traceback__)
    print(type(f.__traceback__))
    print('\nTraceback details')
    details = traceback.format_tb(f.__traceback__)
    print("\n".join(details))

print('Final check is over')