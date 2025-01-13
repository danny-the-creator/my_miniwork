class Counter:
    all_counters = []
    def __init__(self):
        """we can address not only the instance, but also the class itself,
        in this way all instances of this class will have the same attribute"""
        Counter.all_counters.append(self)

class Info:
    public_information = "email"            # public attribute
    __private_information = "password"      # private attribute - use "__" as start of the attribute's name
    _eternal_information = "lghjkjh"        # information, which should not be protected, but is not needed
#     ! you can address this information if you really want but IDE won't help you find this attribute
print(Info.public_information)
# print(Info.__private_information)           # throws an error
class Noop:
    '''I print all my methods'''
    def __init__(self):
        print(Noop.__name__)
        print(Noop.__doc__)
        print(Noop.__module__)
        print(Noop.__bases__)               # stores all parents of the class
        print(self.__class__)               # shows the class of the instance
        print(Noop.__dict__)                # stores all the attributes of the class
        print(self.__dict__)                # shows all the attributes of the instance

class Noop:
    __slots__ = ['some_attribute']          # saves these attributes: they can not be added or deleted
# n = Noop()
# print(n.__dict__)                           # moreover, instances of this class won't even have dict


# !!! if we call a method on an instance, then self is the instance of the class, if we call method of the class itself,
                                                # then we should give an instance as a parameter (usually not needed)

class My_class:
    something = 0
    def __init__(self, something):
        self.something = something
        super().__init__()                  # calls the same method of the super class (object in this cas)
    @property
    def not_needed_attribute(self):        # works as an attribute not a function, but computes, only when it is called
        return My_class(dir(self.something+1))      # basically, it is a GETTER
# !!! Moreover you can use *.setter, *deleter   * - name of the method with property flag
r =My_class(0)
print(r.something)
print(r.not_needed_attribute)

# isinstance(My_class(), (My_class, Noop))         # checks if the given object is instance of one of the given classes

# !!! type(My_class()) == My_class - WRONG way !!!

# issubclass() # takes two classes and works as isinstance function

# Mixin classes         you can create a class, that can be used only in combination with other class like:
class Counter:
    """imagine it works as a counter"""
    pass
class ThreadSafeMixin:
    """imagine it works only in combination with other classes, and doesn't work by itself """
    pass
class ThreadSafeCounter(ThreadSafeMixin,Counter):
    """this class will implement the counter functionality, but it will be threadsafe"""
    pass

# !!! We can use decorators with classes, work in the same way
# you can write singleton function as a decorator to make a chosen class singleton

class Noop:
    def __getattr__(self, item):
        '''this method is called when you try to access the attribute, that doesn't exist '''
        return f'{item} is not the attribute'
    def __setattr__(self, key, value):
        '''is called when an attribute is wanted to be set'''
        pass
    def  __call__(self, *args, **kwargs): # is used for decorators
        '''allows to call the instance of the class: Noop()(42)'''
        pass
    def __str__(self):
        '''it is called, when print(instance of this class) is used'''
        pass
    def __repr__(self):
        '''call of the constructor'''
        pass
    def __bool__(self):
        '''return the boolean value of the instance of the class,
        for example, it can be used in "if" statement (if Noop():) '''
        return bool(self.value)
# ! total_ordering from functools - is used to make your class comparable
