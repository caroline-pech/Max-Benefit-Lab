import sys
import time
import random

# test the dictionary insert speeds (and load factor)
##dict = {}
##for i in range(100, 1000):
##     dict[i] = i
##     print(i,sys.getsizeof(dict))

##d1 = dict()
##d2 = dict()
##
##for i in range(1, 2796205):
##   d1[i] = 0
##   d2[i] = 0
##
##
##t = time.time()
##for i in range(2796205, 5592406):
##   d1[i] = 0
##t1 = time.time() - t
##
##
##t = time.time()
##for i in range(2796205, 5592407):
##   d2[i] = 0
##t2 = time.time() - t
##
##print(t2 - t1)

#d = {1:a, 2:b, 3:c}
import random

class D(object):
    def __init__(self, n):
        self.n = n
    def __hash__(self):
        return random.randint(0, self.n)

d = {}
x = D(100)
d[x] = 0
del d[x]




