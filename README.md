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

**Campaign Geocoder for EDSA**
+ addlatlong_to_gofundmedata.py: Used to add latitude and longitude fields to GoFundMe datasets
+ csv_to_geojson.py: Used to convert GoFundMe entries to geojson for use with Mapbox

**Postal Code Frequency Generator**
+ PostcodeFrequency.py: Used to generate campaign counts for each Forward Sortation Area

**Text Mining Data Pre-Processing**
+ gofundme_feature_extraction.py: Used to select specific features from the gofundmedata (for the purpose of the text-mining method)

**ArcPy - Calculate Percent Area Shared and Compute Weighted Values**
+ working on multithreading this still
+ single_threaded_ada_to_fsa_percent: Used to calculate the percent of area each ADA occupies within each FSA. Example: an ADA with FID 1 comprises 55% of FSA with FID 15. We add 0.55 to the relationship matrix at m[FSA_FID][ADA_FID] to use in adding weighted attribute values we want to compute later.
+ single_threaded_addweights.py: Used to add weighted attribute values based on relationship matrix values previously computed