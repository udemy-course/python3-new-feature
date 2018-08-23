"""
pep448.py
Created by Peng Xiao on 2018-08-12. xiaoquwl@gmail.com
"""

# python 2

dict_one = {'x': 1, 'y': 2, 'z': 3}
dict_two = {'a': 10}
dict_two.update(dict_one)
print(dict_two)

# python 3

dict_one = {'x': 1, 'y': 2, 'z': 3}
dict_two = {'a': 10, **dict_one}
print(dict_two)