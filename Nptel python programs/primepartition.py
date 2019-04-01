'''
A positive integer m can be partitioned as primes if it can be written as p + q where p > 0, q > 0 and both p and q are prime numbers.

Write a Python function primepartition(m) that takes an integer m as input and returns True if m can be partitioned as primes and False otherwise. (If m is not positive, your function should return False.)

Here are some examples of how your function should work.

>>> primepartition(7)
True

>>> primepartition(185)
False

>>> primepartition(3432)
True
'''

#Program

from math import *
def primepartition(m):
  if m <= 0:
    return False
  else:
    for i in range(2, m//2):
      l, h = i, m-i
      flag = 0
      for j in range(2, int(sqrt(h)+1)):
        if (j <= int(sqrt(l))) and (l%j == 0):
          flag = 1
          break
        if (h%j == 0):
          flag = 1
          break
      if flag == 0:
        return True
  return False
