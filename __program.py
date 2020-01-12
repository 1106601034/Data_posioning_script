# coding=GBK
import time
import pandas as pd
from __edit_all import edit_all
from __edit_column import edit_column

menu = {
    1: ' Source IP',
    2: ' Destination IP',
    3: ' Average Packet Size',
    4: ' Protocol',
    5: ' Label',
    6: ' exit'
}

def interface(when):
    print('#############################')
    if when:
        print('-----------Welcome-----------')
    print('---1-generate-new-file-------')
    print('---2-rewrite-existent-file---')
    print('---6-exit--------------------')
    print('#############################')
    selection = 0
    seed = [1,2,6]
    while selection not in seed:
        try:
            selection = int(input('select an action: '))
        except ValueError:
            print('Invaild command.')
        else:
            if selection == 1:
                selection = 0
                return selection
            if selection == 2:
                print('#############################')
                print('---1-rewrite-source-ip-------')
                print('---2-rewrite-destination-ip--')
                print('---3-rewrite-packet-size-----')
                print('---4-rewrite-protocol--------')
                print('---5-rewrite-label-----------')
                print('---6-exit--------------------')
                print('#############################')
                selection = 0
                while selection not in menu.keys():
                    try:
                        selection = int(input('select an action: '))
                    except ValueError:
                        print('Invaild command.')
                    if selection in menu.keys():
                        return selection
                    else:
                        print('Invaild command')
            if selection == 6:
                return selection
            else :
                print('Invaild command')

def read_csv():
    try:
        reader = pd.read_csv('__Portmap.csv', encoding='GBK', low_memory=False)
    except FileNotFoundError:
        print('File __Portmap.csv was not found')
    else:
        return reader

def execution(mask):
    if mask == 0:
        length = 0
        while length < 1:
            try:
                length = int(input('Type the number of row (not includes header): '))
            except ValueError:
                print('Invaild command.')
            if length < 1:
                print('Should have at least one row')
        new_list = edit_all(menu, mask, length)
    else:
        data = read_csv()
        new_list = edit_column(menu, mask, data)
    data_r = new_list.pepare()
    data_rp = new_list.execute(data_r)
    data_rpe = new_list.generate(data_rp)
    create_csv(data_rpe)

def create_csv(writer):
    writer.to_csv('Portmap_posioned.csv', index=False)

def main():
    selection = interface(True)
    while (1):
        if selection == 6:
            return 0
        else:
            start = time.time()
            execution(selection)
            end = time.time()
            print('data was saved in file Portmap_posioned.csv')
            print('*****spent', round(end - start, 2), 'seconds*****')
            print('*********Successful**********')
            selection = interface(False)
main()