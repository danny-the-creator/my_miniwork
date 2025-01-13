# descriptor - a class, which allows you to __set__, __get__, and __delete__ some variable

class Descr:
    def __get__(self, instance, owner):  # this method is called when we address a variable
        print(instance, owner)  # owner is a type of the instance


class A:
    attr = Descr()


A.attr  # in this case class A is an owner and we don't have an instance of class, so it is None
A().attr  # in this case A is still an owner, but we addressed not the attr of the class, but rather attr of its instance


class Descr1:
    def __set__(self, instance, value):  # this method is called when we set a value to the attribute
        print(instance, value)


class B:
    attr = Descr()


B().attr = 42  # works only with instances
B.attr = 42  # just replace value of B.attr from =Descr() to 42


class Descr2:  # work absolutely the same as __set__
    def __delete__(self, instance):
        print(instance)

# data_descriptor - the one with __set__
# non-data_descriptor - the one without __set__

# data_descriptors are GREEDY

# the best way to store information in descriptors: store in inside dict of the instance:

class Proxy:
    def __init__(self,label='attribute'):
        self.label = label
    def __get__(self, instance, owner):
        return instance.__dict__[self.label]
    def __set__(self, instance, value):
        instance.__dict__[self.label] = value
    def __delete__(self, instance):
        del instance.__dict__[self.label]
class Something:
    attr = Proxy('attr')
some = Something()
some.attr = 40
print(some.attr)

# @staticmethod and @classmethod      are decorators
class SomeClass:
    @staticmethod                   # the method of the class becomes a simple function (which doesn't take "self")
    def func():                                 # usually not needed
        print('nothing')
    @classmethod
    def func1(cls):                 # takes class of the object as a parameter instead of instance of the class ("self")
        print(cls)                              # is needed to create alternative constructor

# META_CLASS
# for example, since type(any_class) is type, type may be considered metaclass

# we can create a class using metaclass
# Something = type("Something", (), {"attr":42})            # same as "Something" above
# Something is class (and instance of meta_class)

class Another(metaclass=type):              # all classes have "type" as a default value of the metaclass attribute
    pass                                                # However, we can write owr own meta_classes here

class Meta(type):           # is meta_class
    pass

# meta_class can have some methods:
# __prepare__

# !!! __init__ - is not a constructor, it just initialises variables
# !!! __new__ is the TRUE constructor !!!   - in the end this methods returns instance of the class
                                                            # __new__ - is staticmethod

# metaclass has     similar functionality with class_decorators

# !!! import abc        abstract methods
from collections import abc
#       ! This module has a lot of BASE-classes, which can be inherited to implement something more
#  ex. : abc.Iterable, abc.Hashable, abc.AsyncIterable ...
import abc
class Iterable(metaclass=abc.ABCMeta):
    @abc.abstractmethod       # makes from this class an abstract one, some of these methods should not be implemented
    def __iter__(self):             # this method should be implemented in classes, which inherit this one
        pass