def counter(func):
    k = 0

    def wrapper(*args, **kwargs):
        nonlocal k
        res = func(*args, **kwargs)
        k += 1
        print("Function {} was successfully called {}"
              " times".format(func.__name__, k))
        return res
    return wrapper


if __name__ == "__main__":
    def succ(a):
        return a+1

    def pred(a):
        return a-1

    succ = counter(succ)
    pred = counter(pred)
    for x in range(10, 20):
        succ(x)
        pred(x)
