#!/usr/bin/env python3


# Testing Serialization modules in Python. Test list:
#


import pickle

class account:
	def __init__(self, id, balance):
		self.id = id
		self.balance = balance
	def deposit(self, amount):
		self.balance += amount
	def withdraw(self, amount):
		self.balance -= amount

                
class PickleTest:

    def run_test(self):
        myac = account('123', 100)
        myac.deposit(800)
        myac.withdraw(500)
        with open( "archive", "wb" )  as fd:
            pickle.dump( myac, fd)
        myac.deposit(200)
        print (myac.balance)
        with open( "archive", "rb" ) as fd:
            myac = pickle.load( fd )
        print (myac.balance)
        
