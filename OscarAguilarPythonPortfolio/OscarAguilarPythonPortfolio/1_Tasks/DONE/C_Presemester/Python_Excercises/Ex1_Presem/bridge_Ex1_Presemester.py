#Author: 766468
#Implement a function:
#def bridge( a, b, c, n )
    #- determines a list of the positions and a list
       #of the length of the elements
    #- return positions, elements

#call the function from the >>> prompt
#Check that all values are bigger than 0. Illegal values shall be entered again.
#• Calculate and print the length of every steel element as well as the total length of all steel elements
#• Tricky: The first steel element has to be at position 0, the last at position a!

'''
Defining function to calculate
p1
p2

'''
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

def calculateP1(b,a):
    p1=-(4*b)/(a**2)
    return p1

def calculateP2(b,a):
    p2=4*b/a
    return p2


'''
Defining bridge function to
    place positions and lengths of elements in list
    return positions and elements
'''
    
def bridge (a,b,c,n):
    #There is an 'a' length supported(divided) by n elements 
    #therefore, N elements in the list and N positions, starting in 0
    p1=calculateP1(b,a)
    p2=calculateP2(b,a)
    positions=[]
    lengths=[]
    correctedLengths=[]
    lengthBewteenElements=a/(n-1)
    for x in range (0,n):
        positions.append(round(lengthBewteenElements*x,5))
    #Calculate length of every steel rod based on position
    for position in positions:
        y=p1*(position**2)+p2*position+c #could be done differently b+c-length
        lengths.append(y)
    maxLength=max(lengths)
    #Invert the parabola by taking the max length to the side (position0)
    #this is done by getting the max length, and subtracting the original length
    #then adding a corrected C)
    for length in lengths:
        correctedLengths.append(round(maxLength-length+c,5))
    
    '''differencePerRod=lengths[1]-lengths[0]
    MaxLength=lengths.max()
    for length in lengths:
        MaxLength-di
        '''
    #print out everything
    '''
    print("****Lengths****")
    print(correctedLengths)
    print("***Positions***")
    print(positions)
    '''
    #"Pretty" Print--> As desired at the presemester page
    print ("Calculation:")
    for i in range(len(positions)):
        print("Element No. ", i, " at x-position ", positions[i], " has a length of ", correctedLengths[i])
        
if __name__=="__main__":
    a=isItAPositiveNumber("a")
    b=isItAPositiveNumber("b")
    c=isItAPositiveNumber("c")
    n=isItAPositiveNumber("n")
    bridge (a,b,c,n)
    input("...")

