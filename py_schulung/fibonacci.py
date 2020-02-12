import time
from math import inf

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        return res, time.time() - start
    return wrapper

def memoize(func):
    dict = {}
    def wrapper(x):
        if x not in dict:
            dict[x] = func(x)
        return dict[x]
    return wrapper

def fib_rec(n):
    return n if n in [0,1] else fib_rec(n - 1) + fib_rec(n - 2)

@memoize
def fib_rec_mem(n):
    return n if n in [0,1] else fib_rec_mem(n - 1) + fib_rec_mem(n - 2)

def fib(n):
    if n == 0:
        return 0
    old, new = 0, 1
    for _ in range(n-1):
        old, new = new, old + new
    return new

if __name__ == "__main__":

    fib_rec= timeit(fib_rec)
    fib_rec_mem = timeit(fib_rec_mem)
    fib = timeit(fib)

    for i in range(0, 100000):
        _, t1 = fib_rec(i) if i < 30 else (None, float(inf))
        _, t2 = fib_rec_mem(i)
        _, t3 = fib(i)
        print("n = {}, recursive time: {:.6f}, recursive time (memoized): {:.6f}, loop time: {:.6f}".format(i, t1, t2, t3))
