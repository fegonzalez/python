
import unittest # Unit Test standard library 
# WARNING Never name your own script unittest.py as the standard library module.
# 	...  AttributeError: 'module' object has no attribute 'TestCase'

        
# Import functions to be tested
# from rpsls import rpsls
from rpsls import _get_winner
from rpsls import name_to_number
from rpsls import number_to_name


##==============================================================================
            
# Test unit
class TestRpsls(unittest.TestCase):

    def setUp(self):
        pass

    # test
    def test_winners(self): 
        # rock wins
        self.assertEqual(_get_winner("scissors","rock"), 2)
        self.assertEqual(_get_winner("rock","scissors"), 1)
        self.assertEqual(_get_winner("lizard","rock"), 2)
        self.assertEqual(_get_winner("rock","lizard"), 1)
        # paper wins
        self.assertEqual(_get_winner("spock","paper"), 2)
        self.assertEqual(_get_winner("paper","spock"), 1)
        self.assertEqual(_get_winner("rock","paper"), 2)
        self.assertEqual(_get_winner("paper","rock"), 1)
        # scissors wins
        self.assertEqual(_get_winner("lizard","scissors"), 2)
        self.assertEqual(_get_winner("scissors","lizard"), 1)
        self.assertEqual(_get_winner("paper","scissors"), 2)
        self.assertEqual(_get_winner("scissors","paper"), 1)
        # spock wins
        self.assertEqual(_get_winner("rock","spock"), 2)
        self.assertEqual(_get_winner("spock","rock"), 1)
        self.assertEqual(_get_winner("scissors","spock"), 2)
        self.assertEqual(_get_winner("spock","scissors"), 1)
        # lizard wins
        self.assertEqual(_get_winner("paper","lizard"), 2)
        self.assertEqual(_get_winner("lizard","paper"), 1)
        self.assertEqual(_get_winner("spock","lizard"), 2)
        self.assertEqual(_get_winner("lizard","spock"), 1)
        #ties
        {"rock":1, "paper":2, "scissors":3, "spock":4, "lizard":5 }
        self.assertEqual(_get_winner("rock","rock"), 0)
        self.assertEqual(_get_winner("paper","paper"), 0)
        self.assertEqual(_get_winner("scissors","scissors"), 0)
        self.assertEqual(_get_winner("spock","spock"), 0)
        self.assertEqual(_get_winner("lizard","lizard"), 0)

    def test_name2number(self): 
        self.assertEqual(name_to_number("rock"), 1)
        self.assertEqual(name_to_number("paper"), 2)
        self.assertEqual(name_to_number("scissors"), 3)
        self.assertEqual(name_to_number("spock"), 4)
        self.assertEqual(name_to_number("lizard"), 5)
        self.assertEqual(name_to_number("lizARd"), 5)

    def test_number2name(self): 
        self.assertEqual(number_to_name(1), "rock")
        self.assertEqual(number_to_name(2), "paper")
        self.assertEqual(number_to_name(3), "scissors")
        self.assertEqual(number_to_name(4), "spock")
        self.assertEqual(number_to_name(5), "lizard")




##==============================================================================

# # Test Unit: several test cases may be included (test_ functions)
# class TestStatisticalFunctions(unittest.TestCase):

#     def test_average(self):    # Test function
#         self.assertEqual(average([20, 30, 70]), 40.0)       # test
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3) # test
#         with self.assertRaises(ZeroDivisionError):
#             average([])
#         with self.assertRaises(TypeError):
#             average(20, 30, 70)

 
##==============================================================================
            
if __name__ == '__main__':
    unittest.main()


# shell use:
# python3 rpsls_unittest.py
#
 
##==============================================================================

