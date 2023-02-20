def factorial(n):
    if n == 1 or n == 0:
        print(n)
        return 1
    print(n)
    return n * factorial(n - 1)


print(factorial(995))
