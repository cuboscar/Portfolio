#Author(s): 766468

#File: primes.py
""" Collection of (reusable) functions for prime number related tasks.

    TODO: add (further) doctests
"""


def is_prime( n ):
    """ Returns True if n in a prime.

        TODO: add further doctests
        >>> is_prime(0)
        False
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(5)
        True
        >>> is_prime(4)
        False
        >>> is_prime(104729)
        True
        >>> is_prime (104730)
        False
        >>> is_prime (55)
        False
    """
    isPrime=True
    if n==1 or n==0 or not isinstance(n, int):
        isPrime=False
    else: 
        if (n%2==0 and n!=2) or (n%5==0 and n!=5): #Modified to check whether or not a number is divisible by two or 5
            isPrime=False
        else:
            for number in range (3,math.floor(math.sqrt(n))+1): #The highest number which can be a factor of the number would be that number's square root
                if (n%number==0):
                    isPrime=False
                    break
            
    #return factor(n) == 1 #From professor
    return isPrime
    


def factor( n ):
    """ Return the smallest prime factor of n
        or 1 if n is prime
        or 0 if n < 2 or not int.
        
        TODO: add further doctests
        >>> factor(3)
        1
        >>> factor(4)
        2
        >>> factor(0)
        0
        >>> factor(1)
        0
        >>> factor(6.3333)
        0
        >>> factor(2809)
        53
    """
    
    if is_prime(n):
        fact=1
    elif((n<2) or (not isinstance(n, int)) ):
        fact=0
    else:
        if (n%2==0):
            fact=2
        elif (n%5==0):
            fact=5
        else:
            for number in range (3,math.floor(math.sqrt(n))+1):
                if (n%number==0):
                    fact=number
                    break
    return fact
    
    
def getPrimesList(n):
    primesList=[]
    for number in range (0,n):
        if is_prime(number):
            primesList.append(number)
    return primesList

def getGaps(primesList):
    gapsList=[]
    for i in range (1,len(primesList)):
        gapsList.append(primesList[i]-primesList[i-1])
    return gapsList

def onlyBiggestGaps(gapsList):
    gapsSet=set()
    for i in range (0,len(gapsList)):
        gapsSet.add(gapsList[i])
    return gapsSet
        
if __name__ == "__main__":
    import math
    # run the test cases:
    print( ">>> doctest >>>" )
    import doctest
    doctest.testmod()
    print( "<<< doctest <<<" )
    print()


    import time

    # determine number of primes below n
    n = 99_999
    startTime = time.perf_counter()
    cntPrimes = 0
    cntPrimes=len(getPrimesList(n))
    print( cntPrimes, time.perf_counter() - startTime )

    primes = getPrimesList(n)
    print("primes: ",primes)
    # primes: 2 3 5 7 11 13 17 19 23 29
    gaps=getGaps(primes)
    print("gaps: ",gaps)
    # gaps:    1 2 . 4  .  .  .  .  6
    gap=onlyBiggestGaps(gaps)
    # determine longest prime gaps: 1, 2, 4, 6, 8, 14, 18, 20, ... (performance challenge)
    startTime = time.perf_counter()
    # TODO: add implementation
    print( gap, time.perf_counter() - startTime )


    # keep the window open
    input( "..." )
