#!/usr/bin/env python  # _randNo.py
import sys, copy, random
class RandNo(object):
    ...
if __name__ == '__main__':
    for denom in [7, 7.0001, 6.9999]:
        pr = [1/denom]*7
        try:
            RandNo(pr)
        except ValueError as e:
            print(e)
    print(RandNo([0.51, .49]))
    print(repr(RandNo([0.47, 0.53])))
    histogram = [0]*4
    N = RandNo([0.3, 0.1, 0.4, 0.2])
    for k in range(1000):
        histogram[N()] += 1
    print(histogram)
    import time
    for power in [12, 13]:
        n = 2**power
        N = RandNo([1/n]*n)
        t0 = time.time()
        for k in range(1000): N()
        t1 = time.time()
        print('for n = %d, computing time is %f' % (n, t1 - t0))
    Die = RandNo([0.] + [1./6.]*6)
    ThreeDice = Die + Die + Die
    histogram = [0]*19
    for k in range(1000):
        histogram[ThreeDice()] += 1
    print(histogram[3:])
