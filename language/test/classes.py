#!/usr/bin/env python3

# Testing Classes in Python. Test list:
#
# \class MyComplexTest:
# \test class variables vs instance variables
# \test function overloading
#
# \class SelfTest:
# \test self
#
# \class FuncTest:
# \test BAD PRACTICE: Strange but valid function assignment / function use
#
# \class ReadOnlyTest:
# \test read-only variables (property / decorators)

# \class NameOverrideTest:
# \test Data attributes override method attrs. with the same name -> trick bugs.

# \class StudentAthlete:
# \test Multiple Inheritance in Python (included diamond inheritance)

# \class ReverseIterator:
# \test Iterator behavior in user classes.

##==============================================================================

from enum import Enum, unique


##==============================================================================
# \class MyComplexTest:
# \test class variables vs instance variables
# \test function overloading
##==============================================================================

class MyComplexTest:

    the_class_attr = "I am a 'Class variable', thus I am shared by all the object instances of this class"

    def __init__(self, realpart=0.0, imagpart=0.0):    # c012 
        self.the_real = realpart
        self.the_imag = imagpart
    
        
    # WARNING Function overloading not valid in Python. If more than one are
    # written, all but the last one are ignored by the interpreter.

    # def class_method(self, mas_param):
    #     print("two arguments required))

    def class_method(self):
        print(self.the_real)
        print("Calling a class variable inside a method:", self.the_class_attr);
    
        

##==============================================================================
# \class SelfTest:
# \test self
##==============================================================================

class SelfTest:
    """A simple example class: Includes 'self' use example"""
    i = 12345;

    def f1(self):
        return 'hello world'        

    def f2(antonio):
        print("self OR antonio, it doesn't matters")

    ## TypeError: f3() takes 0 positional arguments but 1 was given
    # def f3(): 
    #     return 'hello world'        

        
##==============================================================================
# \class FuncTest:
# \test BAD PRACTICE: Strange but valid function assignment / function use
##==============================================================================

def f1(self, x, y): # Function defined outside the class
    return min(x, x+y)

class FuncTest:
    f = f1
    def g(self):
        return 'hello world'
    h = g

# Example of use.-     
#
# >>> fo=classes.FuncTest()    
#
# >>> classes.f1(fo, 1,2)
# 1
# >>> classes.f1(fo, 1,2)
# 1
#
# >>> fo.f(3,4)
# 3
# >>> fo.g()
# 'hello world'
# >>> fo.h()
# 'hello world'



##==============================================================================
# \class ReadOnlyTest:
# \test read-only variables (property / decorators)
##==============================================================================

class ReadOnlyTest(object):
    def __init__(self, the_ro_param):
        self.__the_ro_param = the_ro_param

    # WARNING @property overrides (alias) attribute 'the_ro_param', NOT the
    # method the_ro_param()
    @property  
    def the_ro_param(self):
        return self.__the_ro_param


            
  # use example.-
  # >>> a = ReadOnlyTest('test')
  # >>> a.the_ro_param
  # 'test'
  # >>> a.the_ro_param = 'pleh'
  # AttributeError: can't set attribute

  
##==============================================================================
# \class NameOverrideTest:
# \test Data attributes override method attrs. with the same name -> trick bugs.
##==============================================================================

class NameOverrideTest:

    name_class_var = "class variable 'name_class_var'"
    
    def __init__(self):
        self.name_instance_var = "instance variable 'name_instance_var'";

    def name_instance_var(self):
        print("function 'name_instance_var'")

    def name_class_var(self):
        print("function 'name_class_var'")

    def not_override_method(self):
        print("function 'not_override_method'")

    def name_class_var_after_method(self):
        print("function 'name_class_var_after_method'")

    name_class_var_after_method = "class variable 'name_class_var_after_method'"


