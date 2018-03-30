#######################################################
#
#   Extracting & geocoding most frequent terms per FSA
#   by Aly van D
#
#######################################################

import csv
import numpy as np
import requests as req

fields = []
postcodenames = []
data = []
dict = {}

###### Geocoding op ######
def geocodeOp(pc):
    while True:
        try:
            print("Searching")
            url = "https://maps.googleapis.com/maps/api/geocode/json?address="+pc+" canada"
            print(url)
            response = req.get(url)
            res_json_payload = response.json()
            latitude = res_json_payload['results'][0]['geometry']['location']['lat']
            longitude = res_json_payload['results'][0]['geometry']['location']['lng']
            break;
        except:
            print("Retrying")
    arr = [latitude, longitude]
    return arr


###### MAIN #####

f = open('C:/Users/Alysha/Documents/455/postcodefrequencies.csv')
reader = csv.reader(f)

rowcount = 0
for row in reader:
    if rowcount != 0:
        postcodenames.append(row[0])
    rowcount+=1
f.close()
 
#f = open('C:/Users/Alysha/Documents/455/textmining/textmining_descriptions.csv')
f = open('C:/Users/Alysha/Documents/455/textmining/textmining_titles.csv')
reader = csv.reader(f)

rowcount = 0
for row in reader:
    if rowcount == 0:
        fields = row  
    else:
        data.append(row[1:])
    rowcount+=1
f.close()

print(fields[2:])
freqterms = fields[2:]

for x in range(0,rowcount-1):
    if dict.has_key(data[x][0]):
        a = np.asarray(dict.get(data[x][0]),dtype=int)
        b = np.asarray(data[x][1:],dtype=int)
        sumResult = np.add(a,b)
        s = sumResult.tolist()        
        dict.update({data[x][0]: s})
    else:
        dict.update({data[x][0]: data[x][1:]})

with open('C:/Users/Alysha/Documents/455/textmining/textFrequenciesperFSA.csv', 'w') as csvfile:
    fieldnames = ["Postcode", "MostFrequentTerm", "Count", "Latitude", "Longitude"]
    writer = csv.writer(csvfile, lineterminator='\n')
    writer.writerow(fieldnames)
    for j in dict.items():
       curr = ""
       maxCount = 0
       for k in range(0,len(j[1])):
            if j[1][k] >= maxCount:
                maxCount = j[1][k]
                curr = freqterms[k]
       latlng = geocodeOp(j[0]);
       writer.writerow([j[0], curr, maxCount, latlng[0], latlng[1]])


