# CS540_Project_Airport
Provides all material required to determine the distance to the nearest airport for all parcels in Volusia County. 

PROJECT OBJECTIVE:

The purpose of this project was to determine the distance in miles from all parcels in Volusia County (VC) to it's nearest airport. 

PROCESS:
1. Each individual parcel was identified using its parcel id from the volusia.parcel table. 
2. Airports can be identified using the land use code (LUC) of '2000'. This information was sourced from the Volusia.org/property website: 
3. KNN was used with a limit of 1 to find the nearest geom with luc='2000' for each individual parcel.
4. ST_Distance() was then used to find the distance in miles between the parcel geom and the airport geom.
5. This process was looped through the entire volusia.parcel table for all parid's. 

IMPORTANCE:

This project aimed to evaluate the influence of the distance to an airport on a parcels selling price. It was shown that house prices in Volusia County
share a linear relationship with airport distance. However, the most significant factor affecting a properties value was the size and scale of the airport itself. 
In total, three airports were investigated to assess how their presence influenced the house value. 

KEY FINDINGS:

DOWNLOAD OPTIONS: 
1. Run the code: airport_d.py ** remember to change to your Postgres password.
2. Import the data file: dataset_arpt_dst.txt to pgAdmin4 ** Note that the txt file is tab delimated.
