######################################################################
# Author: Tom West Ela jamali
# Username: Westth Jamalie
#
# Assignment: T12: Modules
#
# Purpose: A special game from my (and likely, many of your) childhood
#
######################################################################
# Acknowledgements:
#
# Idea inspired by original code from: https://michael0x2a.com/blog/turtle-examples
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import sys

from t12_dots import *

def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text

    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def calulate_size_test_suite():
    """runs test on calculate size """
    testit(calculate_size(9)== (3,3) )
    testit(calculate_size(16)== (4,4) )
    testit(calculate_size(25)== (5,5) )
    testit(calculate_size(4)== (2,2) )
    testit(calculate_size(5) == (1,5))
    testit(calculate_size(10) == (2,5))
    testit(calculate_size(7) == (1,7))
    testit(calculate_size(11) == (1,11))
    #testit(calculate_size("eleven")=="Error")


def valid_size_test_suit():
    """runs test on is valid size"""
    testit(is_valid_size(70, 70, 70, 1100, 650) == False)
    testit(is_valid_size(50, 50, 50, 1100, 650) == False)
    testit(is_valid_size(20, 20, 20, 1100, 650) == True)
    testit(is_valid_size(10, 10, 10, 1100, 650) == True)






def main():
    calulate_size_test_suite()
    valid_size_test_suit()

if __name__ == "__main__":
    main()
