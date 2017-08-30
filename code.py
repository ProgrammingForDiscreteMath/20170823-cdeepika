"""
This is the code file for Assignment from 23rd August 2017.
This is due on 30th August 2017.
"""
##################################################
#Complete the functions as specified by docstrings
# Coded in Python 3

# 1

def entries_less_than_ten(L):
    """
    Return those elements of L which are less than ten.

    Args:
        L: a list

    Returns:
        A sublist of L consisting of those entries which are less than 10.
    """
    return [i for i in L if  i< 10]

#Test
#print entries_less_than_ten([2, 13, 4, 66, -5]) == [2, 4, 6, -5]
# This test has a spelling mistake. Assuming it is 6 and not 66. - Deepika 

# 2

def number_of_negatives(L):
    """
    Return the number of negative numbers in L.

    Args:
        L: list of integers

    Returns:
        number of entries of L which are negative
    """
    #same logic as #1
    l = [i for i in L if  i< 0]
    return len(l)

# TEST
#print number_of_negatives([2, -1, 3, 0, -1, 0, -45, 21]) == 3

# 3
def common_elements(L1, L2):
    """
    Return the common elements of lists ``L1`` and ``L2``.

    Args:
        L1: List
        L2: List

    Returns:
        A list whose elements are the common elements of ``L1`` and
        ``L2`` WITHOUT DUPLICATES.
    """
    return list(set([i for i in L1 if i in L2]))

#TEST
#common_elements([1, 2, 1, 4, "bio", 6, 1], [4, 4, 2, 1, 3, 5]) == [1, 2, 4]

#4
def fibonacci_generator():
    """
    Generate the Fibonacci sequence.

    The Fibonacci sequence 1, 1, 2, 3, 5, 8, 13, 21,...
    is defined by a1=1, a2=1, and an = a(n-1) + a(n-2).
    """
    a1 = 1
    a2 = 1
    while True:
        yield a1
        a1, a2 = a2, a1 + a2
#TEST
#f = fibonacci()
# Use f.__next__() for printing. It gives individual elements but doesn't fit in the test provided. 
#Throws AttributeError.
#[f.next() for f in range(10)] == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#5
def largest_fibonacci_before(n):
    """
    Return the largest Fibonacci number less than ``n``.
    """
    #read output of above generator upto ``n`` into a list ``l`` and print the preceding index.
    #len(l) -1 => index of ``n``
    return l[len(l)-2] 
#TEST
#largest-fibonacci_before(55) == 34

#6
def catalan_generator():
    """
    Generate the sequence of Catalan numbers.

    For the definition of the Catalan number sequence see `OEIS <https://www.oeis.org/A000108>`.
    """
    pass #Your code goes here.

#TEST
#c = catalan_generator()
#[c.next() for i in range(10)] == [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
 
#7
### CREATE YOUR OWN FUNCTION. Make sure it has a nice docstring.
# See https://www.python.org/dev/peps/pep-0257/
# for basic tips on docstrings.
def fibonacci(n):
    """
    Returns a list of fibonacci series of length ''n''.
    """
    l=[]
    x,y = 0,1
    for i in range(n):
        n = x+y
        l.append(n)
        x,y = y,y+1
    return l
##TEST
#fibonacci(5) == [1, 3, 5, 7, 9]