#!/usr/bin/python3

# regex is imported for .search() function

import re

# a similar approach to question 1 is taken for question 2
# if a line starts with "residue"
# line is stripped and split using appropriate functions


for line in open("angles_degrees.txt"):
    if re.search("Residue", line):
        line = line.strip()
        columns = re.split(r"[\s\(\),]", line)
        if re.search("GLY", columns[1]):
            if (-150 < float(columns[3]) < -45) and (-80 < float(columns[5]) < 70):
                print("{0} {1} alpha".format(columns[0], columns[1]))
            elif (-180 < float(columns[3]) < -30) and (100 < float(columns[5]) < 180):
                print("{0} {1} beta".format(columns[0], columns[1]))
            else:
                print("{0} {1} other".format(columns[0], columns[1]))
        elif re.search("PRO", columns[1]):
            if (-90 < float(columns[3]) < -45) and (-70 < float(columns[5]) < 10):
                print("{0} {1} alpha".format(columns[0], columns[1]))
            elif (-90 < float(columns[3]) < -30) and (100 < float(columns[5]) < 180):
                print("{0} {1} beta".format(columns[0], columns[1]))
            else:
                print("{0} {1} other".format(columns[0], columns[1]))
        #elif re.search("PRO", next(columns[1])):
            #print("Pre-proline residue found")
        else:
            if ((-100 < float(columns[3]) < -48) and (-50 < float(columns[5]) < 60)) or \
            ((40 < float(columns[3]) < 80) and (0 < float(columns[5]) < 100)):
                print("{0} {1} alpha".format(columns[0], columns[1]))
            elif (-110 < float(columns[3]) < -60) and (110 < float(columns[5]) < 170):
                print("{0} {1} beta".format(columns[0], columns[1]))
            else:
                print("{0} {1} other".format(columns[0], columns[1]))
    else:
        print(line)
