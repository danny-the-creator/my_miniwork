# person = ("George", "Carlin", "May", 27, 1989)
# name, date = slice(2), slice(2,None)        # basically mean [:2] and [2:]      (we slice the list)
# print(person[name])
# print(person[date])

# from collections import namedtuple  # Named tuple is the same tuple but, where every index and tuple itself has names
#
# student = namedtuple('student', ['name', 'age'])  # 'Person' - name of the tuple | ['name', 'age'] - name of fields
#                                                                     # that's just a general representation
# me = student('Danil', age=142)  # this way we create a specific example of the tuple above
#
# print(me.name, me.age)
# print(me._asdict())             # represents the named tuple as a dict
# me = me._replace(age=201)            # !!! very useful function: allows us to change "unchangeable" tuple
# print(me)

# Way of replacing elements in a list
# sx = [1,2,3]
# sx[:2] = [0]*2
# print(sx)

# Sorted() and .sort can take some arguments: key and reverse
# xs = [1,2,4]
# xs.sort(key=lambda x: x % 2, reverse=True)  # key takes a function as an argument, which will be used to sort the list
# print(xs)                                                       # in this case we sort by rest of the division by 2

# .pop(0) is bad, since it makes a copy of the rest of the list not efficient
from collections import deque           # it is better to use double linked list
q = deque([1,2,3], maxlen=5)       # maxlen makes sure that your length of your list won't be more than this number
q.append(4)                             # double linked list has the following methods
q.appendleft(0)
q.pop()
q.popleft()

# sets have a method update: it just adds all the elements to the set
# x = set((1,2))
# x.update([1],[3,4],[8])
# print(x)
# x.remove        # throws an error if x has not this element
# x.discard       # ignores if x has not this element

# DICTS
# new_dict = dict.fromkeys(['key0', 'key1'], 0)
# print(new_dict)        # all the keys get the same value you mentioned
#                                                                               (! the value should be unchangeable !)
# print(new_dict.get('key1', 5))              # get has one more parameter: the default value
# print(new_dict.get('key2', 5))
# new_dict.setdefault('key2', 2)            # it will set the default value only if there are no such a value in a dict
# new_dict.update()                         # see "list update" above
# new_dict.pop('key0')                      # it is the same pop from list

# !!! defaultdict !!!                       # very useful for graphs
# from collections import defaultdict

# g = defaultdict(set, **{"a": {"b"}, "b": {"c"}})        # the dict will be filled up with all elements starting from
# the second one, the first argument is used to initialise a new key (default value) should be a simple function(lambda)
# g['c'].add('a')         # since we don't have such a key in the dict, it will be created with the default value,
                                                                                # after that method add will be called
# print(g)

# from collections import OrderedDict    # works the same way as a simple dict, but its keys are ordered
# x = OrderedDict()                  # (if the first key, which was added was '7' - on the first iteration we get 7)
#
# from collections import Counter         # that's the dict which has the number of key occurrences as a value
# counter = Counter(['foo','foo','foo','map','map','bar'])
# print(counter)
# print(counter['zu'])        # returns 0, since there are 0 occurrences of the word 'zu'
# counter.most_common(2)         # returns to 2 most common
