# import doctest      # first method
# def sqr(x):         # doctest is used by default (so we don't even need to import it)
#     """this function has some tests inside the dock:
#
#     >>> sqr(2)   #   after '>>>' you should write your function's test and after an ENTER you should write the result
#     4
#     >>> sqr(-3)  # doctest has some features: +NORMALIZE_WHITESPACE ignores spaces and enters,
#     9
#     >>> sqr(0)                                # +ELLIPSIS - you can write ... and everything after this will be ignored
#     0
#     """
#
#     return x**2
# doctest.testmod()
# print(sqr(4))

# assert            # second method

# def test_abs_pos():         # a good test should have a specific goal and also be short and clear
#     assert abs(42) == 42
# def test_abs_neg():         # if the equation doesn't hold, we get AssertionError, with the text indicated
#     assert abs(-42) == -42, "Should be positive"                                    # after a comma
# test_abs_pos()
# test_abs_neg()

# Example of an excellent test (like the one checkio uses)
# def test_division():
#     actual = 42/0.1
#     expected = float("inf")
#     message = f'Expected: {expected}, Got: {actual}'
#     assert actual == expected, message
# test_division()

import unittest         # it is from java, so we should write all tests in classes
                                                        # which inherit unittest.TestCase
# unittest.main()         # run all the tests in classes

# apart from different asserts "TestCase" has setUp() and tearDown(), which are called at the start and end

# Py.Test
# import pytest
# !!! to use this library you should type "python -m pytest (testfile_name)" , testfile_name is optional
# after that pytest is going to find all test-like functions (starting with test, or ending with _test...) and run them
                    # moreover, it will give a complete argumentation where and why the AssertionError was called
# the only thing you need to do is to write some tests call them appropriate and include some assertion there
# if the testfile_name is not mentioned, you will get all test-like functions from the whole directory
import pytest

# pytest.raises()     # work as raise
# def double(x):
#     return 2*x
# writing test in this way allows you to save time, instead of 5 asserts you can just write parametricTests in this way:
# @pytest.mark.parametrize('input,expected',[
#     (2,4),
#     (100,200),
#     (3,6),
#     (-10, -20),
#     (0, 0)
# ])

# @pytest.yield_fixture
# def oracle():    # pytest uses context manager "yield_fixture" instead of setUp & tearDown, but works in a similar way
#     pass

# ! it has much more functionality - could be useful


# hypothesis - check post-conditions

import hypothesis.strategies as st      # are used in "given" generate random values of the given type
from hypothesis import given  # it takes as many arguments as the test function and will use the given values to test

@given(st.lists(st.integers()))
def test_sort(xs):
    result = sorted_not8(xs)
    assert all(xi<=xj for xi,xj in zip(result, result[1:]))    # "all" is used for testing and is written as generators

def sorted_not8(xs):        # sorted function, which fails if len(xs) == 3
    return xs if len(xs) == 8 else sorted(xs)

# st - has a lot of generation types
# st.just(0) ,st.none, st.text...
# and a lot of useful functions:
# st.one_of(tuple),
