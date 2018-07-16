'''
 Created on Mon Jul 16 2018

 Copyright (c) 2018 Peng Xiao
'''

# Changing the Division Operator
# https://www.python.org/dev/peps/pep-0238/

"""
Python 2.7.10 (default, Oct  6 2017, 22:29:07)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 / 3
0
>>> 1 / 3.0
0.3333333333333333
>>>
>>>
>>> 7 / 2
3
>>>

"""

"""
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> 1 / 3
0.3333333333333333
>>> 1 / 3.0
0.3333333333333333
>>>
>>> 1 // 3
0
>>> 3 / 7
0.42857142857142855
>>> 7 / 2
3.5
>>>
>>> 1 / 7
0.14285714285714285
>>>
>>>
>>> 7 / 1
7.0
>>> 7 // 1
7
>>> 1 // 7
0
"""