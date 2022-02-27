#Author: 766468
import math
def isInputANumber(number):
    try:
        val = int(number)
    except:
        print("Input is not an integer number! Try again!")
        return False
    else:
        return True

def coordinateSetUp():
    coordinates=list()
    while True:
        while True:
            print ("Enter coordinates for corner ",len(coordinates),": x=",end="")
            x=input()
            if(x==""):
                break
            number=isInputANumber(x)
            if (number):
                break
        while True:
            print(", y=",end="")        
            y=input()
            if(y==""):
                break
            number=isInputANumber(y)
            if (number):
                break
        if x=="" or y=="":
            if len(coordinates)<3:
                print("Less than three coordinates have been introduced. Inserted coordinates: ",coordinates)
            else:
                break
        elif ((int(x),int(y)) in coordinates):
            #if nothing is inputted, i.e. empty coordinate, take it as closed polygon as well
            # OR if tuple is already in list coordinates, take it as a closed polygon
            if len(coordinates)<3:
                print("Less than three coordinates have been introduced. Inserted coordinates: ",coordinates)
            else:
                break
            
        else:
            x=int(x)
            y=int(y)
            coordinates.append((x,y))#append tuples to set, so no coordinate is repeated
    print(coordinates)
    return coordinates

def calculateArea(coordinates):
    areaSum=0
    for i in range (len(coordinates)-1):
        areaSum=coordinates[i][0]*coordinates[i+1][1]-coordinates[i+1][0]*coordinates[i][1]
    return abs(areaSum/2)
        
def getPolygonArea():
    coordinates=coordinateSetUp()
    result=calculateArea(coordinates)
    print(result)

if __name__=="__main__":
    getPolygonArea()
    input("...")
        
