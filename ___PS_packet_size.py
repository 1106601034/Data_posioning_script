#coding=GBK
import random

class packet_size():
    def __init__(self, name, mask, list):
        self.name = name
        self.mask = mask
        self.list = list

    def base_rule(self):
        if self.mask == 0:
            for item in range(len(self.list)):
                x = str(int(random.uniform(0, 5120)))
                self.list[item] = str(x + ' bytes')
            return self.list
        else:
            for item in range(len(self.list)):
                x = int(self.list[item])
                y = x
                while x == y:
                   x = str(int(random.uniform(0, 5120)))
                self.list[item] = str(x + ' bytes')
            return self.list