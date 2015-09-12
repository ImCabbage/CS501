#!/usr/bin/env python  # test3.py
from randNo import *
from io import StringIO
output = StringIO()
for denom in [7, 7.0001, 6.9999]:
    pr = [1/denom]*7
    try:
        RandNo(pr)
    except ValueError as e:
        print(e,file=output)
pr = [0.51, .49]
N = RandNo(pr)
print(str(N) == 'RandNo[0.51, 0.49]',file=output)
pr = [0.47, 0.53]
print(str(N) == 'RandNo[0.51, 0.49]',file=output)
N = RandNo(pr)
print(repr(N) == 'RandNo[0.47, 0.53]',file=output)
histogram = [0]*4
N = RandNo([0.3, 0.1, 0.4, 0.2])
for k in range(1000):
    histogram[N()] += 1
print(histogram,file=output)
import time
for power in [12, 13]:
    n = 2**power
    N = RandNo([1/n]*n)
    t0 = time.time()
    for k in range(1000): N()
    t1 = time.time()
    print('for n = %d, computing time is %f' % (n, t1 - t0),file=output)
Die = RandNo([0.] + [1./6.]*6)
ThreeDice = Die + Die + Die
histogram = [0]*19
for k in range(1000):
    histogram[ThreeDice()] += 1
print(histogram[3:],file=output)

key = """Probabilities sum to 0.9999857.
Probabilities sum to 1.0000143.
True
True
True
[298, 104, 390, 208]
for n = 4096, computing time is 0.004333
for n = 8192, computing time is 0.004457
[4, 23, 36, 43, 69, 119, 101, 128, 119, 104, 95, 81, 42, 27, 8, 1]
"""

print('The desired output is:')
print(key)
print('Your output is:')
print(output.getvalue())
notes="""
Note:
1. Your program may generate different random numbers from the desired output.
Make sure that your program generates the random numbers from the correct distribution.
2. Your computing time may be different from the numbers shown in the desired output.
To be O(log(n)), the computing time for n=8192 should be less than 2 times
the computing time for n=4096.
"""
print(notes)
