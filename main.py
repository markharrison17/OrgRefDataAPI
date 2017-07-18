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



if __name__ == "__main__":
    do_setup()
