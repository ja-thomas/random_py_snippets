
class Robot():

    __allowed_cities = {"Erlange", "Nürnberg", "Fürth"}

    __forbidden_names = {"Henry"}

    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name in Robot.__forbidden_names:
            raise NameError("{} is an forbidden name".format(name))
        self.__name = name

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if city not in Robot.__allowed_cities:
            raise NameError("{} is not a valid city.".format(city))
        self.__city = city

    def say_hi(self):
        print("Hi, I am {} from {}".format(self.name, self.city))

    def __add__(self, other):
        return Robot(self.name + "-" + other.name, self.city)

    def __str__(self):
        return "{}, {}".format(self.name, self.city)

    def __repr__(self):
        return "Robot('{}', '{}')".format(self.name, self.city)

    def __eq__(self, other):
        return self.name == other.name and self.city == other.city