# Example.-
#
# >>> nameover = classes.NameOverrideTest()
# >>> nameover.name_instance_var
# "instance variable 'name_instance_var'"
# >>> nameover.name_class_var
# <bound method NameOverrideTest.name_class_var of <classes.NameOverrideTest...
# >>> nameover.name_instance_var()
# TypeError: 'str' object is not callable
# >>> nameover.name_class_var()
# function 'name_class_var'
# >>> nameover.not_override_method()
# function 'not_override_method'
# >>> nameover.name_class_var_after_method
# "class variable 'name_class_var_after_method'"
# >>> nameover.name_class_var_after_method()
# TypeError: 'str' object is not callable
# 
# Conclussions:

# Checked: when two attribute references (one var & one method) are defined
# with the same name, the one defined later in the class is the one used by the
# Python interpreter; all the others raise 'TypeError'.


##==============================================================================
# \class StudentAthlete:
# \test Multiple Inheritance in Python (included diamond inheritance)
##==============================================================================

@unique
class GenderEnum(Enum):
    Male=1
    Female=2

# genero=classes.GenderEnum.Female
# if genero==classes.GenderEnum.Female:

##------------------------------------------------------------------------------

class Person:

    def __init__(self,
                 name,
                 age,
                 gender, # GenderEnum value required
                 employed = False,
                 address="Unknown"):
        assert(isinstance(gender, GenderEnum))
        self._name = name
        self._age = age
        self._gender = gender
        self.address = address
        self.employed = employed

    @property # use: object.name  (NOT object.name())
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender.name

    def __str__(self):
        retval = "(" + str(self.name) + ", " + str(self.age)+ ", " + str(self.gender) + ", " + str(self.address) + ", " + str(self.employed) + ")"
        return retval        

    def my_class_is(self):
        print("My data type is: ", self.__class__)
    
##------------------------------------------------------------------------------

class Student(Person):

    _id = 0

    # ERROR: NOT compilation error (like C++), instead creates the object
    # without the Base attributes
    #     
    # def __init__(self, subject):  # subject example = "History"
    #     self._id+=1
    #     self.subject=subject

    def __init__(self,
                 subject,
                 name,
                 age,
                 gender, # GenderEnum value required
                 employed = False,
                 address="Unknown"):
        Person.__init__(self, name, age, gender, employed, address)
        self._id+=1
        self.subject=subject

    
    @property
    def id(self):
        return self._id

    def __str__(self):
        retval = Person.__str__(self) + "(" + str(self.id) + ", " + str(self.subject) + ")"
        return retval        

    

##------------------------------------------------------------------------------

class Athlete(Person):

    _id = 0

    def __init__(self,
                 sport,
                 name,
                 age,
                 gender, # GenderEnum value required
                 employed = False,
                 address="Unknown"):
        Person.__init__(self, name, age, gender, employed, address)
        self._id+=1
        self.sport=sport

    @property
    def id(self):
        return self._id


    def __str__(self):
        retval = Person.__str__(self) + "(" + str(self.id) + ", " + str(self.sport) + ")"
        return retval  
    
##------------------------------------------------------------------------------
# \class StudentAthlete:
# \test Multiple Inheritance in Python.
##------------------------------------------------------------------------------

# ERROR How to call both fathers ???
class StudentAthlete(Student, Athlete):

    def __init__(self,
                 subject,
                 sport,
                 name,
                 age,
                 gender, # GenderEnum value required
                 employed = False,
                 address="Unknown"):
        Student.__init__(self, subject, name, age, gender, employed, address)
        Athlete.__init__(self, sport, "weeeee", age, gender, employed, address)
        self._id+=1

        
    # def __str__(self):
    #     return Student.__str__(self) + Athlete.__str__(self)



##==============================================================================
# \class ReverseIterator:
# \test Iterator behavior in user classes.
##==============================================================================

class ReverseIterator:

    def __init__(self, data):
        self.data = data
        self._index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index==0:
            raise StopIteration
        self._index-=1        
        return self.data[self._index]

# use:
# >>> rev=classes.ReverseIterator("spam")
# >>> for char in rev:
# ...     print(char)
# m
# a
# p
# s

# EOF
