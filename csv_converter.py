#!/usr/bin/python3

# Library modules are imported: sys to process command line arguments, csv to convert to .csv format

import sys
import csv

# System arguments are held within the sys.argv array
# Hardcoded category strings in array as .sop files originally do not contain these (needed for Tableau)

unconverted_file = sys.argv[1]
converted_file = sys.argv[2]
title_array = ["ReadName",
               "ReadLength",
               "E-Value",
               "AlignmentLength",
               "AlignBegin",
               "AlignEnd",
               "Strand",
               "Identity",
               "ReferenceSequenceName",
               "ReferenceSequenceBegin",
               "ReferenceSequenceEnd"]

# Open unconverted file path name from sys.argv as file
# Create new csv.writer with defined parameters
# .writerow() used to write first row with column titles
# Each line is .split() and converted to necessary data types to be held in a list
# List contents are written to the output file using .writerow()


with open(unconverted_file, 'r', newline='') as file:

    writer = csv.writer(open(converted_file, 'w', newline=''),
                        delimiter=',',
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)

    writer.writerow(title_array)

    for line in file:
        split_line = line.split('\t')

        seq_ID = split_line[0]
        seq_len = split_line[1]
        e_value = split_line[2]
        align_len = split_line[3]
        seq_strand_start = int(split_line[4])
        seq_strand_stop = int(split_line[5])
        seq_strand_sense = (split_line[6])
        percent_match = split_line[7]
        accession_num = split_line[8]
        ref_seq_start = int(split_line[9])
        ref_seq_stop = int(split_line[10])

        percent_match_split = percent_match.split('%')
        percent_match_int = float(percent_match_split[0])

        data_list = [seq_ID,
                      seq_len,
                      e_value,
                      align_len,
                      seq_strand_start,
                      seq_strand_stop,
                      seq_strand_sense,
                      percent_match_int,
                      accession_num,
                      ref_seq_start,
                      ref_seq_stop]

        writer.writerow(data_list)

# file.close() at the end to close the .open() file

file.close()
