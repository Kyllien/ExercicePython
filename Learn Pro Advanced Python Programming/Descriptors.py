import random
import time

class Descriptors:
    def __init__(self):
        self.__bmi = 0

    def __get__(self, instance, owner):
        return self.__bmi

    def __set__(self, instance, value):
        if isinstance(value, int):
            print(value)
        else:
            raise TypeError("Bmi can only int")
        if value < 0:
            raise ValueError("BMI")

        self.__bmi = value

    def __delete__(self, instance):
        del self.__bmi


class Person:
    bmi = Descriptors()

    def __init__(self, name, age, bmi):
        self._name = name
        self.age = age
        self.bmi = bmi

    @property
    def name(self):
        print("Get")
        return self._name

    @name.setter
    def name(self,name):
        print("set")
        self._name = name

    @name.deleter
    def name(self):
        print("deleting")
        del self._name

    def __str__(self):
        return"{0} age is {1} and bmi {2}".format(self._name, self.age, self.bmi)


# using property(get, setter, deleter) afin d'avoir de les personnaliser si besoin


person1 = Person("MO", 15, 14)
print(person1)
person1.name ="PO"
print(person1.name)

class Lazy:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]

    def __set__(self, instance, value):
        pass

class Waiting:
    @Lazy
    def wait(self):
        time.sleep(1)
        return 42

x=Waiting()
# print(x.wait)
# print(x.wait)
# print(x.wait)

class Values:
    def __init__(self):
        self._value1 = EventNumber()
        self._value2 = EventNumber()

    # def __str__(self):
    #     return " Value de {0} et de {1}".format(self._value1, self._value2)


class EventNumber:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "__" + name

    def __get__(self, obj, type=None) -> object:
        value = getattr(obj, self.private_name)
        return value

    def __set__(self, obj, value) -> None:
        setattr(obj, self.private_name, (value if value % 2 == 0 else 0))

val = Values()
val._value1 = -4
print(val._value1)

