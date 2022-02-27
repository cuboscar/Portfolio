#Author 766468
"""
Write a small program which uses a data structure to store the properties of a modulo n counter,
which counts from 0 to n-1, just beginning at 0 again after having reached n-1 (overflow).
Declare a class for counters with integer members for:
• the maximum count value (n)
• the current count value

Write functions which
• initialize a counter by setting the current count value to 0 and the maximum count value to
an arbitrary value.
• count, that is increase the current count value of a passed counter by 1 or reset it to 0, in
case of the value becomes greater than n-1 (overflow). It returns 1 if an overflow had
occurred otherwise 0.
• optionally print the name of the counter (modulo n counter, n should be replaced by the
current value of the maximum count value) or the current count value (without newline!).
Use an enumeration type to pass the option.
Test the code with a modulo 10 counter, print its name, count three times until the overflow while
printing the actual count value after each counting step. 

"""
#Enumeration in Python
from enum import Enum
class Option(Enum):
    NAME=1
    CURRENT_VALUE=2
    
#Class ModuloNCounter
class ModuloNCounter():
    
    #Constructor
    def __init__(self,maxValue):
        self.maxValue=maxValue
        self.currentValue=0 #Not user-defined, but needs to be in initialization
        self.overFlow=0
    #count
    def count(self):
        self.currentValue+=1  #increase value
        if self.currentValue >=self.maxValue: #if currentValue is greater than or equal to maxValue,set currentValue to 0
            self.currentValue=0
            self.overFlow=1
        overFlowFlag=self.overFlow# overflow buffer
        self.overFlow=0 #resetOverflow
        #print(self.currentValue)
        return overFlowFlag
    #option printing
    def printingOption(self,option): #Option.Name.name
        if (option==Option.NAME.name):#print name
            print("Hi, I'm a counter with a {} base!".format(self.maxValue))
        elif (option==Option.CURRENT_VALUE.name):
            print("Hi, my current value is {}".format(self.currentValue))

