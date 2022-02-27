#Author: 766468, Oscar Aguilar Aguila Isaías 

"""
This module consists of different number checking for error handling and or prevention.
"""


def isItAPositiveNumber(numberToTest):
    """
    This function tests whether or not a number is positive, by using th function "isItANumber"
    param1: numberToTest
    return: bool
    github test
    """
    if isItANumber(numberToTest):
        if(numberToTest > 0):
            return True
        else:
            print_errmsg("Negative or Zero detected!")
            return False
    else:
        return False
    
def isItANumber(numberToTest):
    """
    This function tests whether or not an input is a number (float)
    param1: numberToTest
    return: bool
    """
    try:
        val = float(numberToTest)
        return True
    except ValueError:
        print_errmsg("Input is not a number!")
        return False
    
__errmsg_enabled = False
def print_errmsg( *text ):
    if __errmsg_enabled : print( *text )
