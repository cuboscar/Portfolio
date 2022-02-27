#Author(s): 766468


#File: type_of_triangle_impl_TASK.py
""" Implements function type_of_triangle.

- make the function robust against false input
- print diagnostic messages (call print_errmsg( "message text" ), see below)
- return error code (to be specified)
"""
import sys 
import os
sys.path.append(os.path.abspath("D:/Semester/Applied Programming/766468_AppliedProgramming/0_ReUse_Library/stringOfFloatsToFloatArray"))
from stringOfFloatsToFloatArray import *
from math import *

def triangleInequalityValidity(splittedTriangles):
    a=splittedTriangles[0]
    b=splittedTriangles[1]
    c=splittedTriangles[2]
    if(isItANumber(a) and isItANumber(b) and isItANumber(c)):
        a=float(splittedTriangles[0])
        b=float(splittedTriangles[1])
        c=float(splittedTriangles[2])
        if((a+b>c) and (b+c>a) and (a+c>b)):
            #print ("x")
            return True
        else:
            return False
    else:
        return False
        
                    

def type_of_triangle( inputString ):
    """ Determines the type of a triangle.

        input: three sides of a triangle as string (e.g. "3 4 5")
        
        returns:
           3  for equilateral (three sides of equal length)
           2  for isosceles (two sides of equal length)
           1  for general ordinary triangle
           0  not a triangle or non numeric input
           -1 less than three sides inputted

        ** please add further specs if needed **
    
    
    TODO: add further doctests
    >>> type_of_triangle( "3 3 3" )
    3
    
    >>> type_of_triangle( "3 4 5" )
    1
    >>> type_of_triangle("3 3 a")
    0
    """
    triangle=inputString
    splittedTriangles=triangle.split(" ")
    typeOfTriangle=-1
    setToCompare=stringOfFloatsToFloatSet(triangle)
    #print(setToCompare)
    if (len(splittedTriangles)!=3):
        print_errmsg("Either less or more than 3 lengths have been inputted.\nTherefore, it is not a triangle!")
        typeOfTriangle=-1
    #print(triangleInequalityValidity(splittedTriangles))
    if (not triangleInequalityValidity(splittedTriangles)):
        typeOfTriangle=0
    else:
        if (len(setToCompare)==3):
            typeOfTriangle=1
        elif (len(setToCompare)==2):
            typeOfTriangle=2
        elif (len(setToCompare)==1):
            typeOfTriangle=3
    return typeOfTriangle  # TODO: replace with correct implementation


__errmsg_enabled = True

def set_errmsg( enabled ):
    global __errmsg_enabled
    __errmsg_enabled = enabled

def print_errmsg( *text ):
    if __errmsg_enabled : print( *text )


if __name__ == "__main__":

   set_errmsg( False )

   # run the test cases:
   print( ">>> doctest (impl) >>>" )
   import doctest
   doctest.testmod()
   print( "<<< doctest (impl) <<<" )

   # keep the window open
   input( "..." )
