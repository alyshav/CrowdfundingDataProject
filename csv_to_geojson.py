#######################################################
#
#   csv to geoJson parser by Aly van D
#   used to convert crowdfunding csv to geoJson
#
#######################################################

import csv

fields = []
data = []

f = open('C:/Users/Alysha/Documents/455/csv_latlong_50entries.csv', encoding="utf8")
reader = csv.reader(f)

rowcount = 0
for row in reader:
    if rowcount == 0:
        fields = row
    else:
        data.append(row)
    rowcount+=1

f.close()

print(data[0])

geojsonf = open("C:/Users/Alysha/Documents/455/geojson_50records.geojson","w", encoding="utf-8")
geojsonf.write("{\n\t\"type\":\"FeatureCollection\",")
geojsonf.write("\n\t\"features\": [")

for x in range(0,rowcount-1):        
    geojsonf.write("\n\t{")#start feature
    geojsonf.write("\n\t\t\"type\": \"Feature\",")

    #PROPERTIES
    geojsonf.write("\n\t\t\"properties\": {")
    geojsonf.write("\n\t\t\t\"title\": \"")
    geojsonf.write(data[x][0])
    #geojsonf.write("\",\n\t\t\t\"description\": \"")
    #geojsonf.write(data[x][12])
    geojsonf.write("\",\n\t\t\t\"marker-color\": \"")
    geojsonf.write(data[x][8])
    geojsonf.write("\",\n\t\t\t\"location\": \"")
    geojsonf.write(data[x][17])
    geojsonf.write("\"\n\t\t},")

    #GEOMETRY
    geojsonf.write("\n\t\t\"geometry\": {")
    geojsonf.write("\n\t\t\t\"type\": \"Point\",")
    geojsonf.write("\n\t\t\t\"coordinates\": [")
    geojsonf.write("\n\t\t\t\t")
    geojsonf.write(data[x][19])
    geojsonf.write(",\n\t\t\t\t")
    geojsonf.write(data[x][18])
    geojsonf.write("\n\t\t\t]")    
    geojsonf.write("\n\t\t}")
    
    geojsonf.write("\n\t}")#end feature
    if (x < rowcount-2):
        geojsonf.write(",")

geojsonf.write("\n\t]\n\t\n}")
geojsonf.close()
