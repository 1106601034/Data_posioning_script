#coding=GBK
import random

class label():
    def __init__(self, name, mask, list):
        self.name = name
        self.mask = mask
        self.list = list

    def base_rule(self):
        if self.mask == 0:
            seed = [0,1]
            for item in range(len(self.list)):
                self.list[item] = random.choice(seed)
            return self.list
        else:
            for item in range(len(self.list)):
                if self.list[item] == 1:
                    self.list[item] = 0
                else:
                    self.list[item] = 1
            return self.list
