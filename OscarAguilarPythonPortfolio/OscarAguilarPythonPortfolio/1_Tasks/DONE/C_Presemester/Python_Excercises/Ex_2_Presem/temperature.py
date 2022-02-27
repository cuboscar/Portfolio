#Author: 766468
def celsius2Farenheit(celsius):
    farenheit=(celsius*9/5)+32
    #print("{}°C = {}°F".format(celsius,farenheit))
    return farenheit

def farenheit2Celsius(farenheit):
    celsius=(farenheit-32)/(9/5)
    #print("{}°F = {}°C".format(farenheit,celsius))
    return celsius

def kelvin2CelsiusAndFarenheit(kelvin):
    celsius=kelvin-273.15
    farenheit=celsius2Farenheit(celsius)
    print("{}K = {}°C = {}°F".format(kelvin,celsius,farenheit))
    result=(celsius,farenheit) #return as tuple
    return result

if __name__ == "__main__":
    print("Temperature Converter")
    print("=====================")
    celsius=[0,100]
    for temperature in celsius:
        farenheit=celsius2Farenheit(temperature)
        print("{}°C = {}°F".format(temperature,farenheit))
    farenheit=[0,100]
    for temperature in farenheit:
        celsius=farenheit2Celsius(temperature)
        print("{}°F = {}°C".format(temperature,celsius))

    print("")

    for i in range (11):
        kelvin2CelsiusAndFarenheit(100*i)
    input("...")
