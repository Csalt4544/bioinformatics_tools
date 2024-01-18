#!/usr/bin/env python3

# imported sys to process command line arguments typed after .py file name
# I searched 'wrap' within the Python documentation and found the module textwrap

import sys
import textwrap

# any variables needed outside the loop are initialized here
# decided to use a similar memory system here after working on problem #6

mem_list = []
sequence_mem = ('')
within_FASTA = False
within_chromosome = False
chromosome_num = ('')
arguments = []
sense_seq = []

# list generated from command line arguments are processed below using the .split method

file_name = sys.argv[1].split('=')
type = sys.argv[2].split('=')
attribute = sys.argv[3].split('=')
value = sys.argv[4].split('=')

# for loop to iterate through the .gff file
# similar set up at the beginning to the .gff lecture example
# used .strip() to remove any whitespaces and carriage returns
# .split('\t') used on tab-delimited spacing on the first portion of .gff file

for line in open(file_name[1]):
    line = line.strip()
    columns = line.split('\t')
    num_start_site = 0
    num_stop_site = 0

    # if conditional used to check if within_FASTA and within_chromosome are true
    # line is added to string variable initiated above
    # if not, then line is passed and not added to sequence

    if within_FASTA == (True) and within_chromosome == (True):
        sequence_mem = sequence_mem + line
    else:
        pass

    # similar set-up to the .gff parsing lecture to recognize start of FASTA section
    # also added a variation that recognize start of specific chromosome

    if line.startswith('##FASTA'):
        within_FASTA = True

    if line.startswith('>{0}'.format(chromosome_num)):
        within_chromosome = True

    # if not within the FASTA section of the file, searches for command line arguments
    # passes the commentary and description of the file at the beginning
    # two .splits() are used to process the column 9 attributes
    # once line has matches in specific columns to the command line arguments,
    # any important information is stored in memory lists (arguments and mem_list)
    # start and stop site subtract one to account for difference in counting base pairs vs. lists

    if line.startswith('#'):
        pass
    elif len(columns) == 9:
        section_9_cols = columns[8].split(';')
        first_field = section_9_cols[0].split('=')
        if columns[2] == (type[1]) and first_field[0] == (attribute[1]) and first_field[1] == (value[1]):
            arguments.append(columns[2])
            arguments.append(first_field[0])
            arguments.append(first_field[1])
            start_site = (columns[3])
            stop_site = (columns[4])
            strand_sense = columns[6]
            chromosome_num = columns[0]
            num_start_site = (int(start_site) - 1)
            num_stop_site = (int(stop_site) - 1)
            mem_list.append(num_start_site)
            mem_list.append(num_stop_site)
            mem_list.append(strand_sense)

# after for loop, if/elif conditional used to check sense stored in mem_list
# if sense is minus, string is reversed using class slice from problem #4
# otherwise both sections extract substring at specified start and stop sites
# processed string is stored in sense_seq memory list
# if arguments match and there are no missing values or multiple matches, header is printed
# FASTA sequence uses textwrap module mentioned earlier to limit line width to 60 character limit
# if missing an argument, Python will produce an IndexError

if arguments[0] == (type[1]) and arguments[1] == (attribute[1]) and arguments[2] == (value[1]):
    if mem_list[2] == ('+') or mem_list[2] == ('.') or mem_list[2] == ('?'):
        parsed_sequence = sequence_mem[mem_list[0]:mem_list[1]]
        sense_seq.append(parsed_sequence)
        print('>{0}:{1}:{2}'.format(type[1], attribute[1], value[1]))
        print(textwrap.fill(sense_seq[0], 60))
    else:
        reverse_seq = (sequence_mem)[::-1]
        reverse_parsed_sequence = (reverse_seq[mem_list[0]:mem_list[1]])
        sense_seq.append(reverse_parsed_sequence)
        format_style = textwrap.fill(sense_seq[0], 60)
        print(format_style)
else:
    print('Error, one or more arguments repeats found in file.')
