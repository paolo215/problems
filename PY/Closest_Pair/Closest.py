import Point
import random

n = 10
A = [Point.Point(random.randint(0,10), random.randint(0,10)) for f in range(n)]


def Closest(A):
    minDistance = float("inf")
    closestPair = None
    for i in range(0, len(A)-1):
        for j in range(i+1, len(A)):
            p = A[i]
            q = A[j]
            if p.distance(q) < minDistance:
                minDistance = p.distance(q)
                closestPair = (p,q)
    return closestPair

