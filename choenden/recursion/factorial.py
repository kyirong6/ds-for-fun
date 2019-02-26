def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


if '__main__' == __name__:
    for i in range(8):
        print(factorial(i))    