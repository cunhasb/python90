"""
Decorators are HOC - High Order Functions receive a function,execute it without any alterations and return the function.
"""


def decorator_function(original_function):
    def wrapper_function():
        original_function()
    return wrapper_function


def display():
    print('display function ran')


decorated_display = decorator_function(display)

decorated_display()
