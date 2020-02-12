#! /usr/bin/env python3


class Letters(object):
        def __init__(self):
            self.current = 'a'
        def __next__(self):
            if self.current > 'd':
                raise StopIteration
            result = self.current
            self.current = chr(ord(result)+1)
            return result
        def __iter__(self):
            return self



if __name__ == "main":
    x = Account("bla")
    y = Account("blubb")
    print(x.interest)
    print(y.interest)
    x.interest = 2
    print(x.interest)
    print(y.interest)
    Account.interest = 5
    print(x.interest)
    print(y.interest)
