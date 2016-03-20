#Non-abundant sums

def sumDivisors(n):
    s = 0
    for i in range(1, int(n//2) + 1):
        if n % i == 0:
            s += i
    return s


s = []
a = 0



for i in range(1, 28123):
    if sumDivisors(i) > i:
        s.append(i)
    


print s
