import csv

print("Starting")

def writeToCSV(data):
    for i in data:
        print(i)
        w.writerow(i)
        

csvFile = input("Enter raw Census CSV File (no quotes):")
newCSV = input("Enter output Census CSV File (no quotes:")

headers = "geoid_census","geo_name","geo_join","total_pop","white","black","am_indian_nat_alaska","asian","nat_hawaiian_pac_island","some_other","two_or_more","hispanic_latino"

print("CSV at path {0} is in a variable".format(csvFile))


fileRef = open(csvFile)
csvRef = csv.reader(fileRef)

print("CSV file is opened and in a reader variable for reference")

censusDict = {}


for row in csvRef:
    #print(row)
    if csvRef.line_num <= 3:
        continue
    geoJoin = row[0][9:]
    totMinority = int(row[8])+int(row[10])+int(row[12])+int(row[14])+int(row[16])+int(row[18])+int(row[24])
    if int(row[2]) != 0:
        prctMinority = round((totMinority/float(row[2]))*100,2)
    else:
        prctMinority = -999
    censusDict[row[0]] = [row[0],row[1],geoJoin,int(row[2]),int(row[6]),int(row[8]),int(row[10]),int(row[12]),int(row[14]),int(row[16]),int(row[18]),int(row[24]),totMinority,prctMinority]
    #print(row)
    #print(row[0])
    #print(row[1])


with open(newCSV, 'w') as csvWriter:
    print("Creating writer to write to new csv")
    w = csv.writer(csvWriter, delimiter= ',', lineterminator = '\n')
    print("Writing headers")
    #writeToCSV(headers)
    w.writerow(headers)
    print("Starting to write census data to csv")
    for key, value in censusDict.items():
        print(value)
        w.writerow(value)

print("Done")
        
        
    
    



