"""
Class for an actual element of the field. Contains all the 
relevant operations. The GaloisField class should store an
array of these when it creates the field.

This is separate from the main field so that it has it's own type
and we can do things like
GF8[4] + GF8[2],
rather than
GF8.add(4, 2)
and thus store the field elements in individual variables for
later use.
"""

import math

class FieldElement():
    """
    Initialize a field element given the field dimensions
    and the expansion coefficients.
    """
    def __init__(self, p, n, exp_coefs):
        self.p = p
        self.n = n

        # Set the expansion coefficients.
        # If we're in a prime field, the basis is 1, and
        # the coefficient is just the value
        self.exp_coefs = exp_coefs


    """
    Add two elements together. Simple modulo for primes, 
    need to deal with the coefficients modulo p for the 
    extended case.
    """
    def __add__(self, el):
        # Make sure we're in the same field!
        if self.p != el.p:
            print("Error, cannot add elements from different fields!")
            return None
        if self.n != el.n:
            print("Error, cannot add elements from different fields!")
            return None

        # Prime case
        if self.n == 1:
            return FieldElement(self.p, self.n, [(self.exp_coefs[0] + el.exp_coefs[0]) % self.p])
        # Power of prime case
        else:
            print("Under construction!")
        
    
    """
    Compute the difference of two elements. Simple modulo for primes, 
    need to deal with the coefficients modulo p for the 
    extended case.
    """
    def __sub__(self, el):
        # Make sure we're in the same field!
        if self.p != el.p:
            print("Error, cannot add elements from different fields!")
            return None
        if self.n != el.n:
            print("Error, cannot add elements from different fields!")
            return None

        # Prime case
        if self.n == 1:
            return FieldElement(self.p, self.n, [(self.exp_coefs[0] - el.exp_coefs[0]) % self.p])
        # Power of prime case
        else:
            print("Under construction!")


    """
    Compute the product of two elements. Simple modulo for primes, 
    need to deal with the coefficients modulo p for the 
    extended case.
    """
    def __mul__(self, el):
        # Make sure we're in the same field!
        if self.p != el.p:
            print("Error, cannot add elements from different fields!")
            return None
        if self.n != el.n:
            print("Error, cannot add elements from different fields!")
            return None

        # Prime case
        if self.n == 1:
            return FieldElement(self.p, self.n, [(self.exp_coefs[0] * el.exp_coefs[0]) % self.p])
        # Power of prime case
        else:
            print("Under construction!")


    """
    Compute the power. Simple modulo for primes, 
    need to deal with the coefficients modulo p for the 
    extended case.
    """
    def __pow__(self, exponent):
        # Prime case
        if self.n == 1:
            return FieldElement(self.p, self.n, [int(math.pow(self.exp_coefs[0], exponent)) % self.p])
        # Power of prime case
        else:
            print("Under construction!")


    """ 
    Compute the trace. The formula just relies on the pow function so
    it has the same implementation for prime and powers of prime.
    The sum should be an element of the base field for power of prime case.
    """
    def trace(self):
        sum = self

        for i in range(1, self.n):
            sum = sum + pow(self, pow(self.p, i))

        return sum


    def __repr__(self):
        if self.n == 1:
            return str(self.exp_coefs[0])
        else:
            return str(self.exp_coefs)


    """ 
    Print out information about the element.
    """
    def print(self):
        if self.n == 1:
            print(self.exp_coefs[0])
        else:
            print(self.exp_coefs)


