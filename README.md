# CS540_Project_Airport
Provides all material required to determine the distance to the nearest airport for all parcels in Volusia County. 

PROJECT OBJECTIVE:

The purpose of this project was to determine the distance in miles from all parcels in Volusia County (VC) to it's nearest airport. 

PROCESS:
1. Each individual parcel was identified using its parcel id from the volusia.parcel table (only used parcels with geometry). 
2. Airports can be identified using the land use code (LUC) of '2000'. This information was sourced from the Volusia.org/property website: 
3. KNN was used with a limit of 1 to find the nearest geom with luc='2000' for each individual parcel.
4. ST_Distance() was then used to find the distance in miles between the parcel geom and the airport geom.
5. This process was looped through the entire volusia.parcel table for all parid's. 

IMPORTANCE:

This project aimed to evaluate the influence of the distance to an airport on a parcels selling price. It was shown that house prices in Volusia County
share a linear relationship with airport distance. However, the most significant factor affecting a properties value was the size and scale of the airport itself. 
In total, three airports were investigated to assess how their presence influenced the house value. Plots of the price behaviour with respect to nearest airport distance are provided in the attached PowerPoint. 

KEY FINDINGS:

It was shown that the distance to an aiport does have an effect on property value. However, the value of a home is more concerned with the size of the airport. For larger airports, such as Daytona International Airport the house price reduces as the distance from the property to the airport decreases. Conversely, for smaller, less commercial, airports, such as New Smyrna Airport, the property price increases as distance decreases.

SQL COMMANDS:

To determine the distances for each parid in the county, a Python script was developed to loop through the table in its entirety. Firstly though, all of the "null" geometries were removed because it was not possible to determine the distance between the nearest airport and the parcel without it. 

Another prerequisite before using the following SQL commands was to create a column within the volusia.parcel table to store the airport distance data. To do so use the command:

ALTER TABLE volusia.parcel ADD COLUMN airport_d double precision;

Alternatively, you could create a new table. ** You can more culumns if you need to...

CREATE TABLE volusia.new_table (
    parid numeric,
    airport_distance double precision
);

There are two SQL commands used in the Python code:

1. select p.parid::integer, p.geom, ST_Distance(p.geom, (select p2.geom from volusia.parcel p2 where p2.parid=" + parid + "))/5280  from volusia.parcel p where    
    p.luc='2000' order by p.geom <-> (select p2.geom from volusia.parcel p2 where p2.parid=" + parid + ") limit 1;
    
As the code ran through each row in the parcel table and calculated the distance, it was then added to the parcel table under the column name "airport_d" using the code below.  
  
2.  sql3 = "update volusia.parcel p1 set airport_d = " + str(distance) + " where p1.parid=" + parid + ";"

DOWNLOAD OPTIONS: 
1. Run the code: airport_d.py ** remember to change to your Postgres password.
2. Import the data file: dataset_arpt_dst.txt to pgAdmin4 ** Note that the txt file is tab delimated.
