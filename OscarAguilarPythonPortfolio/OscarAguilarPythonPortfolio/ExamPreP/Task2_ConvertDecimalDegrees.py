import math

def splitEntireAndDecimals(floatNumber):
    #Assumes NaN checking has been done
    entire=round(floatNumber//1)#Obtain only units
    decimals=round(floatNumber%1,10)#get leftover decimals
    return(entire,decimals)

def floatDegrees2DegMinSec(floatDegrees,isSecondsRequired):
    #TODO: Implement error handling for not a number (NaN)
    #TODO: implement error handling for boolean isSecondsRequired
    carry=0
    conversionStep=splitEntireAndDecimals(floatDegrees)#get degrees and its decimal
    degrees=conversionStep[0] 
    carry=conversionStep[1]*60 #carry decimals to next conversion step
    conversionStep=splitEntireAndDecimals(carry) #get minutes and decimal
    minutes=conversionStep[0] 
    if(isSecondsRequired==True):
        carry=conversionStep[1]*60
        conversionStep=splitEntireAndDecimals(carry)
        seconds=conversionStep[0]+conversionStep[1] # decimals needed in seconds
    else:
        seconds=0.0
    print("{}° {}min {}sec".format(degrees,minutes,seconds))
    #input("***\nProgram ended. Press any button to get returned values and close the program...\n***")
    return(degrees,minutes,seconds)


def degMinSec2FloatDegrees(degrees,minutes,seconds=0):
    #TODO: Implement error handling to check for each being a number
    minutes=minutes+seconds/60
    floatDegrees=degrees+minutes/60
    print("{}°".format(floatDegrees))
    #input("***\nProgram ended. Press any button to get returned values and close the program...\n***")
    return floatDegrees
#TODO: implement DocTest?
