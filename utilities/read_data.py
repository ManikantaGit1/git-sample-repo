import csv


def getCsvData(fileName):
    rows = []
    openFile = open(fileName, 'r')
    reader = csv.reader(openFile)
    next(reader)
    for i in reader:
        rows.append(i)
    return rows
