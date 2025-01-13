# float("inf")          max number in float
# float("-inf")         min number in float

# if (3 < x < 5):       easy way to write boundary (instead of (x>3)and(x<5))
#                       * - package and unpackage - need to use more frequently

# None - falsy (bool(None) == False)

# list, set, dict ... - should not be a default value, instead you can use something like this:
# def unique(iterable, seen=None):    seen should be a set, but we cannot use a default set,
#                                           so we set seen to unchangeable None
#     seen = set(seen or [])            this line makes a set from seen or if seen is None (which is falsy),
#                                                                                       it just creates a new empty set

# def flatten(x,*, depth = None)       * - in this case just ignores all elements after the x
#                                                           (in case we want to farce user to write named variables)
# (x1, y1), (x2, y2) = (1,2), (3,4)         - easy way to unpack variables: x1 = 1, y1 = 2, x2 = 3, y2 = 4
#                               if we write "-" instead of the variable, the value on that position will be ignored
# nonlocal                       represents enclosing field of view - every variable, which is not global and not local
#                                           (if we have function in function) (Is similar to the "global")
# global - not needed, usually means that the code could be written better      !!!

# list(zip("abc", range(3), [42j,42j,42j])) == [('a', 0, 42j), ('b', 1, 42j), ('c', 2, 42j)]
#                                                                                   zip can take more than 2 arguments
# [x for xs in nested for x in xs]        flatten: [(1,2),(3,4,5),(6)] ==> [1,2,3,4,5,6]

# def inner(func):
#     inner.count = 0         # this is not a variable, but an attribute, so we have access to this data on global level

# functools has a lot of basic decorators !


