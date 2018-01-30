#######################################################
#
#   Canadian Hospital Locator by Aly van D
#   1) pulls hospital names from wikipedia
#   2) geocodes hospital locations
#   3) creates geojson containing point data
#
#######################################################

from bs4 import BeautifulSoup

facilities = [] # Array of facilities extracted from Wikipedia list

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

# Geocode hospital locations
def geocode():
    print("Geocoding data...")


# Generate geojson points
def generateGeojson():
    print("Generating geoJson...")


#***** MAIN *****#

#1) pulls hospital names from wikipedia
pullFacilities()
#2) geocodes hospital locations
geocode()
#3) creates geojson containing point data
generateGeojson()

