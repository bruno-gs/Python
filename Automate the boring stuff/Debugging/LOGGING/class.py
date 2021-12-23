# LOGGING IS A GREAT WAY TO SEE WHAT'S HAPPENING IN YOUR CODE

import logging
logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# to have a file with the messages from the log
# logging.basicConfig(filename='myProgramLog.txt',level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# To disable the messages
logging.disable(logging.CRITICAL)

# To create and see messages and control your CODE
logging.debug('Start of program')

# Example with factorial
def factorial(n):
    logging.debug(f'Start of factorial {n}')

    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i is {i}, total is {total}')

    logging.debug(f'return value is {total}')
    return total

print(factorial(5))

logging.debug('End of program')
