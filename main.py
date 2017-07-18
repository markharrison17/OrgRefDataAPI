""" This module is the root of the application and contains the main startup
class."""
import logging

def do_setup():
    """Setup for the application logger."""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    #handler = DefaultStreamHandler()
    #logger.addHandler(handler)
    logger.info('configured logger')


    num1 = 1.5
    num2 = 6.3

    # Add two numbers
    sum = float(num1) + float(num2)

    # Display the sum
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


if __name__ == "__main__":
    do_setup()
