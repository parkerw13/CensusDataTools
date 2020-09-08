import csv

print("Starting")

def writeToCSV(data):
    for i in data:
        print(i)
        w.writerow(i)
        

csvFile = r"C:\Users\William\Desktop\CensusData\RaceHispanic\ACS_5YR_Hispanic_AlamedaCounty\ACSDT5Y2018.B03002_data_with_overlays_2020-08-31T161649_TEST.csv"
newCSV = r"C:\Users\William\Desktop\CensusData\RaceHispanic\ACS_5YR_Hispanic_AlamedaCounty\ACSDT5Y2018.B03002_data_with_overlays_2020-08-31T161649_NEW.csv"

headers = "geoid","geo_name","total_pop","white","black","am_indian_nat_alaska","asian","nat_hawaiian_pac_island","some_other","two_or_more","hispanic_latino"

print("CSV at path {0} is in a variable".format(csvFile))


fileRef = open(csvFile)
csvRef = csv.reader(fileRef)

print("CSV file is opened and in a reader variable for reference")

censusDict = {}


for row in csvRef:
    #print(row)
    if csvRef.line_num <= 3:
        continue
    censusDict[row[0]] = [row[0],row[1],row[2],row[6],row[8],row[10],row[12],row[14],row[16],row[18],row[24]]
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
        
    
    



