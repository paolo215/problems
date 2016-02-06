import Point
import random

n = 10
A = [Point.Point(random.randint(0,10), random.randint(0,10)) for f in range(n)]

for i in A:
    print i

minDistance = float("inf")
closestPair = None
for i in range(1, n-1):
    for j in range(i+1, n):
        p = A[i]
        q = A[j]
        if p.distance(q) < minDistance:
            minDistance = p.distance(q)
            closestPair = (p,q)

print closestPair[0], closestPair[1]
