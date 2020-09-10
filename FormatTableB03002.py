import csv

print("Starting")

# Get user input for raw census csv and new csv to be created, this needs to be full path no quotes.
csvFile = input("Enter raw Census CSV File:")
newCSV = input("Enter output Census CSV File:")

# Column headers in the csv, for import to PostGIS the table headers need to match exactly. These are formatted in standard PostGIS format.
headers = ["geoid_census","geo_name","geo_join","total_pop","white","prct_white","black","prct_black","am_indian_nat_alaska","prct_am_indian_nat_alaska","asian","prct_asian",
           "nat_hawaiian_pac_island","prct_nat_hawiian_pac_island","some_other","prct_some_other","two_or_more","prct_two_or_more","hispanic_latino","prct_hispanic_latino",
           "total_minority","percent_minority","majority_population","percent_of_pop_majority_pop"]

print("CSV at path {0} is in a variable".format(csvFile))

# create a variable to hold the open csv and one for reading the open csv for the input census csv
fileRef = open(csvFile)
csvRef = csv.reader(fileRef)


print("CSV file is opened and in a reader variable for reference")

# Create and empty dictionary to hold the values from the census table
censusDict = {}

# Iterate through each row in the csv
for row in csvRef:
    #print(row)
    # This if statement will skip the first 2 lines of the csv since the census csvs have 2 headers and we want to drop those and creat our own.
    if csvRef.line_num <= 2:
        continue
    # Take the GEOID field in the census csv and drop the first 9 characters as they are not in the census shapefiles that this can be joined to.
    geoJoin = row[0][9:]

    # Calculate the total minority population. For this all people that are not white are considered minority
    totMinority = int(row[8])+int(row[10])+int(row[12])+int(row[14])+int(row[16])+int(row[18])+int(row[24])
    # Create a list of all the populaton values and find the index in the list of the value that is the max
    popList = [int(row[6]),int(row[8]),int(row[10]),int(row[12]),int(row[14]),int(row[16]),int(row[18]),int(row[24])]
    maxValIndex = popList.index(max(popList))

    # Because some census geographies have 0 populaton an if statement is needed to calculate percentage in just the geographies with a total pop as dividing by 0 causes an error
    if int(row[2]) != 0:
        # Calculate the percent of each population in the geography
        prctWht = round((int(row[6])/float(row[2]))*100,2)
        prctBlk = round((int(row[8])/float(row[2]))*100,2)
        prctAmIn = round((int(row[10])/float(row[2]))*100,2)
        prctAsi = round((int(row[12])/float(row[2]))*100,2)
        prctNatHaw = round((int(row[14])/float(row[2]))*100,2)
        prctSmOth = round((int(row[16])/float(row[2]))*100,2)
        prctTwoMr = round((int(row[18])/float(row[2]))*100,2)
        prctHispLat = round((int(row[24])/float(row[2]))*100,2)
        prctMinority = round((totMinority/float(row[2]))*100,2)

        # If and elif statements to find what the largest population is in the geography and set that percentage to percent majority
        if maxValIndex == 0:
            majPop = "White"
            prctMaj = prctWht
        elif maxValIndex == 1:
            majPop = "Black"
            prctMaj = prctBlk
        elif maxValIndex == 2:
            majPop = "American Indian/Native"
            prctMaj = prctAmIn
        elif maxValIndex == 3:
            majPop = "Asian"
            prctMaj = prctAsi
        elif maxValIndex == 4:
            majPop = "Native Hawaiian Pacific Islander"
            prctMaj = prctNatHaw
        elif maxValIndex == 5:
            majPop = "Some Other Race"
            prctMaj = prctSmOth
        elif maxValIndex == 6:
            majPop = "Two or More Races"
            prctMaj = prctTwoMr
        elif maxValIndex == 7:
            majPop = "Hispanic/Latino"
            prctMaj = prctHispLat
    else:
        # This will set all percentages to -999 so they will be obvious as in areas with no population.
        prctWht = -999
        prctBlk = -999
        prctAmIn = -999
        prctAsi = -999
        prctNatHaw = -999
        prctSmOth = -999
        prctTwoMr = -999
        prctHispLat = -999
        prctMinority = -999
        prctMinority = -999
        prctMaj = -999
        majPop = "None, no population"
    
    # Add each geography to the empty dictionary with the list that has the geo id, geography name, geo id for join, and population and percentage data.
    # All the numbers are added as ints or float
    censusDict[row[0]] = [row[0],row[1],geoJoin,int(row[2]),int(row[6]),prctWht,int(row[8]),prctBlk,int(row[10]),prctAmIn,int(row[12]),prctAsi,int(row[14]),prctNatHaw,
                          int(row[16]),prctSmOth,int(row[18]),prctTwoMr,int(row[24]),prctHispLat,totMinority,prctMinority,majPop,prctMaj]
    #print(row)
    #print(row[0])
    #print(row[1])



# Write from the data dictionary out to a csv with each value as a single comma seperated line.
with open(newCSV, 'w') as csvWriter:
    print("Creating writer to write to new csv")
    # Create a variable to hold the writer with a delimeter as a , and the lineterminator set to '\n' to ensure no blank lines between lines from the data dictionary
    w = csv.writer(csvWriter, delimiter= ',', lineterminator = '\n')
    print("Writing headers")
    # Write out the headers as the first row of the csv
    w.writerow(headers)
    print("Starting to write census data to csv")
    # iterate through key, value pairs to write value lists as a row
    for key, value in censusDict.items():
        print(value)
        # Write the row from the data dictionary
        w.writerow(value)

print("Done")
