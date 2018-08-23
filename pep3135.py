"""
pep3135.py
Created by Peng Xiao on 2018-08-13. xiaoquwl@gmail.com
"""

class Animal:

    def talk(self):
        return 'Sound'


class Cat(Animal):

    def talk(self):
        # parent = Animal.talk(self)
        parent = super().talk()
        return '{} and Purr.'.format(parent)

c = Cat()
print(c.talk())