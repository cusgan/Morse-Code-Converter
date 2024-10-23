#This program converts CSV file to Python dictionary.

import json

f = open('state_table.csv','r')
lines = f.readlines()
state_tbl = dict()

for line in lines:
    line = line.split(',')
    line[2] = line[2].strip()
    state_tbl.update({line[0] : [line[1], line[2]]})
    # print(line)
    
print(json.dumps(state_tbl,indent=4))