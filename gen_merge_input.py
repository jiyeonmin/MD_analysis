#!/usr/bin/env python

with open('tmp.txt','w') as fout:
    for i in range(1200):
        fout.write('trajin step5_%d.nc 1 last 100\n'%(i+1))
        
