#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 20:47:43 2018

@author: u3h9
"""

import pandas as pd
import os

df =  pd.read_csv('lista_pocos.txt')

pocos = df['well'].unique()

for dir in pocos:
    for subdir1 in ('RiDat','txt'):
        for subdir2 in ('Sw1','Swi'):
            os.makedirs(os.path.join(dir, 'decay',subdir1, subdir2))

