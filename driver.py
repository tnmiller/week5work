#tnm6qz Talia Miller

#tnm6qz Talia Miller

import numpy as np
import logging  # See https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

import Wahoovian_Transformation  # Our local library with greeter()
import greeter_lib

# The following is the preferred and accepted ("Pythonesque") way to divide a  program
# into multiple files:
#   (1) In the "main" file to be run, put all code that executes in function main()
#   (2) Put your own utlility or helper functions in a separate file that's imported,
#       like greeter_lib.py here.
#   (3) In the "main" file to be run, use the if-statement at the bottom of this file.


def main():
    # Using Python's built-in logging.
    # See https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

    # Configure the logger: The options on the first line matter most.
    #   The second line clear the log-file everytime the program runs.
    #   The last two lines add a time-stamp in a format I like.
    logging.basicConfig(filename='demo-log.txt', level=logging.DEBUG,
                        filemode='w',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')

    # logging.debug('This message should go to the log file')
    # logging.info('So should this')
    # logging.warning('And this, too')

    logging.info('Program begins!')

    m1 = np.array([[2, 4], [5, -6]])
    m2 = np.array([[9, -3], [3, 6], [2, -5]])
    m4 = np.zeros((3, 3))


    logging.info('Beginning matrix operations!')

    print(Wahoovian_Transformation.wahoovian(m1))
    print(Wahoovian_Transformation.wahoovian(m2))
    print(Wahoovian_Transformation.wahoovian(m4))

    logging.info('Program ends!')



if __name__ == '__main__':
    main()

# What's the magic of the code right before this?
#    If this file is named main.py and it's run with:  python main.py
#       then the if is True and main() is executed.
#    But, if this file is imported then the method main() is defined but not executed.