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
 
f = open('C:/Users/Alysha/Documents/455/textmining/textmining_descriptions.csv')
#f = open('C:/Users/Alysha/Documents/455/textmining/textmining_titles.csv')
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

with open('C:/Users/Alysha/Documents/455/textmining/textmining_descriptions_perfsa.csv', 'w') as csvfile:
#with open('C:/Users/Alysha/Documents/455/textmining/textmining_titles_perfsa.csv', 'w') as csvfile:    
    fieldnames = ["Postcode", "MostFrequentTerm1","MostFrequentTerm2","MostFrequentTerm3", "Count1","Count2","Count3", "Latitude", "Longitude"]
    writer = csv.writer(csvfile, lineterminator='\n')
    writer.writerow(fieldnames)
    for j in dict.items():
       freq1 = "NA"
       freq2 = "NA"
       freq3 = "NA"
       maxCount1 = 0
       maxCount2 = 0
       maxCount3 = 0
       for k in range(0,len(j[1])):
            if j[1][k] > maxCount1:
                maxCount1 = j[1][k]
                freq1 = freqterms[k]
            elif j[1][k] > maxCount2:
                maxCount2 = j[1][k]
                freq2 = freqterms[k]
            elif j[1][k] > maxCount3:
                maxCount3 = j[1][k]
                freq3 = freqterms[k]

       latlng = geocodeOp(j[0])
       writer.writerow([j[0], freq1, freq2, freq3,maxCount1,maxCount2,maxCount3, latlng[0], latlng[1]])


