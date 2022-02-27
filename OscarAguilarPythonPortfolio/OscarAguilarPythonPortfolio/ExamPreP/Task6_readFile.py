#Author 766468
f=open ("T6_input.txt")
products=[]
for line in f:
    splitted= line.split(" ")
    for i in range(len(splitted)):
        if ("\n" in splitted[i]):
            splitted[i]=splitted[i].split("\n")[0]
        splitted[i]=float(splitted[i])
    products.append(splitted[0]*splitted[1])
print (products)
(maximum,minimum)=(max(products),min(products))
print("The maximum product is {} and the minimum product is {}".format(maximum, minimum))
