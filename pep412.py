"""
pep412.py
Created by Peng Xiao on 2018-08-10. xiaoquwl@gmail.com
"""
import time

class Foo:

    def __init__(self, a, b):
        self.a = a
        self.b = b


if __name__ == "__main__":

    n = 1000000
    i = 0
    result = []
    while i < n:
        result.append(Foo(1,2))
        i += 1
    while True:
        time.sleep(4)
