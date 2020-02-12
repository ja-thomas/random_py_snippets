
class Robot():

    def __init__(self, name):
        assert(name != "Henry")
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)
