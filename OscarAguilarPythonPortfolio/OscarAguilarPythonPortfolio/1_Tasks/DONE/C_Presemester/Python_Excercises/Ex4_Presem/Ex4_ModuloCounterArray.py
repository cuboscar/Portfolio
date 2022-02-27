#Author 766468
from enum import Enum
class Option(Enum):
    NAME=1
    CURRENT_VALUE=2
    
switcher={2:"BINARY COUNTER",8:"OCTAL COUNTER",10:"DECIMAL COUNTER",16:"HEXADECIMAL COUNTER"}

def isItAPositiveNumber(param):
    while True: #do-while substitute
        number=input("Enter a value for {}: ".format(param))
        try:
           val = int(number)
           if(val > 0):
               return int(number)
               break
           else:
               print("Negative numbers are not possible!")
        except ValueError:
           print("Input is not a number! Try again!")


    
def switch(counterType):
    return switcher.get(counterType)

from Ex4_ModuloCounterDigit import ModuloNCounter

class ModuloNCounterArray():
    def __init__(self,maxValue,numberOfDigits):
        self.maxValue=maxValue
        self.numberOfDigits=numberOfDigits
        self.globalOverflow=0
        self.array=[]
        for i in range (self.numberOfDigits):
            self.array.append(ModuloNCounter(self.maxValue))

    def printCounter(self,option):
        if (option == Option.CURRENT_VALUE.name):
            buffer=[]
            for i in range (self.numberOfDigits):
                buffer.append(self.array[i].currentValue)
            buffer=buffer[::-1]
            if self.maxValue==16:
                print ("0x",end=" ")
                for i in range (len(buffer)):
                    print(hex(buffer[i])[2:],end=" ")
            else:
                print(*buffer,end="")
        elif (option == Option.NAME.name):
            print(switcher[self.maxValue])
            

    def increaseCounterArr(self):
        for i in range (self.numberOfDigits):
            overFlow=self.array[i].count()#increase Lowest
            if(not overFlow):
                break
            elif (overFlow and i+1==self.numberOfDigits):
                self.globalOverflow=1
                tempGlobalOverflow=self.globalOverflow
                print ("GLOBAL OVERFLOW REACHED! COUNTER ARRAY RESET AND LOST!")
                self.globalOverflow=0
                return tempGlobalOverflow
        #self.printCounter("CURRENT_VALUE")

            
def useCounters(base,digits,countTimes):
    if (base != 2 and base !=8 and base !=10 and base!=16):
        print("Invalid base! Valid bases are {},{},{}, and{}".format(switcher[2],switcher[8],switcher[10],switcher[16]))
    else:
        M=ModuloNCounterArray(base,digits)
        for i in range (countTimes):
            M.increaseCounterArr()
        M.printCounter("NAME")
        print("End value = ",end="")
        M.printCounter("CURRENT_VALUE")
        
if __name__=="__main__":
    base=isItAPositiveNumber("base")
    digits=isItAPositiveNumber("digits")
    countTimes=isItAPositiveNumber("countTimes")
    useCounters(base,digits,countTimes)
    input("\n...")
