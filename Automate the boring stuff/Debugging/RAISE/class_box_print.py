

def boxPrint(symbol, width, height):

    ## Two examples of errors messages to direct the user
    if len(symbol) != 1:
        # for a call boxPrint('**', 5, 8)
        raise Exception('"symbol" needs to a string of length 1.')

    if len(symbol) != 1:
        # for a call boxPrint('*', 1, 1)
        raise Exception('"width" and "height" must be greater or equal to 2.')


    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    
    print(symbol * width)

boxPrint('*', 15, 5)
'''

***************
*             *
*             *
*             *
***************

'''

boxPrint('X', 5, 8)
'''

XXXXX
X   X
X   X
X   X
X   X
X   X
X   X
XXXXX

'''

boxPrint('**', 1, 1)