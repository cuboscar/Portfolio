#Author: 766468, Oscar Aguilar Aguila Isaías 
"""
    The current files
"""

def isItAPositiveNumber(numberToTest):
    if isItANumber(numberToTest):
        if(numberToTest > 0):
            return True
        else:
            print("Negative or Zero detected!")
            return False
    else:
        return False
    
def isItANumber(numberToTest):
    try:
        val = float(numberToTest)
        return True
    except ValueError:
        print("Input is not a number!")
        return False
