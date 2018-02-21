# CrowdfundingDataProject
Created for Geog 455W Spring 2018

This repository contains scripts and other files I write to be shared with team members for the Geog 455W course offering in Spring 2018.

# Setup

run the following installations:

1) pip install beautifulsoup4

# Descriptions

The following are standalone scripts written for the purpose of the Geog 455W Medical Crowdfunding Project in Spring 2018.

1) CanadianHospitalLocator.py: Used to create a list of Canadian hospitals, geocode entries, and create a geojson containing these points in preparation for use with mapbox
2) addlatlong_to_gofundmedata.py: Used to add latitude and longitude fields to GoFundMe datasets
3) csv_to_geojson.py: Used to convert GoFundMe entries to geojson for use with Mapbox
4) PostcodeFrequency.py: Used to generate campaign counts for each Forward Sortation Area
5) gofundme_feature_extraction.py: Used to select specific features from the gofundmedata (for the purpose of the text-mining method)