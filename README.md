# CensusDataTools

The tools here will allow people to take specific census data tables and extract specific columns with new headers for other use.

First step will be creating a new csv from the raw census csv. The new csv will be formatted with headers that are appropriate for input into
PostgresSQL/PostGIS. These are first writen as python tools to be run in IDLE with the user selecting the input and output files manually. Updates will
include a GUI for the user.

The next step is creating instructions and SQL that will import the csv into PostgresSQL.
Along with another tool that will do the same process and join the data to an existing shapefile. 
