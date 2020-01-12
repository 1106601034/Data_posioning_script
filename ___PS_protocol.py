#coding=GBK
import random

class protocol():
    def __init__(self, name, mask, list):
        self.name = name
        self.mask = mask
        self.list = list

    def base_rule(self):
        seed = [0,6,17]
        if self.mask == 0:
            for item in range(len(self.list)):
                x = random.choice(seed)
                self.list[item] = x
            return self.list
        else:
            for item in range(len(self.list)):
                x = int(self.list[item])
                y = x
                while x == y:
                    x = random.choice(seed)
                self.list[item] = x
            return self.list
