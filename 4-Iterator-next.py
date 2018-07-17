'''
 Created on Mon Jul 16 2018

 Copyright (c) 2018 Peng Xiao
'''

from __future__ import print_function

# PEP 3114 -- Renaming iterator.next() to iterator.__next__()
# https://www.python.org/dev/peps/pep-3101/


# the different between .next() and __next__()

class A:

    def str(self):
        return 'A'

class B:

    def __str__(self):
        return 'B'

"""
>>> a = A()
>>> b = B()
>>> a.str()
'A'
>>> str(a)
'<__main__.A instance at 0x10cc3d638>'
>>> b.str()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: B instance has no attribute 'str'
>>> str(b)
'B'
>>>
"""

def my_generator():
    for i in range(10):
        yield i

a = my_generator
print(type(a))
# print(a.next())   # for python 2

# print(next(a))    # for python 3


