import math
import matplotlib.pyplot as plt
import numpy as np

t=np.linspace(0,10,400,endpoint=False).tolist() # step size of 0.25, by dividing 10 into 40 
t.append(10) # adding the last  part to avoid rounding errors
d=0.25 #defined constants d and t

"""
Now declare arrays for plotted functions 
"""
X=[]
Y=[]

"""
Now fill arrays
"""

for i in range (len(t)):
    X.append(math.exp(t[i])*math.cos(math.pi*t[i]))
    Y.append(math.exp(t[i])*math.sin(math.pi*t[i]))

"""
Finally, plot
"""
#lines=plt.subplot(projection='polar').plot(t,X,t,Y)
lines=plt.plot(X,Y)
plt.setp( lines[0], linewidth=2, color='r', linestyle="--" )
#plt.setp( lines[1], linewidth=2, color='b', linestyle="-." )
plt.grid()
plt.xlabel( 'X(t)' )
plt.ylabel( 'Y(t)' )
plt.title( "Spiral Plot" )
plt.show()

