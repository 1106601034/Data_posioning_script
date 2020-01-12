#coding=GBK
import random

class ip():
    def __init__(self, name, mask, list):
        self.name = name
        self.mask = mask
        self.list = list

    def base_rule(self):
        if self.mask == 0:
            for item in range(len(self.list)):
                a = str(int(random.uniform(0, 256)))
                b = str(int(random.uniform(0, 256)))
                c = str(int(random.uniform(0, 256)))
                d = str(int(random.uniform(0, 256)))
                x = a + '.' + b + '.' + c + '.' + d
                self.list[item] = x
            return self.list
        else:
            for item in range(len(self.list)):
                x = str(self.list[item])
                y = x
                while x == y:
                    a = str(int(random.uniform(0, 256)))
                    b = str(int(random.uniform(0, 256)))
                    c = str(int(random.uniform(0, 256)))
                    d = str(int(random.uniform(0, 256)))
                    x = a + '.' + b + '.' + c + '.' + d
                self.list[item] = x
            return self.list