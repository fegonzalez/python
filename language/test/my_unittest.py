
import unittest # Unit Test standard library 
# WARNING Never name your own script unittest.py as the standard library module.
# 	...  AttributeError: 'module' object has no attribute 'TestCase'

        
# Import functions to be tested
from standard_lib import multiply 
from standard_lib import average

 
##==============================================================================

# Test Unit: several test cases may be included (test_ functions)
class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):    # Test function
        self.assertEqual(average([20, 30, 70]), 40.0)       # test
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3) # test
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

##==============================================================================
            
# Test unit
class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    # test
    def test_numbers_3_4(self): 
        self.assertEqual( multiply(3,4), 12)

    # test
    def test_strings_a_3(self):
        self.assertEqual( multiply('a',3), 'aaa')


        
if __name__ == '__main__':
    unittest.main()



# b) shell:
# python3 my_unittest.py
#


### SUCCESS test EXAMPLE
#
# OK test
# Ran 3 tests in 0.000s
# OK


### ERROR test EXAMPLE
#
#  bash-3.2$ python3 my_unittest.py
# ..F
# ======================================================================
# FAIL: test_strings_a_3 (__main__.TestUM)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "my_unittest.py", line 39, in test_strings_a_3
#     self.assertEqual( multiply('a',3), 'aaB')
# AssertionError: 'aaa' != 'aaB'
# - aaa
# ?   ^
# + aaB
# ?   ^
# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s
#
# FAILED (failures=1)
# bash-3.2$


