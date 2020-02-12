def check_range(a, b):
    def dec(func):
        def wrapped(*args, **kwargs):
            res = func(*args, **kwargs)
            assert(a < res < b)
            return res
        return wrapped
    return dec


if __name__ == "__main__":

    @check_range(1, 10)
    def foo(x):
        return x + 2

    print(foo(1))
    print(foo(2))
