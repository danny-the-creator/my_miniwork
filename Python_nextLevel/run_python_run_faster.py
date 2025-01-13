# As and examples of optimisation the Matrix multiplication will be used
# timeit - one of the fairest libraries to calculate the working time

import cProfile     # shows how much time every function has worked, how many times it was called...
                                        # but this can be used only if we try to speed up more than one function
# import line_profiler  # shows how much time we spend on every line (in %)

# Ways of making your program faster:
# 1. make variables (instead of calling twice the same function, call it once and assign to a variable)
# 2. use default functions (ex. from builtins) usually they are written in C, so they are much faster
# 3. loops in python are slow, so sometimes it is better to use generator instead
# 4. if something is already done (method of a library), it's almost 100% better, than you can implement by yourself
                                                            # at least, for short period of time and using only python


# !!! Compilation !!!
# To make python even faster, we should use different languages
# there are 2 different ways:
# 1. Ahead_of_time compilation - we can either write code on C, which will be clear to python interpreter, or easier way
#    we can write a code on python, but then translate it to syntax which is clear to faster languages (C - Cython...)
# 2. Just_in_time compilation - we have a code on python and try make it faster only when running it
#                               (ex. Numba - the code is transmitted to LLVM, which is doing all the optimisation job)

import numba
@numba.jit              # just write this before the function, which needs to become faster, and everything works well
def faster_func():  # however, not all functions can be speed up,  for ex. it cannot make list operations faster
                        # or the function has a lot of python methods, the code should be as simlie as possible,
    pass                                                        # like it was written on C (which is used by numba)

# import cython       "cython" - extends python (everything that is written on python will work on cython)
import cython

# %%cython          (the syntax is wrong, because it was meant for compiler )
# this "magic" function compiles everything that is beneath with Cython and assigns compiled version to a variable
# def some_func():
#     pass

# it is easy to write (just compile everything using cython), but the code becomes just a bit faster
# to make your code even faster, you should make it more clear to C,
# Cython has several features for it (ex. adding type - "cdef int name = ...", cimport, adding type to the result
#                    inside [] - ex. np.ndarray[np.int64_t, ndim = 2] - the 2dim matrix with values inside 64 range)

# Moreover, to make your code even faster we can disable some cython checks, to do so:
# cimport cython
# @cython.boundarycheck(False)
# @cython.overflowcheck(False)
# def func():
#     pass

# !!! BEFORE TRYING TO SPEED UP YOUR FUNCTION,TRY TO FIND IT IN INTERNET,AND ONLY IF YOU FOUND NOTHING, IMPLEMENT IT !!!

# !!! DON'T INVENT THE BICYCLE !!!
