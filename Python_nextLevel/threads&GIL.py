from time import sleep
import threading
def countdown(n):                   # one way of threading is to create thread and then start it
    for i in range(n, -1, -1):
        print(i)
        sleep(1)
# countdown(5)
t = threading.Thread(target=countdown, args= (4,))     # target - the function we use, args  should be itterable
t.start()                               # in this case, the program won't be closed, till thread is finished
# if we want to kill all threads if the main Thread is finished we should set daemon to True (False is the default one)
# t = threading.Thread(daemon=True)

class CountdownThread(threading.Thread):        # another way of threading is by creating a class which inherits Thread
    def __init__(self,n):
        self.n = n
        super().__init__()                      # we should call super().__init__() when implementing this class
    def run(self):                              # inside run method we can run anything and it will be a separete thread
        for i in range(self.n, -1, -1):
            print(i)
            sleep(1)
t = CountdownThread(5)              # the second way is usually NOT used
t.start()                           # calls run() method

# t= threading.Thread(name="counter")       # threads can be named (used for debugging)
t.join()                            #  MainThread waits for the end of the given thread
print("FInished")
t.is_alive()                         # returns if thread is still running (not finished)

# to kill the thread even if it is not finished you can write a method, which sets FINISHED to True and inside run()
# you can write:  while not FINISHED:

# ! synchronisation !

# Lock and RLock            lock - blocks any attempts to get the recourse,
#                                                               rlock - allows the owner to get lock more than once
                                    # rlock - is better to use
# semaphore                 allows more than one thread to get the lock (you can set the limit yourself)

# bounded_semaphore         throws an exception if locks wasn't released as many times as it was taken

# all og them have two methods: acquire and release
# methods wait and notify           - wait blocks the thread, until notify will be called somewhere
# !!! Sometimes the thread can wake up even without "notify", to avoid this "wait" should be inside while (not if)


import queue            # this module has several threadsafe queues:

# Queue - fifo
# LifoQueue - lifo (stack)
# PriorityQueue - every element of this queue represents a pair of element and its priority
# ! don't forget to write queue.task_done() when you are working with the elements of the queue,

import concurrent.futures as f
executor = f.ThreadPoolExecutor(max_workers=4)      # executor is an object, which controls several threads
fut = executor.submit(print, "Submitted")                 # after the submission executor is ready to work
executor.map(print, ['Work', 'Work hard', 'Work smart'])       # for every worker the given command will be called
                                                                                                # with the given args
# executor.shutdown()         # executor cannot do anything after that

# "futures" has several interesting methods (after submission)
fut.running()
fut.done()              # return Bool value
fut.cancelled()

fut.result()            # will block everything, until the given thread will be finished
fut.add_done_callback(print)     # will apply the given function to the result (when it will be calculated)


# !!! GIL !!! - global interpreter lock
# it guaranties that at any moment only one thread will have access to the interpreter's internal condition (not good!)
# to avoid some (not all) problems we can use "cython" using the following command:
# with nogil:
import asyncio
# async def                 - co-program
# inside "async" we use await instead of yield from (same logic)

import multiprocessing as mp            # another way to solve GIL related problem (every process has its own GIL),
                                                # works almost as threading:
p = mp.Process(target=countdown, args=(5,), daemon=False)
p.start()
print(p.name, p.pid)
p.join()

# !!! to transfer data between processes we need a Pipe, so mp is less effective than using "cython"
parent,child = mp.Pipe()
# ! Not complete syntax !
# parent.send()           # use this inside the process, which is sending
# child.recv()            # use this inside the process, which is receiving


import joblib       # the packet, which can be used to create trivial parallel independent threads or processes
