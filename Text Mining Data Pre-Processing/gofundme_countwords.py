#######################################################
#
#   Finding most frequent terms per FSA by Aly van D
#   Using frequent terms found to extract the most common
#   terms per FSA
#
#######################################################

import csv
import numpy as np

fields = []
postcodenames = []
data = []
numberOfRecords = 1808
dict = {}

###### MAIN #####

f = open('C:/Users/Alysha/Documents/455/postcodefrequencies.csv')
reader = csv.reader(f)

rowcount = 0
for row in reader:
    if rowcount != 0:
        postcodenames.append(row[0])
    rowcount+=1
f.close()
 
f = open('C:/Users/Alysha/Documents/455/textmining/textmining_descriptions.csv')
reader = csv.reader(f)

rowcount = 0
for row in reader:
    if rowcount == 0:
        fields = row  
    else:
        #print(row[1])
        data.append(row[1:])
    rowcount+=1
f.close()
#print(data[0])

#dict.update({postcodenames[16]: data[0][1:]})
#print(dict)

print(fields[1:])

#for x in range(0,rowcount-1):
for x in range(0,rowcount-1):
    if dict.has_key(data[x][0]):
        a = np.asarray(dict.get(data[x][0]),dtype=int)
        b = np.asarray(data[x][1:],dtype=int)
        sumResult = np.add(a,b)
        s = sumResult.tolist()        
        #print(s)
        dict.update({data[x][0]: s})
    else:
        dict.update({data[x][0]: data[x][1:]})
#print(dict)

# finish this:
with open('C:/Users/Alysha/Documents/455/textFrequenciesperFSA.csv', 'w') as csvfile:
    fieldnames = fields[1:]
    writer = csv.writer(csvfile, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    for j in dict.items():
       newStr = str(fieldnames[0]): j[0]
       for i in len(fieldnames-1):
           print(i)
       writer.writerow(j)


