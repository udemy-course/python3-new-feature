'''
 Created on Mon Jul 16 2018

 Copyright (c) 2018 Peng Xiao
'''

# PEP 237 -- Unifying Long Integers and Integers
# https://www.python.org/dev/peps/pep-0237/

"""
python 2

>>> import sys
>>> a = sys.maxint
>>> type(a)
<type 'int'>
>>> b = a + 1
>>> b
9223372036854775808L
>>> type(b)
<type 'long'>
>>>

"""


"""
python 3

>>> import sys
>>> a = sys.maxsize
>>> a
9223372036854775807
>>> type(a)
<class 'int'>
>>> b = a + 1
>>> b
9223372036854775808
>>> type(b)
<class 'int'>
>>>

"""