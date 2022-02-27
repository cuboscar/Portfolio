#Author : 766468
"""
File 'InputData_766468.dat' in the 3rd column (2nd after date and time) contains average
power values in W of 15 min intervals ending at the time given in the 1th column
as local time (with dst shift).

Please determine the average power during the period from 2019-10-22 00:00 (lokal time) to
2019-10-31 00:00 (lokal time).

For the correct result >>> random_hash( round( 1000 * result ), 16 ) should return 36771.
"""
import csv #https://www.programiz.com/python-programming/reading-csv-files
import datetime # to convert string into datetime
"""
Installation requirements:
    For Windows:
        Open a command prompt as admin and run 'pip install pytz' in order to install the pytz module
"""
import pytz # full list of timezones including UTC
from RandomHash_KOPIE import * 

def getUsefulLines(reader):
    rowCount=0
    rows=[]
    for row in reader:
        rowCount=rowCount+1 #test counter to print less than 10 lines
        if (rowCount>4):
            spaceLocations=[]
            for i in range(len(row)):
                if (row[i]==''):
                    spaceLocations.append(i)
            spaceControl=0
            for element in spaceLocations:
                row.pop(element-spaceControl)
                spaceControl+=1
            #print(row) # print for visualization, remove later
            row.pop(4)
            row.pop(2)
            rows.append(row)
            #print(row)
    return rows
    
def getUTCTimeFromRows(rows,formt,startUTCTime,stopUTCTime):
    for row in rows:
        dateTimeString=row[0]+" "+row[1]
        row.pop(0)#delete date from row
        row.pop(0)# delete time from row
        localTime=datetime.datetime.strptime(dateTimeString,formt)
        #test=datetime.datetime.strptime("04.11.2019 23:45:00", "%d.%m.%Y %H:%M:%S")
        local=pytz.timezone ("Europe/Berlin") #Local German time
        try:
            localization=local.localize(localTime,is_dst=None) 
            utcTime=localization.astimezone(pytz.utc)
            row.insert(0,utcTime)
        except:
            #print ("AmbiguousTimeError")
            localization=local.localize(localTime,is_dst=True) #Handling AmbiguousTimeError
            utcTime=localization.astimezone(pytz.utc)
            row.insert(0,utcTime)
            #print(row)

    #print(rows)
    return rows

def germanTimeToUTC (time,formt):
    localTime=datetime.datetime.strptime(time,formt)
    local=pytz.timezone ("Europe/Berlin") #Local German time
    localization=local.localize(localTime,is_dst=None)
    utcTime=localization.astimezone(pytz.utc)
    return utcTime

def getPowerAverageFromRelevantTimes(rows,start,stop):
    powerSum=0
    loopCount=0
    for row in rows:
        if (start<row[0] and row[0]<=stop):
            powerSum+=float(row[1])
            loopCount+=1
    powerAvg=powerSum/loopCount
    return powerAvg

def main():    
    with open('InputData_766468.dat','r') as file:
        reader=csv.reader(file,delimiter =" ")
        rows=getUsefulLines(reader)# 2D array of useful rows.
        """
        Important to know--> useful columns per row are:
        |   ID  index  name
        |-->1st  [0]  (DATE)
        |-->2nd  [1]  (TIME)
        |-->3rd  [2]  (Average Power Values in W)
        """
    file.close() #Close rows
    """
    From now on:
     |-->For every row, DATE and TIME Columns, create a unified UTC time column
         |-->Then delete DATE and TIME COLUMNS
             |-->Then obtain only relevant times' rows id est 'Please determine the average power during the period from 2019-10-22 00:00 (lokal time) to
    2019-10-31 00:00 (lokal time)'
    """
    formt="%d.%m.%Y %H:%M:%S"
    fromTime="22.10.2019 00:00:00"
    toTime="31.10.2019 00:00:00"
    startUTCTime=germanTimeToUTC(fromTime,formt)
    stopUTCTime=germanTimeToUTC(toTime,formt)
    UTCHandledRows=getUTCTimeFromRows(rows,formt,startUTCTime,stopUTCTime)
    powerAverage=getPowerAverageFromRelevantTimes(UTCHandledRows,startUTCTime,stopUTCTime)
    print("The average power consumption, during the period from {} to {} is {}W".format(startUTCTime,stopUTCTime,powerAverage))
    
    print("Random Hash result: {}".format(random_hash( round( 1000 * powerAverage ), 16 )))
    
if __name__== "__main__":
    main()
    input("*********************\n\nPress any key to continue...")
    
