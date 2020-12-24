# https://www.w3schools.com/python/python_functions.asp

# Arbitrary Arguments, *args
#
def my_function_21(*args):
    for i in args:
        print(i)


my_function_21(1,2,"43")

print("* * * *")

# Keyword Arguments
# You can also send arguments with the key = value syntax.

def my_function_22(child3, child2, child1):
  print("The youngest child is " + child3)

my_function_22(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print("* * * *")

# Passing a List as an Argument

def my_function_23(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function_23(fruits)

print("* * * *")


# Recursion

def fakultaet(n):
    if n == 1:
        return 1
    else:
        return n * fakultaet(n-1)

print('fakultaet von 5:', fakultaet(5))
