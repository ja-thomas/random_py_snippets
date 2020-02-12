#! /usr/bin/env python3

from robots import Robot

x = Robot("Marvin")
x.say_hi()

y = Robot("x")
y.name = "Henry"
y.say_hi()
