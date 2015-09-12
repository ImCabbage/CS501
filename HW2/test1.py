#!/usr/bin/env python  # test1.py
from funcf import *
from io import StringIO

output = StringIO()
def f(x): return x*x + 1
def g(y): return y*y - 2
h = lambda z: z*z +3*z
for o in [o1, o2]:
    fog = o(f, g)
    for x in [2, 3, 5]:
        print(fog(x) == f(g(x)),file=output)
    hogof = o(h, o(g, f))
    for x in [-1, -2]:
        print(hogof(x) == h(g(f(x))),file=output)

key = 'True\n'*10

print('The desired output is:')
print(key)
print('Your output is:')
print(output.getvalue())
if key==output.getvalue():
    print('test1 is passed!')
else:
    print('test1 is failed!')


