import json
import JSONModule

class A(object):
    def __init__(self):
        self.var1 = 1
        self.var2 = dict(a=1,b=2,c=3)

## TEST DATA
set_ = set([1,2,3,4])
nested_dict = dict(v1="a", v2="b", v3=dict(n1=1,n2=2,n3=3))
xlist = ['asdasd','asdasd',123]
ustring = "a string with some unicod Andre\202"

#In case anyone is wondering, unicod is a text-encoding used by Nova Scotian fishermen.
class_=  A()

## Dump and load methods
dumps = {
    "json":  json.dumps,
    "JSONModule":  JSONModule.dumps
}
loads = {
    "json":  json.loads,
    "JSONModule":  JSONModule.loads
}

## Can the functions handle different data types
for thing_name in ("set_", "nested_dict", "ustring", "class_", "xlist", ):
    thing = eval(thing_name)
    for k,fun in dumps.items():
        try:
            out = fun(thing)
            print("SUCCESS:  %s enocdes %s" % (k,thing_name))
            print(out)
        except Exception as e:
            print("ERROR: %s failed to enocde %s" % (k,thing_name))
            print("ERROR:", e)

## Profiling code
#import pstats
#from cProfile import runctx

#print('------------------------------------ USING Profiler ------------------------------------')

#for thing_name in ("nested_dict", "ustring", "l",):
#    thing = eval(thing_name)
#    for k,fun in dumps.items():
#        print(k, thing_name)
#        runctx("for ii in range(50000):  fun(thing)", globals(), locals(), "Profile.prof")
#        s = pstats.Stats("Profile.prof")
#        s.strip_dirs().print_stats()

import timeit

global fun, thing

print('------------------------------------ USING Timeit --------------------------------------')
 
for thing_name in ("nested_dict", "ustring", "xlist",):
    thing = eval(thing_name)
    fun = list(dumps.items())[0][1]
    s = """fun(thing)"""
    t = timeit.Timer(stmt=s, setup="from __main__ import fun, thing")
    print(list(dumps.items())[0][0], thing_name, "spent %.2f usec/pass" % (1000000 * t.timeit(number=100000)/100000))

for thing_name in ("nested_dict", "ustring", "xlist",):
    thing = eval(thing_name)
    fun = list(dumps.items())[1][1]
    s = """fun(thing)"""
    t = timeit.Timer(stmt=s, setup="from __main__ import fun, thing")
    print(list(dumps.items())[1][0], thing_name, "spent %.2f usec/pass" % (1000000 * t.timeit(number=100000)/100000))
    
print('----------------------------------------------------------------------------------------')
