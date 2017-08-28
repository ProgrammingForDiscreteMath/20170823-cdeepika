# Create a list with the first ten triangular numbers
 
##Codes in Python 3 -Deepika
L = [(i*(i+1)/2) for i in range(10)]

# Create a function to test if a number is prime
def is_prime(n):
    """
    Test if `n` is a prime.
    """
    for i in range(2,n):
        if n%i ==0:
            print("FALSE")
            break
        else:
            print("TRUE")
            break
# Tests
# is_prime(2033) == False
# is_prime(2039) == True

# Create a function which returns a list of the first ten prime numbers
# greater than or equal to n

def next_ten_primes(n):
    """
    Return the list of the first ten prime numbers greate than or equal to n
    
    """
    l = list()
    
    while len(l) != 10:
        for i in range(n, n/2.0 + 1.0):
            if n%i ==0:
                break
            else:
                l.append(n)
            n += 1
    return l
# Tests
# next_ten_primes(2033) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]
# next_ten_primes(2039) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]
