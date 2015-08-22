#!/usr/bin/env python3

# \file file_lib_unittest.py
# Python file library's test set.
# date: 2015-08-22
# Author: Fernando Gonzalez Rodriguez

#===============================================================================

#NOTICE Using from the  shell:
# python3 eco_ecuations_unittest.py
# python3 -m eco_ecuations_unittest 

#===============================================================================


import unittest # Unit Test standard library 
# WARNING Never name your own script unittest.py as the standard library module.
# 	...  AttributeError: 'module' object has no attribute 'TestCase'


from file_lib import skip_blanks
from file_lib import skip_comments
from file_lib import skip_blanks_and_comments


#===============================================================================

_SINGLE_COMMENTS_FILE = "comment_test.data"
_MULTI_COMMENTS_FILE = "multicomment_test.data"
_BLANKS_FILE = "blanks_test.data"
_BLANKS_AND_SINGLECOMMENTS_FILE = "blanks_singlecomments_test.data"
_BLANKS_AND_MULTICOMMENTS_FILE = "blanks_multicomments_test.data"
_BLANKS_SAMPLE=" \t\n"
_SINGLE_COMMENT_SAMPLE = ["#"]
_MULTIPLE_COMMENT_SAMPLE =['#', '%', '//']
_EXPECTED_CLEAN_DATA={"PARAMETER_DOG": 1,
                      "ANOTHER_VALUE": 3,
                      "YET_ANOTHER_VALUE": 34,
                      "FINAL_VALUE": 22}
            
_EXPECTED_UNCOMMENTS_FILE = ' PARAMETER_DOG 1\nANOTHER_VALUE 3\n    YET_ANOTHER_VALUE 34\nFINAL_VALUE 22  \n'
        
#===============================================================================
# Test Unit
#===============================================================================

class TesEcuations(unittest.TestCase):

    def setUp(self):
        pass
    
    #-------------------------
    
    def test_skip_single_comments(self):
        obtained=""
        with open(_SINGLE_COMMENTS_FILE, 'r') as afile:
            for line in skip_comments(afile):
                obtained+=line
        self.assertEqual(obtained, _EXPECTED_UNCOMMENTS_FILE)

    #-------------------------
    
    def test_skip_multiple_comments(self):
        obtained=""
        with open(_MULTI_COMMENTS_FILE, 'r') as afile:
            for line in skip_comments(afile, _MULTIPLE_COMMENT_SAMPLE):
                obtained+=line
        self.assertEqual(obtained, _EXPECTED_UNCOMMENTS_FILE)

    #-------------------------
    
    def test_skip_blanks(self):
        obtained={}
        with open(_BLANKS_FILE, 'r') as afile:
            for line in skip_blanks(afile):
                separate_values = line.split()
                assert(len(separate_values)==2)
                obtained[separate_values[0]] = int (separate_values[1])
        self.assertEqual(obtained, _EXPECTED_CLEAN_DATA)

    #-------------------------
    
    def test_skip_blanks_and_single_comments(self):
        obtained={}
        with open(_BLANKS_AND_SINGLECOMMENTS_FILE, 'r') as afile:
            for line in skip_blanks_and_comments(afile):
                separate_values = line.split()
                assert(len(separate_values)==2)
                obtained[separate_values[0]] = int (separate_values[1])
        self.assertEqual(obtained, _EXPECTED_CLEAN_DATA)

    #-------------------------
    
    def test_skip_blanks_and_multiple_comments(self):
        obtained={}
        with open(_BLANKS_AND_MULTICOMMENTS_FILE, 'r') as afile:
            for line in skip_blanks_and_comments(afile, _BLANKS_SAMPLE, _MULTIPLE_COMMENT_SAMPLE):
                separate_values = line.split()
                assert(len(separate_values)==2)
                obtained[separate_values[0]] = int (separate_values[1])
        self.assertEqual(obtained, _EXPECTED_CLEAN_DATA)

    #-------------------------



#===============================================================================
        
if __name__ == '__main__':
    unittest.main()

#===============================================================================

