from math import sqrt

class Fibonacci:

    GOLDEN_RATIO = (1 + sqrt(5)) / 2

    @staticmethod
    def recursive(n):
        if n <= 1: return n
        return Fibonacci.recursive(n - 1) + Fibonacci.recursive(n - 2)
    
    @staticmethod
    def iterative(n):
        if n <= 1: return n
        a, b = 1, 0
        for i in range(2, n + 1):
            a, b = a + b, a
        return a
    
    @staticmethod
    def binets_formula(n): # Note that binet's formula has growing inaccuracy for large inputs
        phi = Fibonacci.GOLDEN_RATIO
        return (phi**n - (1 - phi)**n) / sqrt(5)
