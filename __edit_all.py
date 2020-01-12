# coding=GBK

import pandas as pd
from ___PS_ip import ip
from ___PS_packet_size import packet_size
from ___PS_protocol import protocol
from ___PS_label import label

class edit_all():
    def __init__(self, menu, mask, length):
        self.menu = menu
        self.mask = mask
        self.length = length

    def pepare(self):
        n = [1, 2, 3, 4, 5]
        table = []
        for each in n:
            i = 0
            list = []
            while i < self.length:
                list.append(0)
                i = i + 1
            table.append(list)
        return table

    def execute(self, the_list):
        list = []
        new_list = ip(self.menu[1], self.mask, the_list[0])
        new_list.base_rule()
        list.append(new_list.list)
        new_list = ip(self.menu[2], self.mask, the_list[1])
        new_list.base_rule()
        list.append(new_list.list)
        new_list = packet_size(self.menu[3], self.mask, the_list[2])
        new_list.base_rule()
        list.append(new_list.list)
        new_list = protocol(self.menu[4], self.mask, the_list[3])
        new_list.base_rule()
        list.append(new_list.list)
        new_list = label(self.menu[5], self.mask, the_list[4])
        new_list.base_rule()
        list.append(new_list.list)
        return list

    def generate(self, list):
        writer = pd.DataFrame()
        n = [1, 2, 3, 4, 5]
        for each in n:
            writer[self.menu[each]] = list[each - 1]
        return writer