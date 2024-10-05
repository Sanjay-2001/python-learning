def sumOfN(num):
    if (num == 1):
        return num

    return num+sumOfN(num-1)


print(sumOfN(5))
