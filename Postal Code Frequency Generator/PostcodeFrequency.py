#######################################################
#
#   Counting postcode frequency by Aly van D
#
#######################################################

import csv

fields = []
newfields = ["Postcode", "Frequency"]
data = []
dict = {}

f = open('C:/Users/Alysha/Documents/455/csv_latlong_all.csv')
reader = csv.reader(f)

rowcount = 0
for row in reader:
    if rowcount == 0:
        fields = row
    else:
        data.append(row)
    rowcount+=1

f.close()

for x in range(0,rowcount-1):
    if dict.has_key(data[x][16]):
        count = dict.get(data[x][16]) + 1
        dict.update({data[x][16]: count})
    else:
        dict.update({data[x][16]: 1})

with open('C:/Users/Alysha/Documents/455/postcodefrequencies.csv', 'w') as csvfile:
    fieldnames = fields
    writer = csv.DictWriter(csvfile, fieldnames=newfields)
    writer.writeheader()  
    for j in dict.items():
        writer.writerow({ 'Postcode': j[0], 'Frequency' : j[1]})




        
    
