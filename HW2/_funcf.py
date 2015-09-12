#!/usr/bin/env python  # _funcf.py
def o1(f, g):
    ...
o2 = ...
if __name__ == '__main__':
    def f(x): return x*x + 1
    def g(y): return y*y - 2
    h = lambda z: z*z +3*z
    for o in [o1, o2]:
        fog = o(f, g)
        for x in [2, 3, 5]:
            print(fog(x) == f(g(x)))
        hogof = o(h, o(g, f))
        for x in [-1, -2]:
            print(hogof(x) == h(g(f(x))))
