# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:36:00 2015

@author: tailajohnston

The purpose of this script is to split our large Collector.csv file into smaller files so that we can read it
"""

from itertools import izip_longest

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

# number of lines per CSV file
n = 300

# Opening and saving files
with open('/Users/tailajohnston/Desktop/collector.csv') as f:
    for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
        with open('/Users/tailajohnston/Desktop/smallerCollectorFiles/small_file_{0}'.format(i * n), 'w') as fout:
            fout.writelines(g)
            
            



