# CrowdfundingDataProject
Created for Geog 455W Spring 2018

This repository contains scripts and other files I write to be shared with team members for the Geog 455W course offering in Spring 2018.

# Setup

run the following installations:

1) pip install beautifulsoup4

# Descriptions

The following are standalone scripts written for various purposes within the Geog 455W Medical Crowdfunding Project developed in Spring 2018.

**Canadian Hospital Dataset Creation & Geocoding**
+ CanadianHospitalLocator.py: Used to create a list of Canadian hospitals, geocode entries, and create a geojson containing these points in preparation for use with mapbox

**Campaign Geocoder for ESDA**
+ addlatlong_to_gofundmedata.py: Used to add latitude and longitude fields to GoFundMe datasets
+ csv_to_geojson.py: Used to convert GoFundMe entries to geojson for use with Mapbox

**Postal Code Frequency Generator**
+ PostcodeFrequency.py: Used to generate campaign counts for each Forward Sortation Area

**Text Mining Data Pre-Processing**
+ gofundme_feature_extraction.py: Used to select specific features from the gofundmedata (for the purpose of the text-mining method)

**Computing weighted census data for FSAs**
+ https://github.com/alyshav/ArcPy-Calculate-Percent-Area-Shared-and-Compute-Weighted-Values 