# Decorators add a certain functionally to a method
# they wrap the function/method


# A decorator is function in a function
def mydecorator(function):
    def wrapper(*args, **kwargs):
        print("I am decorating your function!")
        function(*args, **kwargs)
        print("I decorate your function now!")

    return wrapper


def helloworld():
    print("Hello world!")


mydecorator(helloworld)()


@mydecorator
def method_x(s):
    print(f"This is how to use decorators: {s}")


method_x("Mike")


# Practical example 1

def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value

    return wrapper


@logged
def add(x, y):
    return x + y


print(add(10, 20))


# Practical example 2
import time


def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__

        print(f"{fname} took {after-before} seconds to execute")
        return value

    return wrapper


@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result


myfunction(10)
myfunction(90000)
