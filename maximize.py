#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:14:45 2023

@author: winniemak
"""

import math
from itertools import product

# read input
n, k = map(int, input().split())

#Initialize lists

lists = []


for i in range(n):
    row = list(map(int, input().split()))
    row.pop(0)
    lists.append(list(map(lambda x:x**2, row)))
    #print(lists)

print(max(map(lambda x: sum(x)%k,product(*lists))))