# https://www.w3schools.com/python/python_functions.asp

# Arbitrary Arguments, *args
#
def processReiheFunctions(start, fun, iterations):
    last = start
    for i in range(iterations):
        last = fun(last, i)
        print(last)


def fun1(last, n):
    return 0 if n == 0 else 1 / n


processReiheFunctions(0, fun1, 10)

print("* * * *")


def fun2(last, n):
    return last + (0 if n == 0 else 1 / n)


processReiheFunctions(0, fun2, 10)

print("* * * *")


def chaosFun(n, i):
    # chaosConst = 2 : single value
    # chaosConst = 3.2 : two values
    # chaosConst = 3.5 : four values
    # chaosConst = 3.7 : chaos..
    chaosConst = 2
    return chaosConst * n * (1 - n)


processReiheFunctions(0.7, chaosFun, 2)

print("* * * *")
