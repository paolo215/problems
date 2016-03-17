import random
import Point
import Closest

def DivideAndConquer(xP, yP):
    if len(xP) <= 3:
        a,b = Closest.Closest(xP)
        d = a.distance(b)
        return (a, b), d
    xL = xP[0:int(len(xP)/2)+1]
    xR = xP[int(len(xP)/2):len(xP)]
    xmid = xP[len(xP)/2].x
    yL = [f for f in yP if f.x < xmid]
    yR = [f for f in yP if f.x >= xmid]

    (pairL, distL) = DivideAndConquer(xL, yL)
    (pairR, distR) = DivideAndConquer(xR, yR)
    minPair, minDist = pairR, distR
    if (distL < distR):
        minPair, minDist = pairL, distL

    yS = [p for p in yP if abs(xmid - p.x) < minDist]
    nS = len(yS)
    (bestPair, bestDist) = (minPair, minDist)
    for i in range(0, nS-2):
        k = i + 1
        while k < nS and yS[k].y - yS[i].y < minDist:
            dist = yS[i].distance(yS[k])
            if dist < bestDist:
                (bestPair, bestDist) = (yS[k], yS[i]), dist
            k = k+1

    return bestPair, bestDist

def p(arr):
    for i in arr:
        print i
    print "-"

n = 10
P = [Point.Point(random.randint(0, n), random.randint(0, n)) for f in range(n)]
xP = sorted(P, key=lambda s: s.x)
xY = sorted(P, key=lambda s: s.y)

p(xP)
a,b = DivideAndConquer(xP, xY)
p(a)
print b
