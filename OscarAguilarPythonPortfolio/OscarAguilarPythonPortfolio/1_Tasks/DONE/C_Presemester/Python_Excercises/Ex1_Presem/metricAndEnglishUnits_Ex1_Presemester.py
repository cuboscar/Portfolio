#Author(s): 766468

#Develop a program which translates meter units into miles and feet.
#• The user is prompted to enter a value in meter
#• In case the value is negative, an error message is printed and the input is repeated
#(hint: use a do – while loop and if statement for this)
#• The value is printed in miles and feet. 1 mile = 1852m and 1 foot = 0.3048m

#obtain data from user
#verify if negative
    #if negative reask data from user
#change to meters ad

#function declaration
def meters2miles(metersMeasurement):
    #1 mile = 1852m
    answerMiles=metersMeasurement/1852
    return answerMiles

def meters2feet(metersMeasurement):
    #1 foot = 0.3048m
    answerMiles=metersMeasurement
    return answerMiles/0.3048


userMeters=float(input("Hi! Please provide measurement in meters: "))

while userMeters < 0:
    userMeters=float(input("Sorry, measurement cannot be negative. Provide new value in meters: "))

print(userMeters, "meters = ",meters2miles(userMeters)," miles = ",meters2feet(userMeters)," feet")
print("*************")
input("Conversion done, press any key to continue")
