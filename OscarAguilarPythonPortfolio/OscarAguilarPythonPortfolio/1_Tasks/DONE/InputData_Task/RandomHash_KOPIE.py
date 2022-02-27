#Author(s): 102242

#File: RandomHash.py
""" Determines reproducible hash values. """


import random

def random_hash( number, bits=64 ):
    """ Determines random hash value for number.
   
    TODO: add further doctests
    >>> random_hash( 765432 )
    9503171686022637069

    >>> random_hash( "765433" )
    4100528466891446958

    >>> random_hash( "765434" )
    6330401606655874305

    """
    random.seed( int( number ) )
    return random.getrandbits( bits )


if __name__ == "__main__":

   # run the doctest cases:
   print( ">>> doctest >>>" )
   import doctest
   doctest.testmod()
   print( "<<< doctest <<<" )

   # keep the window open:
   input( "..." )  # activate/deactivate at will
