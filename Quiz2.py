from __future__ import division, print_function
import time
from numpy import linspace, sqrt
from math import pi
start=time.perf_counter()
N = 100
h = 2/N
x = linspace(-1,1,N)
y = sqrt(1 - x**2)

TotalValue = h*sum(y)*2
end=time.perf_counter()

difference = I - pi
print('The value of integral is = {}'.format(TotalValue))
print('The difference of the rule and actual value is = {}'.format(difference))
print(end-start)
