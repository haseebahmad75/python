# Basic decorator
def decorator(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished...")
    return wrapper
    
@decorator
def greet():
    print("Hello")

greet()

# apply decoration on functions with arguments
def decorator(func):
    def wrapper(name):
        func(name)
        print(f"{name} lives in Islamabad")
    return wrapper

@decorator
def this_func(name):
    print(f"My name is {name}")

this_func("Haseeb")

# Decorator with arguments
def decorator(n):
    def decorator(func):
        def wrapper(name):
            print(func(name))
            if n==1:
                return f"Message conveyed to {name}"
            else:
                return "Message not conveyed"
        return wrapper
    return decorator

@decorator(1)
def msg(name):
    return f"Convey my message to {name}"

print(msg("Hamza"))

# when we wrap a function in a decorator, it's original metadata is lost. To prevent this, we use wraps function from functools module
# to copy the attributes of the original function into the wrapper function

import functools
def decorator(func):
    @functools.wraps(func)
    def inner_func():
        print("Start")
        func()
        print("Finish")
    return inner_func
@decorator
def greet():
    print("Hello")
greet()
print(greet.__name__)

# Write a decorator called log_call that:

# Accepts any number of positional and keyword arguments.
# Prints "Function called" before the function executes.
# Calls the original function with all its arguments.
# Prints "Function finished" after it executes.
# Returns whatever the original function returns.

def log_call(func):
    def inner(*args, **kwargs):
        print("Function called")
        res = func(*args, **kwargs)
        print("Function finished")
        return res
    return inner

@log_call
def intro(name,age,city):
    return f"{name},{age},{city}"

print(intro("Faiq", 20, city="Lahore"))

@log_call
def add(a,b):
    return a+b
print(add(5,5))

# Create a decorator called require_role(role).
# Requirements
# The decorator should take one argument: role.
# The decorated function should always receive a keyword argument named user_role.
# If user_role matches role, execute the function.
# Otherwise, print "Access Denied" and do not execute the function.
# Return the original function's return value if access is granted.

def require_role(role):
    def require_role(func):
        def wrapper(username, **kwargs):
            if role == kwargs["user_role"]:
                print("Function executed")
                return func(username, **kwargs)
            else:
                print("Access denied")
        return wrapper
    return require_role

@require_role("admin")
def delete_user(username, user_role=None):
    print(f"{username} deleted.")

delete_user("Ali", user_role="admin")