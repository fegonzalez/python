
# Testing argument types

# positional + optional + Keyword Arguments
def fname(b, a=5, alist=[]):
    alist.append(b)
    print(a, b, alist)


# Arbitrary Argument Lists

def concat(*args, sep="/"): # (*args): args must be = str
    return sep.join(args)

def print_array(*args): # (*args): args can be an array of any type
    print (args)



# dictionary Argument Lists
#
# call example:
# 1) d = {"key1": "value1", "key2": "value2"}  # type(d) == <class 'dict'>
# 2) test_functions.print_dict(**d)
def print_dict(**dict_args): # dict_args must be a (**dict)
    print (dict_args)
    

    
