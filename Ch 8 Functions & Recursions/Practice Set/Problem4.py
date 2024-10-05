
def starPattern(n):
    for i in range(1, n+1):
        print("*"*n, end="")
        print("")
        n -= 1


starPattern(3)

print("--------")


def pattern(n):
    if (n == 0):
        return
    print("*"*n)
    pattern(n-1)


pattern(5)
