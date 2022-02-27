import sys 
import os
sys.path.append(os.path.abspath("D:/Semester/Applied Programming/766468_AppliedProgramming/0_ReUse_Library/checkForNumbers"))
from checkForNumbers import *
def stringOfFloatsToFloatSet(stringOfFloats):
    """
    This function splits a string of floats into an array of floats.
    Afterwards, it returns the array.
    """
    floatSet=set()
    if(isString(stringOfFloats)==True):
        
        splittedSringOfFloats=stringOfFloats.split(" ")
        for i in range(len(splittedSringOfFloats)):
            boolIsItANumber=isItANumber(splittedSringOfFloats[i])
            if(not boolIsItANumber):
                print_errmsg("Error! Element number {:d} in string is not a float number!".format(i+1))
                #return False #TODO: implement errors}
                floatSet=set()
                return floatSet
            else:
                if(float(splittedSringOfFloats[i])<=0):
                    print_errmsg("Error! Element number {:d} in string is equal to or lower than 0!".format(i+1))
                    #print(floatSet)
                    floatSet=set()
                    #print(floatSet)
                    return floatSet
                else:
                    floatSet.add(float(splittedSringOfFloats[i]))

    return floatSet
    
def isString(string):
    if(isinstance(string,str)):
        return True
    else:
        print("Not a string!")
        return False
    
__errmsg_enabled = False
def print_errmsg( *text ):
    if __errmsg_enabled : print( *text )
        
         
