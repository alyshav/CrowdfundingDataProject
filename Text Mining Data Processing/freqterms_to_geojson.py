#######################################################
#
#   Freq terms to geojson by Aly van D
#
#######################################################

import csv

print("Generating geoJson...")
csvfields = []
data = []

#f = open('C:/Users/Alysha/Documents/455/textmining/textmining_titles_perfsa.csv')
f = open('C:/Users/Alysha/Documents/455/textmining/textmining_descriptions_perfsa.csv')
reader = csv.reader(f)

rowcount = 0
for row in reader:
    if rowcount == 0:
        csvfields = row
    else:
        data.append(row)
    rowcount+=1

f.close()

print(data[0])

#geojsonf = open("C:/Users/Alysha/Documents/455/textmining/freq_titles.geojson","w")
geojsonf = open("C:/Users/Alysha/Documents/455/textmining/freq_descriptions.geojson","w")
geojsonf.write("{\n\t\"type\":\"FeatureCollection\",")
geojsonf.write("\n\t\"features\": [")

for x in range(0,rowcount-1):        
    geojsonf.write("\n\t{")#start feature
    geojsonf.write("\n\t\t\"type\": \"Feature\",")

    #PROPERTIES
    geojsonf.write("\n\t\t\"properties\": {")
    geojsonf.write("\n\t\t\t\"postcode\": \"")
    geojsonf.write(data[x][0])
    geojsonf.write("\",\n\t\t\t\"term1\": \"")
    geojsonf.write(data[x][1])
    geojsonf.write("\",\n\t\t\t\"term2\": \"")
    geojsonf.write(data[x][2])
    geojsonf.write("\",\n\t\t\t\"term3\": \"")
    geojsonf.write(data[x][3])    
    geojsonf.write("\",\n\t\t\t\"count1\": \"")
    geojsonf.write(data[x][4])
    geojsonf.write("\",\n\t\t\t\"count2\": \"")
    geojsonf.write(data[x][5])
    geojsonf.write("\",\n\t\t\t\"count3\": \"")
    geojsonf.write(data[x][6])    
    geojsonf.write("\"\n\t\t},")     

    #GEOMETRY
    geojsonf.write("\n\t\t\"geometry\": {")
    geojsonf.write("\n\t\t\t\"type\": \"Point\",")
    geojsonf.write("\n\t\t\t\"coordinates\": [")
    geojsonf.write("\n\t\t\t\t")
    geojsonf.write(data[x][8])
    geojsonf.write(",\n\t\t\t\t")
    geojsonf.write(data[x][7])
    geojsonf.write("\n\t\t\t]")    
    geojsonf.write("\n\t\t}")
    
    geojsonf.write("\n\t}")#end feature
    if (x < rowcount-2):
        geojsonf.write(",")

geojsonf.write("\n\t]")
geojsonf.write("\n\t\n}")
geojsonf.close()    
