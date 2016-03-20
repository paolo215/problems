#Lattice path
#Wiki'd the formula for Lattice path
import math

def nCk(n, k):
    f = math.factorial
    return (f(n) / (f(n-k) * f(k)))

print nCk(20+20, 20)
