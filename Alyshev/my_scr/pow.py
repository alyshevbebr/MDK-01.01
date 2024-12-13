import math as m
class PoW():#ig
    def pow2(a):
        return a**2
    def pow2_math(a):
        return m.pow(a,2)
    def pow3_math(a):
        return m.pow(a,3)

def find_fibonacci(n): 
    if n == 0:
        return 1
    return find_fibonacci(n-1) + find_fibonacci(n-2)


