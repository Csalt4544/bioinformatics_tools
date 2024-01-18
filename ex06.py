#!/usr/bin/env python3

import re

# initialize variables/lists outside of for loop
# prevents resetting when not desired

start = True
alignment_count = 0
mem_list = []

# for loop to iterate through each line of the text

for line in open('example_blast.txt'):
    line = line.strip()

    # first two if statements with regex checks only the beginning portion of file

    if re.search('Sequences', line):
        start = False

    elif start == True:
        if re.search('Query=', line):
            query_ID = re.split(r'[=\s]', line)
            print('Query ID: {0}'.format(query_ID[2]))
        elif re.search('Length=', line):
            query_length = re.split(r'[=]', line)
            print('Query Length: {0}'.format(query_length[1]))

    # once start == False, program begins checking rest of file
    # nested if statements with regex parse out lines containing accession, length, and score
    # split regex to parse this information out, and saved to 'temporary' mem_list
    # after program prints the string containing information, mem_list contents are deleted for next line
    # each new increases the alignment_count, after it reaches 11 the if statement uses break to stop

    if start == False:
        if alignment_count == 11:
            break
        elif re.search('>', line):
            alignment_count += 1
            group_1 = re.split(r'[\s]', line)
            mem_list.append(group_1[0])
        elif re.search('Length', line):
            group_2 = re.split(r'[=]', line)
            mem_list.append(group_2[0])
            mem_list.append(group_2[1])
        elif re.search('Score', line):
            group_3 = re.split(r'[\s(,]', line)
            mem_list.append(group_3[0])
            mem_list.append(group_3[4])
            if mem_list[4] == ('bits'):
                del mem_list[4]
                mem_list.append(group_3[3])
            print('Alignment #{0}: Accession Number = {1} ({2} = {3}, {4} = {5})'
                  .format(alignment_count, mem_list[0], mem_list[1],
                          mem_list[2], mem_list[3], mem_list[4]))
            del mem_list[4]
            del mem_list[3]
            del mem_list[2]
            del mem_list[1]
            del mem_list[0]
