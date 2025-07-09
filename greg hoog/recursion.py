print('=====fibonancci================')

def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibo(n-1) + fibo(n-2)

# for n in range(1,50):
#     print(n, ':', fibo(n))

print('==========implement memoization =====')
fib_cache= {}
def fun(n):
    # if we have cached the value, then return it
    if n in fib_cache:
        return fib_cache[n]

    if n == 1:
        value = 1

    elif n == 2:
        value = 1
    elif n > 2:
        value = fun(n-1) + fun(n-2)

#     cache the value and return it
    fib_cache[n] = value
    return value

# for i in range(1,50):
#     print(i, ':', fun(i))

print('using buitin func')

from functools import lru_cache

@lru_cache
def fib(n):
    if type(n) != int:
        raise TypeError('n must be a +ve int')
    if n < 1:
        raise TypeError('n must be a +ve int')
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fib(n-1) + fib(n-2)
    return None


for i in range(1,100):
    print(i, ":", fib(i))












