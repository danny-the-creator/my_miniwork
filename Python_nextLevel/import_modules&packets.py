# module - is any file with ".py" extension
import sys

import new_features
print(dir(new_features))            # any module has some attributes:
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

# you can write and delete new variables in the imported module
new_features.some_value = 42
print(new_features.some_value)
del new_features.some_value

# __name__ usually stores the name of the file, unless this file is used as a script (you run the file, not import)
                                        # in this case: __name__ == __main__
import numpy as np               # doesn't change __name__ of the file, only assigns this library to a given variable

# import sys
# print(sys.path)

# __all__             # when from module import * - all objects from __all__ list, and only from it, will be imported

# PACKETS
# any directory, which has __init__.py becomes a packet and when we import directory.__name__, only __init__.py will
                                                                                        # be called (as with modules)
# others files of packet (except __init__) should be imported separately: ex. import srs.game
                                                                             # alternative way: from srs import game
# !!! It is BETTER to use relative import:
# from . import game            # in this case name of the directory doesn't matter and the program won't crash if
                                    # name of the directory was changed ! Works only if this fild is inside the packet !

# __init__.py     - cannot have a lot of code: we can create some global variables, or we can just import other packets
                                                                                                # inside the __init__.py
# Ex: let's say we have "useful_name" packet, it has two files: first.py, second.py and also __init__.py
# then inside the __init__.py we can write:
# from .first import *
# from .second import *
# __all__ = first.__all__ + second.__all__

# In this case when we import "useful_name" it will have all attributes of first and second files
# __main__.py - name of the file, that will be executed when packet is run, (not imported)


# IMPORT

# import - calls a function __import__() from builtins          just info

# modules should be imported only ones

# sometimes it is useful to import files inside the function:
# def first():              # for example if the imported object is needed only once
    # from . import some_variable     # or if the module, which stores this variable imports the function (import loop)
    # print(some_variable)

# import sys
# if module not in sys.path -> the module cannot be imported
# sys.path ia a list of directories: the current one, standard library, our packets...

# sys.path.extend([a,b])        sys.path can be changed
# meta_path - stores all "finders" (methods, which are looking for all imports)
# which finder to use is decided by the function, which is stored in sys.path_hook (we can also extend this list)  !
# sys.meta_path[0].find_spec() - every component of meta_path has method find_spec(),
                                                    # which tries to find the given module, using chosen "finder"
# the system uses it automatically, so THESE METHODS WON'T BE USED
# ! But it can be used to upgrade the following structure:
# Instead of:
# try:
#     import _useful_speedups as useful
# except ImportError:
#     import useful

# Is better to use this:            (because in upper case all ImportErrors will be ignored, that might not be needed)
# from importlib.util import find_spec
# if find_spec("_useful_speedups"):
#     import _useful_speedups as useful
# else:
#     import useful

# using find_pec we can ever create an AutoLoader (which will install a module using pip if it doesn't find any)
