#Author 766468
def positiveNumberCheck():
    while True: #do-while substitute
        number=input("Enter step size: ")
        try:
           val = int(number)
           if(val > 0):
               return int(number)
               break
           else:
               print("Negative numbers are not possible!")
        except ValueError:
           print("Input is not a number! Try again!")

def encode(string,stepSize):
    encoded=""
    for char in string:
        current=ord(char)
        if (ord('a')<=current) and (current<=ord('z')):
            if ((current+stepSize)>ord('z')):
                current=(current+stepSize)-(ord('z')+1)+ord('a')
            else:
                current+=stepSize
        elif (ord('A')<=current) and (current<=ord('Z')):
            if ((current+stepSize)>ord('Z')):
                current=(current+stepSize)-(ord('Z')+1)+ord('A')
            else:
                current+=stepSize
        elif (ord('0')<=current) and (current<=ord('9')):
            if ((current+stepSize)>ord('9')):
                current=(current+stepSize)-(ord('9')+1)+ord('0')
            else:
                current+=stepSize
        encoded+=(chr(current))
    print("Encoded: ",encoded)
    return encoded

def decode(string,stepSize):
    decoded=""
    for char in string:
        current=ord(char)
        if (ord('a')<=current) and (current<=ord('z')):
            if ((current-stepSize)<ord('a')):
                current=ord('z')-(ord('a')-(1+(current-stepSize)))
            else:
                current-=stepSize
        elif (ord('A')<=current) and (current<=ord('Z')):
            if ((current-stepSize)<ord('A')):
                current=ord('Z')-(ord('A')-(1+(current-stepSize)))
            else:
                current-=stepSize
        elif (ord('0')<=current) and (current<=ord('9')):
            if ((current-stepSize)<ord('0')):
                current=ord('9')-(ord('0')-(1+(current-stepSize)))
            else:
                current-=stepSize
        decoded+=(chr(current))
    print("Decoded :",decoded)
    return decoded

if __name__=="__main__":
    string=str(input("Enter string to encode/decode: "))
    stepSize=positiveNumberCheck()
    decode(encode(string,stepSize),stepSize)
    input("...")
    
    
