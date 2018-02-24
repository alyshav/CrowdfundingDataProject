#######################################################
#
#   Multi-threaded GoFundMe data parser by Aly van D
#   Adds lat/long based on location field to csv
#
#######################################################

import csv
import requests as req
import threading

fields = []
data = []
workerThreads = []
numberOfThreads = 4
numberOfRecords = 1808
rowDivs = int(numberOfRecords/numberOfThreads)

###### THREAD TASK #####

def geocodeOp(start,end):
    for x in range(start,end):
        while True:
            try:
                print("Searching")
                url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + data[x][17].replace(" ", "")
                print(url)
                response = req.get(url)
                res_json_payload = response.json()
                latitude = res_json_payload['results'][0]['geometry']['location']['lat']
                longitude = res_json_payload['results'][0]['geometry']['location']['lng']
                break;
            except:
                print("Retrying")
        data[x].append(latitude)
        data[x].append(longitude)

###### MAIN #####
    
f = open('C:/Users/Alysha/Documents/455/2016gofundmefull2.csv')
reader = csv.reader(f)

rowcount = 0
for row in reader:
    if rowcount == 0:
        fields = row
    else:
        data.append(row)
    rowcount+=1

f.close()

fields.append('Latitude')
fields.append('Longitude')

for i in range(0,numberOfThreads):
    t = threading.Thread(target=geocodeOp, args=(i*rowDivs,(i+1)*rowDivs,))
    workerThreads.append(t)

for thread in workerThreads:
    thread.start()
for thread in workerThreads:
    thread.join()

with open('C:/Users/Alysha/Documents/455/csv_latlong_all.csv', 'w') as csvfile:
    fieldnames = fields
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  
    for j in range(0,rowcount-1):
        writer.writerow({ 'Title': data[j][0], 'URL' : data[j][1],'Category' : data[j][2], 'Raised_Current': data[j][3], 'Raised_Goal': data[j][4], 'Raised_Number of Donations': data[j][5],'Photo_Number of Favoriates': data[j][6],'Share': data[j][7],'Color Theme': data[j][8],'Created by_Date': data[j][9],'Created by_Name': data[j][10],'Created by_Number of Facebook Friends': data[j][11],'Message_Content': data[j][12],'Crawling Date': data[j][13],'Number of Comments': data[j][14],'Location_Country': data[j][15],'Location_Postal': data[j][16],'Location_Description': data[j][17],'Latitude': data[j][18],'Longitude': data[j][19]})
