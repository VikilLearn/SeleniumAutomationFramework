import csv

def getCSVData(fileName):
    # create an empty list to store rows
    rows = []

    # open the CSV file
    datFile = open(fileName, 'r')

    # create a CSV reader from CSV file
    reader = csv.reader(datFile)

    # skip the headers
    next(reader)

    # add rows from reader to list
    for row in reader:
        rows.append(row)

    return rows