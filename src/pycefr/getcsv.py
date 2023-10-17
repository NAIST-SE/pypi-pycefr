#-- PROGRAM TO OBTAIN SUMMARIES FROM CSV

import csv
import os
import pandas as pd

def cleanData(): 
    """ Clean the data from the csv. """
    # Read the CSV file into a DataFrame
    df = pd.read_csv('results/d.csv')
    df.dropna(subset=['Repository', 'File Name', 'Class', 'Start Line', 'End Line', 'Displacement', 'Level'], inplace=True)
    # Write the cleaned dataframe to a new CSV file
    df.to_csv('results/d.csv', index=False)

def create_csv(myDataList):
    """Scrolls through the list looking for different .py files. """
    #-- Remove the header
    cleanData()
    list = myDataList[1:]
    myDataCsv = ''
    for i in list:
        if (myDataCsv == '') or (i[1] != myDataCsv[1][1]):
            myDataCsv = [['Repository', 'File Name', 'Class', 'Start Line',
                          'End Line', 'Displacement', 'Level']]
        myDataCsv.append(i)
        print (myDataCsv[1][1])
        file_name = myDataCsv[1][1]
        write_FileCsv(myDataCsv, file_name)


def write_FileCsv(myDataCsv, file_name, file_csv = ""):
    """ Create and add data in the .csv file. """
    #-- Get current path
    wd = os.getcwd()
    #-- Create new folder
    try:
        os.mkdir(wd + "/DATA_CSV")
    except FileExistsError:
        pass
    file_name = file_name.split('.py')[0] + '.csv'
    path_file = wd + '/DATA_CSV/' + file_name
    #-- Create a csv with each file name
    if not file_csv:
        file_csv = open(path_file, 'w',encoding="utf-8")
        with file_csv:
            writer = csv.writer(file_csv)
            writer.writerows(myDataCsv)
    else:
        with open(path_file, 'a',encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(myDataCsv)


def read_FileCsv(file_csv = ""):
    """ Read data.csv and create a list to iterate. """
    cleanData()
    with open('results/d.csv', newline='',encoding="utf-8") as File:
        reader = csv.reader(File)
        myDataList = []
        for row in reader:
            myDataList.append(row)
            # print(row)
        create_csv(myDataList)


if __name__ == '__main__':
    cleanData()
    read_FileCsv()
