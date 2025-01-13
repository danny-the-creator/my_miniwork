# ITERATORS
# StopIteration               # an error which is thrown, when the iterator doesn't have the next element
                                    # it is thrown in "for" loop to stop it
# for i in iter(read_block,'k'):  # calls __next__, until the result of __next__ is given value
#     print(i)                    # read block - iterator (has a function next)

# next(iter, __default=value)       # next method has a default value (instead of StopIteration)

# in and not in             use method __contains__ of the object

# !!! iterator is a class which has two methods: __iter__, __next__
# iterable is an object which can be used as iterator (list, str, dict...)

# map, filter, zip            - are iterators

# GENERATORS

# generator is a function, which has method "yield"
# def unique(iterable, seen=None):
#     seen = set(seen or [])
#     for item in iterable:
#         if item not in seen:
#             seen.add(item)
#             yield item
# xs = [1,2,2,3,3,3,4,4,4,4,5]
# gen = unique(xs)                # gen is just an iterator object it doesn't store (and even didn't compute) anything
# print(type(gen))
# print(gen)
# print(next(gen))                # prints the first unique element and freeze the generator (1)
# print(next(gen))                # 2
# print(next(gen))                # 3
# print(next(gen))                # 4
# print(next(gen))                # 5
# # print(next(gen))                # Throws an exception StopIteration (there is no more yield)
#
# print(2 in unique(xs))          # for all generators is default implementation of "in"

# Generators could be infinite
# def count(start=0):
#     while True:
#         yield start
#         start+=1
# counter = count(1)
# print(next(counter))
# print(next(counter))
# print(list(count()))            # we cannot create an infinite list...

# !!! you cannot reuse generators !!!

# generator can be written in one row, using (i for i in list if True)-same syntax as in list generator () instead of []

# yield can be used as a value
# this value can be transmitted to the generator using generator.send()
# def f():
#     x1 = yield
#     print(x1)
#     x2 = yield 8            # the number doesn't matter
#     print("x2="+x2)
#     yield
# s = f()
# next(s)
# s.send(None)                # firstly we should transmit None (rules...)
# next(s)                     # after that we go to the next yield
# s.send(None)
# s.send('100')               # and transmit the second value, this value will be printed
                            # works as "next" but we choose the value we want to transmit ("next" always transmits None)
# next(s, None)

# s.throw(Exception)          # throws an Exception to the yield we are currently at

# s.close()                   # the way to exit the generator - throws the following error:
# GeneratorExit               # one of the exceptions, that can be thrown

# using this technique we can create CooPROGRAMS

# CooPROGRAMS are used as a "magic box" you give them something using s.send, and they do something in response
# def grep(pattern):          # this generator gets pattern and check if this pattern is contained in a given string
#     print(f"Looking for {pattern}")
#     while True:
#         line = yield
#         if pattern in line:
#             print('Found it!')
# gen = grep('you')
# next(gen)
# gen.send('Hello world!')
# gen.send('Tell me')
# gen.send('I love you')

# to make it look better we can use decorators and inside the decorator call method "next", which is 'costili'

# yield from iterable        works as following:
# for i in iterable:
    # yield i

# return                   it calls StopIteration in generators, but if we use return,this exception cannot be handled

import itertools    # !!! useful module MORE information is needed

from itertools import islice        # it works as the simple slice, but it is more efficient, since it doesn't copy
# xs = list(range(10))                                          # the list (it uses generator)
# print(list(islice(xs, 2, 7, 2)))    # it gets: LIST | start_point | end_point | step
# print(list(islice(xs,4, None)))     # None means till the end (same as [4:])
# print(list(islice(xs, 2)))          # if only one number is given, that will be the end point (same as [2:])

from itertools import cycle, count, repeat      # all of them are INFINITE generators

# count(0,5)                          # counts from 0 with step = 5, till infinity
# cycle([1,2,3])                      # goes in a loop: 1->2->3->1->2->3->1->2->...
# repeat(11,3)                        # repeats the same number 3 times, it cannot be...

from  itertools import dropwhile, takewhile
print(list(dropwhile(lambda x: x<5, range(10))))  # DROPS all the elements from the given list, if function returns True
print(list(takewhile(lambda x: x<5, range(10))))  # TAKES all the elements from the given list, if function returns True

from  itertools import chain            # concatenates N iterators

from itertools import tee               # cloning machine

it = range(3,5)
x1,x2,x3,x4,x5 = tee(it, 5)             # all these iterators are independent

# itertools has a lot of tools for COMBINATORICS
from itertools import product, permutations, combinations, combinations_with_replacement

print(list(product("AB",repeat=2)))     # computes all possible products from AB, every element is repeated twice
print(list(product("ab",repeat=3)))

print(list(permutations("ABC")))
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

print(list(combinations("ABC", r=2)))      # [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(list(combinations_with_replacement("ABC",r=3)))       # same thing as above, but elements can be repeated
# [('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'B', 'B'), ('A', 'B', 'C'), ('A', 'C', 'C'),
                                                # ('B', 'B', 'B'), ('B', 'B', 'C'), ('B', 'C', 'C'), ('C', 'C', 'C')]

