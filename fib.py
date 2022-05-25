def fib(n):
    assert n >= 0, 'n must be positive int'
    if n == 0|1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)    


# print(fib(8))
    

def fact(n):
    assert n > 0 and type(n) == int, 'please pass int greater than 0'
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

