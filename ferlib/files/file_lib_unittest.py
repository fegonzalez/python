#!/usr/bin/env python3

#===============================================================================

#NOTICE Using from the  shell:
# python3 eco_ecuations_unittest.py
# python3 -m eco_ecuations_unittest 

#===============================================================================

_EXAMPLE_SIMPLE_FILE = "file_lib_test.data"
_EXAMPLE_MULTCOMMENT_FILE = "filelib_multicomment_test.data"
_BLANKS_SAMPLE=" \t\n"
_SINGLE_COMMENT_SAMPLE = "#"
_MULTIPLE_COMMENT_SAMPLE = "# % //" # split()) is ['#', '%', '//']



import unittest # Unit Test standard library 
# WARNING Never name your own script unittest.py as the standard library module.
# 	...  AttributeError: 'module' object has no attribute 'TestCase'

from file_lib import skip_blanks
from file_lib import skip_comments
from file_lib import skip_blanks_and_comments


#===============================================================================
# Test Unit
#===============================================================================

class TesEcuations(unittest.TestCase):

    def setUp(self):
        pass

    #-------------------------
    
    # def test_compound_interest(self):
    #     self.assertAlmostEqual(compound_interest(500, .04, 10, 10), \
    #                            745.317442824) #, places=7, msg=None, delta=None)


    #-------------------------
    
    def test_skipcomments(self):
        self.assertAlmostEqual(compound_interest(500, .04, 10, 10), \
                               745.317442824) #, places=7, msg=None, delta=None)

    #-------------------------



def _parse_trading_errors_file():
    """ return markets from file"""
    ret_value={}
    with open(_TRADING_ERRORS_FILE, 'r') as afile:
        # for line in (l.strip(_BLANKS) for l in skip_comments_and_blanks(afile)):
        for line in (l.strip(_BLANKS) for l in skip_comments(afile)):
            separate_values = line.split()
            print(separate_values)
            assert(len(separate_values)==2)
            ret_value[separate_values[0]] = separate_values[1]
 
    return ret_value

#------------------------------------------------------


#-------------------------------------------------------------------------------


#===============================================================================
        
if __name__ == '__main__':
    unittest.main()

#===============================================================================

