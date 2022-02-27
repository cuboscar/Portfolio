def extractDuplicatesInList(inputList):
    outputList=[]
    for value in inputList:
        if (inputList.count(value)>1):
            outputList.append(value)
    return outputList
