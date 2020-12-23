# https://www.w3schools.com/python/python_functions.asp

# define a function
def my_function():
    print("Hello from a function")


# use a function
my_function()


# The terms parameter and argument can be used for the same thing:
# information that are passed into a function.

def my_function(fname, lname):
    return print(fname + " " + lname)


print(my_function("Emil", "Refsnes"))

def add(a,b):
    return a + b


print(add(12,54))
