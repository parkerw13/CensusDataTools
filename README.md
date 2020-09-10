# CensusDataTools

The tools here will allow people to take specific census data tables and extract specific columns with new headers for other use.

FormatTableB03002 will take the raw census table B03022 table and update the column headers and extract out just the raw counts for
total population, white, black, american indian/native alaskan, asian, native hawaiian/pacific islander, some other race, 2 or more races, hispanic/latino.
It then calculates the total minority population (minority is considered all the non-white population) and then the percent minority in each census geography

The PostGIS_CreateTableForRace.sql is an sql query that can be run in the PostGIS query window of PgAdmin to create a new table with the same headers as the formatted census csv. The table name and schema should be set to one that is in your database.

A manual import of the formatted census csv is run in PgAdmin 4 to import thte formatted table to the empty table just created.

The JoinRaceData_AlamedaCountySample.sql is a sql query that can be run in the PostGIS query window of PgAdmin to join the newly created census csv to the census shapefile (must already be loaded into your PostGIS database) and save it as a new table. This table can be viewed in a GIS viewer such as QGIS.


Next steps are to create a single Python tool that will create the table, import the csv, join it, and create new table. 

