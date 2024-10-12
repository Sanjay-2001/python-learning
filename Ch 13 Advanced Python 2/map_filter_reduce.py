from functools import reduce

l = [1, 2, 3, 4, 5]


def square(x): return x*x


sqList = map(square, l)
print(list(sqList))


def even(n):
    if (n % 2 == 0):
        return True
    return False


onlyEven = filter(even, l)
print(list(onlyEven))


def sum(a, b):
    return a+b


print(reduce(sum, l))
