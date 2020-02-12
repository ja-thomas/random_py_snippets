#! /usr/bin/env python3


from operator import add, sub


def make_ternary_constraint(a, b, c, ab, ca, cb):
    """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b)=a."""
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]


def adder(a, b, c):
    """The constraint that a + c = c"""
    return make_ternary_constraint(a, b, c, add, sub, sub)


def make_connector(id):
    """Return a functional implementation of a connector"""
    cons = {}

    def set_val(source, values):
        pass

    def has_val():
        pass

    def forget():
        pass

    def connect():
        pass

    def dispatch(message, source=None, values=None):
        if message == "set_val":
            return set_val(source, values)
        elif message == "has_val":
            return has_val()
        elif message == "forget":
            return forget()
        elif message == "connect":
            return connect()

    return dispatch


if __name__ == "name":

    def make_converter(c, f):
        """Connect c to f with constraints to convert from Celsius to
        Fahrenheit."""
        u, v, w, x, y = [make_connector() for _ in range(5)]
        multiplier(c, w, u)
        multiplier(v, x, u)
        adder(v, y, f)
        constant(w, 9)
        constant(x, 5)
        constant(y, 32)

    make_converter(celsius, fahrenheit)
