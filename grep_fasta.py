#!/usr/bin/env python3
#Date:25/01/2020
#Author: V A Ramesh
#Purpose: Extract fasta sequences of a Matching "Pattern" and writing to a new file


import sys

f1_fh = open(sys.argv[1])   #Input Multi-Fasta file
f2_fh = open(sys.argv[2])   #Input file with patterns in Fasta headers

f1_lines = [line.strip() for line in f1_fh.readlines()]
f2_lines = [line.strip() for line in f2_fh.readlines()]
f1_fh.close()
f2_fh.close()

data = "demo"
print_line = False
fh_dict = dict()   # Dictionary of File Handles

for fh in f2_lines:
    fh_name = data + "_" + fh + ".fasta"
    fh_dict[fh] = open(fh_name, 'w')

#Key is Pattern, Value is File Handle


def write_fasta(seq, file_pat):
    print(seq, file=fh_dict[file_pat])


for i in f1_lines:
    if (print_line and ">" not in i):
        write_fasta(i, j)
    if (">" in i):
        print_line = False
        for j in f2_lines:
            if (j in i):
                write_fasta(i, j)
                print_line = True
                break


for fh in fh_dict:
    fh_dict[fh].close()


###################
#input_1: Regular Multi-Fasta File
#input_2: Patterns in Headers
# cat ptn_names.txt
# First
# Middle
# Last

# CP_VFs is multifasta_input file

# grep -f ptn_names.txt CP_VFs.faa
# >First R012405 (gi:30260710) BA0552 - internalin, putative First [Bacillus anthracis str. Ames (pXO1- pXO2-)]
# >R012311 (gi:30261922) nheA (BA1887) - enterotoxin Middle  [Bacillus anthracis str. Ames (pXO1- pXO2-)]
# >R012456 Middle  (gi:49478943) BT9727_4954 - hypothetical protein [Bacillus thuringiensis str. 97-27]
# >Last  R015014 (gi:170026132) YPK_3919 - two component transcriptional regulator, LuxR family [Yersinia pseudotuberculosis str. YPIII (serotype O:3)]
