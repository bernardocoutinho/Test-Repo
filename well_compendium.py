#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 20:47:43 2018

@author: u3h9
"""

import pandas as pd
import re

df =  pd.read_csv('tree.txt')
#df =  pd.read_csv('lista_pocos.txt')

#pocos = df['well'].unique()

lst = df.iloc[:,0].apply(lambda s: s[0:20])

regex=re.compile("\d*/\d\D*\d*")

lst_out = []
for item in list(map(regex.findall,lst)):
    if item:
        lst_out.append(item[0].split('/'))

#print(lst_out)

ano = list(map(lambda s: s[0],lst_out))
poco = list(map(lambda s: s[1],lst_out))

df2 = pd.DataFrame(poco,index=ano,columns=['well'])

ano = list(map(lambda s: s[0],lst_out))
pocos = df2['well'].unique()

print(df2['well'].sort_values().unique())
