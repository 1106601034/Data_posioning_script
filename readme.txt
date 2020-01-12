---------------------------------
Check list
---------------------------------
___PS_ip.py
___PS_label.py
___PS_packet_size.py
___PS_protocol.py
__edit_all.py
__edit_column.py
__Portmap.csv
__program.py
---------------------------------

---------------------------------
Log
---------------------------------
ver0.3 released at Jan 12, 2020
Support creating new .csv file with at least one data recording
Support avoid error cause by invalid input
---------------------------------
ver0.2 released at Jan 5,2020
User interface
Object-oriented programming
---------------------------------
ver0.1 released at Dec 21,2019
Created and edited
---------------------------------

---------------------------------
Above scripts will not edit original data(___Portmap.csv) directly.
However a backup for data is still recommended.

The program generates .csv file, or reads an existent one. 

If wish to edit an existent file, rename the file as __Portmap.csv.

The result will be saved in a new file names Portmap_posioned.csv

__program.py
The main part of program. Run this file and get start.

___PS_ip.py
randomly generates 4 numbers that equal or larger than 0 and less than 256, then merges numbers as an address.

___PS_protocol.py
changes number base on randomly selection in numbers 0, 6, 17.

___PS_packet_size.py
randomly generates size units no larger than 5kb

___PS_label.py
labels could be 0 or 1