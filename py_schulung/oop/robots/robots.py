
class allowed(type):
    def __init__(cls, *args, **kwargs):
        cls.allowed_cities = {"Erlangen", "Nürnberg", "Fürth"}
        cls.forbidden_names = {"Henry"}

    @property
    def allowed_cities(cls):
        return cls.__allowed_cities

    @allowed_cities.setter
    def allowed_cities(cls, value):
        cls.__allowed_cities = value

    @property
    def forbidden_names(cls):
        return cls.__forbidden_names

    @forbidden_names.setter
    def forbidden_names(cls, value):
        cls.__forbidden_names = value


class Robot(metaclass=allowed):

    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name in Robot.forbidden_names:
            raise NameError("{} is an forbidden name".format(name))
        self.__name = name

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if city not in Robot.allowed_cities:
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
