#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Append column as an AGN flag
    @author:  Maria Luiza L. Dantas
    @date:    2015.23.10
    @version: 0.0.1
    This program appends a new column to a csv file.
"""
import numpy as np
import csv

# ======================================================================================================================
# Main thread
if __name__ == '__main__':

    data = np.loadtxt('/home/mdastro/Documentos/CPR02_LOGIT_AGN/sample_CRP02_sub.csv', delimiter=',',  dtype=str)

    first_column = data[1:, 0].astype(long)
    lines        = data[:, :].astype(str)
    columns      = data[:, :].astype(str)

    dictionary = {}
    for i in range(len(data[0, :])):                             # Converting numpy array into dictionary
        dictionary[data[0, i]] = np.array(data[0 + 1:, i], dtype=str)

    flag_bar    = dictionary['t03_bar_a06_bar_flag']
    flag_no_bar = dictionary['t03_bar_a07_no_bar_flag']

    column = ['bar_presence']
    for i in range(first_column.size):
        if flag_bar[i] == str(1):
            column.append('1')                                     # With bar (t03_bar_a06_bar_flag = -1)
        elif flag_no_bar[i] == str(1):
            column.append('0')
        else:
            column.append('NA')
    column = np.array(column, dtype=str)

    input_file  = open('/home/mdastro/Documentos/CPR02_LOGIT_AGN/sample_CRP02_sub.csv')
    reader_file = csv.reader(input_file)

    with open('output.txt', 'w') as file_out:
        with input_file as in_file:
            i = 0
            for line in in_file:
                s = ''
                s = line.replace('\n', '') + ',' + column[i] + '\n'
                i+=1
                file_out.write(s)


__author__ = 'mdastro'
