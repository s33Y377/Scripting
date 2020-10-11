from functools import partial


def add(a, b, c):
    return a + b + c


func = partial(add, b=2, c=1)
print(func(3))
print(func(4))
