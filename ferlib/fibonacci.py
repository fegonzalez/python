#!/Users/jc/.virtualenvs/env1/bin/python
# -*- coding: utf-8 -*-

def fib(n): #Returns the list with the Fibonacci series up to n.
    """ Returns the list with the Fibonacci series up to n. """
    retval=[]
    a, b = 0, 1
    while a<n:
        retval.append(a)
        a, b = b, a+b # Parallel assignment
    return retval

 
    ### to test script: this code only runs if the module is executed as script
if __name__ == '__main__':
    print("\n... fibonacci.py: script test\n")
    assert fib(0)==[]
    print("fib(0) = ", fib(0))
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
                987, 1597];
    obtained=fib(2000);
    print("fib(2000) = ", obtained)
    assert obtained==expected
    print("\n... test OK\n")

