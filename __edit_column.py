# coding=GBK
import pandas as pd
from ___PS_ip import ip
from ___PS_packet_size import packet_size
from ___PS_protocol import protocol
from ___PS_label import label

class edit_column():
    def __init__(self, menu, mask, reader):
        self.menu = menu
        self.mask = mask
        self.reader = reader

    def pepare(self):
        to_change_list = []
        to_change = self.reader[self.menu[self.mask]]
        for row in to_change:
            to_change_list.append(row)
        return to_change_list

    def execute(self, the_list):
        if self.mask == 1:
            new_list = ip(self.menu[self.mask], self.mask, the_list)
            new_list.base_rule()
            return new_list.list
        if self.mask == 2:
            new_list = ip(self.menu[self.mask], self.mask, the_list)
            new_list.base_rule()
            return new_list.list
        if self.mask == 3:
            new_list = packet_size(self.menu[self.mask], self.mask, the_list)
            new_list.base_rule()
            return new_list.list
        if self.mask == 4:
            new_list = protocol(self.menu[self.mask], self.mask, the_list)
            new_list.base_rule()
            return new_list.list
        if self.mask == 5:
            new_list = label(self.menu[self.mask], self.mask, the_list)
            new_list.base_rule()
            return new_list.list

    def generate(self, changed):
        writer = pd.DataFrame()
        n = [1, 2, 3, 4, 5]
        for each in n:
            writer[self.menu[each]] = self.reader[self.menu[(each)]]
            if each == self.mask:
                writer[self.menu[self.mask]] = changed
        return writer
