#######################################################
#
#   Canadian Hospital Locator by Aly van D
#   1) pulls hospital names from wikipedia
#   2) geocodes hospital locations
#   3) creates geojson containing point data
#
#######################################################

from bs4 import BeautifulSoup
import csv
import requests as req
import threading

facilities = [] # Array of facilities extracted from Wikipedia list
nestedFacilities = [] # facilities nested for field additions during geocoding fn
facilitiesNotFound = [[],[],[],[]] # facilities not found during geocoding step
numberOfThreads = 4 # Number of threads used to parallelize geocoding fn
workerThreads = [] # thread array
fields = ["Name", "Latitude", "Longitude"] # fields for CSV

# Pull Hospital & Care Centre Names from Wikipedia
def pullFacilities():
    print("Pulling facility names from wiki...")
    url = "https://en.wikipedia.org/wiki/List_of_hospitals_in_Canada"
    
    import urllib.request 
    with urllib.request.urlopen(url) as url:
        html = url.read()
        
    soup = BeautifulSoup(html, "html.parser")
    
    for script in soup(["script", "style"]):
        script.extract()
        
    for x in soup.find_all('h2'):
        province = x.findNext('h2')
        #print(province.getText()[:-6]) # sanity check displaying province name
        city = (x.findNext('ul'))
        for cityhospitals in city.find_all('ul'):
            hospitalnamelist = (cityhospitals.getText()).split('\n')
            for entry in hospitalnamelist:
                if entry not in facilities and entry != '':
                    facilities.append(entry)                   
        #Termination condition to prevent unnecessary reads of page references etc.
        if "References" in province.getText():
            break
    # nest facilities for geocoding
    for i in facilities:
        nestedFacilities.append([i])        

# Geocode operation thread task
def geocodeOp(start,end,threadID):
    for x in range(start,end):
        latitude = 0
        longitude = 0
        try:
            url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + facilities[x].replace(" ", "+")
            response = req.get(url)
            res_json_payload = response.json()
            latitude = res_json_payload['results'][0]['geometry']['location']['lat']
            longitude = res_json_payload['results'][0]['geometry']['location']['lng']
        except:
            # fail case. log the facility not found
            facilitiesNotFound[threadID].append(nestedFacilities[x])
        nestedFacilities[x].append(latitude)
        nestedFacilities[x].append(longitude)
           
# Geocode hospital locations
def geocode():
    print("Geocoding data...")
    divs = int(len(facilities)/numberOfThreads)
    for i in range(0,numberOfThreads):
        t = threading.Thread(target=geocodeOp, args=(i*divs,(i+1)*divs,i,))
        workerThreads.append(t)
    for thread in workerThreads:
        thread.start()
    for thread in workerThreads:
        thread.join()

def writeToCSV(entries):
    print("writing to CSV...")
    with open('C:/Users/Alysha/Documents/455/Canadian_hospitals.csv', 'w') as csvfile:
        fieldnames = fields
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  
        for j in entries:
            print(j)
            writer.writerow({ 'Name': j[0], 'Latitude': j[1],'Longitude': j[2]})

# Generate geojson points
def generateGeojson():
    print("Generating geoJson...")
    csvfields = []
    data = []

    f = open('C:/Users/Alysha/Documents/455/Canadian_hospitals.csv')
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

    geojsonf = open("C:/Users/Alysha/Documents/455/Canadian_hospitals.geojson","w", encoding="utf-8")
    geojsonf.write("{\n\t\"type\":\"FeatureCollection\",")
    geojsonf.write("\n\t\"features\": [")

    for x in range(0,rowcount-1):        
        geojsonf.write("\n\t{")#start feature
        geojsonf.write("\n\t\t\"type\": \"Feature\",")

        #PROPERTIES
        geojsonf.write("\n\t\t\"properties\": {")
        geojsonf.write("\n\t\t\t\"title\": \"")
        geojsonf.write(data[x][0])
        geojsonf.write("\"\n\t\t},")

        #GEOMETRY
        geojsonf.write("\n\t\t\"geometry\": {")
        geojsonf.write("\n\t\t\t\"type\": \"Point\",")
        geojsonf.write("\n\t\t\t\"coordinates\": [")
        geojsonf.write("\n\t\t\t\t")
        geojsonf.write(data[x][1])
        geojsonf.write(",\n\t\t\t\t")
        geojsonf.write(data[x][2])
        geojsonf.write("\n\t\t\t]")    
        geojsonf.write("\n\t\t}")
        
        geojsonf.write("\n\t}")#end feature
        if (x < rowcount-2):
            geojsonf.write(",")

    geojsonf.write("\n\t]")
    geojsonf.write("\n\t\n}")
    geojsonf.close()    

#***** MAIN *****#

#1) pulls hospital names from wikipedia
pullFacilities()

#2) geocodes hospital locations
geocode()
print("Failed cases: ", facilitiesNotFound)
print(len(nestedFacilities)) # sanity check

# write to csv [just in case]
writeToCSV(nestedFacilities)

#3) creates geojson containing point data
generateGeojson()

