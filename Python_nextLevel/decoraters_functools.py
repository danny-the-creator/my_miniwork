import functools


def trace(func):
    ''' This decorator works almost like a "help" functions but also calls the function itself '''
    def inner(*args,**kwargs):
        print(func.__name__)
        print(func.__doc__)
        print(args, kwargs)
        return func(*args,**kwargs)

    inner.__name__ = func.__name__      # these changes should be made in order to hide inner function
    inner.__doc__ = func.__doc__        # it gets all the necessary information from the function the decorator receives
    inner.__module__ = func.__module__
    # This can be done easier using functools:
    # functools.update_wrapper(inner, func)       # do the same as the above

# To write it cleaner, we could just use "@functools.wraps(func)" before the inner function instead of the line above

    return inner
@trace
def some(x):
    '''I just return x'''
    return x
some(56)
# help(some)

# We can "turn off" the decorator if we want to, to do so lets make a constant:
trace_enabled = True
def trace1(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        print(func.__name__)
        print(func.__doc__)
        print(args, kwargs)
        return func(*args, **kwargs)

    # we return our wrapped function if trace is enabled, otherwise just the function itself
    return inner if trace_enabled else func

# Decorator can take arguments: {@trace(*args)} but we nee to wrap the decorator:
def trace2(handle):
    def decorator(func):        # we construct the decorator with some attribute "handle" above
        @functools.wraps(func)
        def inner(*args,**kwargs):
            print(func.__name__, file=handle)
            return func(*args,**kwargs)
        return inner
    return decorator

# An example of the useful decorator:
import functools
def memorized(func):        # every time this function will be called, it will save the result in a cache dict
    cache = {}              # if the function is called the second time with the same arguments, it won't be computed,
    @functools.wraps(func)                                                      # it will be taken from cache: speed up
    def inner(*args,**kwargs):          # !!! arguments og your function have to be UNCHANGEABLE
        key = (args, tuple(sorted(kwargs)))
        if key not in cache:
            cache[key] = func(*args,**kwargs)
        return cache[key]
    return inner

# functools has a lot of basic decorators !