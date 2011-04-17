import json
import JSONModule

class A(object):
    def __init__(self):
        self.var1 = 1
        self.var2 = dict(a=1,b=2,c=3)

## TEST DATA
set_ = set([1,2,3,4])
nested_dict = dict(v1="a", v2="b", v3=dict(n1=1,n2=2,n3=3))
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
for thing_name in ("set_", "nested_dict", "ustring", "class_", ):
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
from profile import run
for thing_name in ("nested_dict", "ustring", ):
    thing = eval(thing_name)
    for k,fun in dumps.items():
        print(k, thing_name)
        run("for ii in range(10000):  fun(thing)")

