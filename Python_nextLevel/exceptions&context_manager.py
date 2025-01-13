
try:
    pass
except(Exception):                 # here function isinstance() is called
    pass

# print(BaseException.__subclasses__())           # the parent of all exceptions in python including exceptions what we cannot handle
# [<class 'Exception'>, <class 'GeneratorExit'>, <class 'SystemExit'>, <class 'KeyboardInterrupt'>] - subclasses

# Exception           # is the class of all exceptions that we may want to handle
# if we want to handle all the exception, we should write:
# except Exception:
#     pass

# Different Exceptions:
NameError, AttributeError,KeyError,IndexError,TypeError,

AssertionError      # type of errors, that MUST NOT be handled (since these errors are used for tests)

ImportError         # might be used to import a replacement for module, which import was failed

ValueError          # if no other errors are suitable

# My Exceptions:
class MyBaseException(Exception):       # when you create a lot of connected exception (for example for a library)
    pass                    # it is recommended to create your own BaseException which inherits python Exception class
class MyMethodException(MyBaseException):   # after that all your exceptions can inherit your BaseException
    pass

# import traceback                        # the way to print traceback of error by yourself
# traceback.print_tb(ValueError.__traceback__)

# raise ImportError('You have error! :<')               # the way to raise an error with the given string printed
# raise TypeError from ValueError       # you can raise one exception from another one can be useful for debugging
try:
    pass
except Exception:               # if we have an error inside the except: we will get a message:
    pass                                                            # we have an Exception from (caused by) Exception
else:                           # we go here only if there are no exception
    pass
finally:
    pass

# Contex Manager:
# with acquire_resource() as r:     # looks like that: always release resources in the end (works as try + finally)
    # do_something()                # uses two methods __enter__ - the first row, __exit__ - when leaves body of manager

# if a function has these two methods, then it can be called 'Context Manager'
# with acquire_resource() as r, acquire_other_resource() as other:          # we can use more than one context manager

# synchronized - is a context manager
import threading                # interpretation of synchronized in Python
class synchronized:
    def __init__(self):
        self.lock = threading.Lock()
    def __enter__(self):
        self.lock.acquire()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.lock.release()

with synchronized():            # since it is a context manager it can be used with "with"
    pass

# !!! CONTEXLIB
from contextlib import closing   # closes files like "with open..." but is used not only for files (ex: HTTP resources)
from contextlib import redirect_stdout   # everything that is printed inside "with", will be transferred inside the file
from contextlib import suppress         # suppresses every error inside "with" body, which was given inside the method
                                                                                        # with surpress(Exception)
# ! Sometimes it is useful to use context managers as decorators, to do so we need ContextDecorator
from contextlib import suppress as _suppress, ContextDecorator
class suppressed(_suppress,ContextDecorator):
    pass                    # this class basically makes decorator from "suppress" using ContextDecorator

@suppressed(Exception)     # the whole function "do_something"  will be suppressed as if (with surpress(Exception):)
def do_something():
    pass
# ExitStack       - works strange is needed rarely (check it later, maybe)
