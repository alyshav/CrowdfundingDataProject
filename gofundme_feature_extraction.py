#######################################################
#
#   Extracting fields from GoFundMeData by Aly van D
#   Selecting only relevant fields to run tm method
#
#######################################################

import csv

fields = []
data = []
numberOfRecords = 1808

###### MAIN #####
    
f = open('C:/Users/Alysha/Documents/455/2016gofundmefull2.csv')
reader = csv.reader(f)

rowcount = 0
for row in reader:
    if rowcount != 0:
        data.append(row)
    rowcount+=1
f.close()

with open('C:/Users/Alysha/Documents/455/csv_descriptions.csv', 'w') as csvfile:
    fieldnames = ['Title', 'Message_Content', 'Location_Postal']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    for j in range(0,rowcount-1):
        writer.writerow({ 'Title': data[j][0], 'Message_Content': data[j][12].replace('\n', ' '), 'Location_Postal': data[j][16]})
