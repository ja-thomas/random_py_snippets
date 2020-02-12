#! /usr/bin/env python3

from robots import Robot

x = Robot("Marvin", "Nürnberg")
x.say_hi()

y = Robot("Hen", "Nürnberg")
y.say_hi()
try:
    y.name = "Henry"
except NameError as e:
    print(e)

try:
    z = Robot("Hans", "München")
except NameError as e:
    print(e)

w = x + y
w.say_hi()

print(w)
print(repr(w))
w2 = eval(repr(w))
w2.say_hi()

print(w == w2)
