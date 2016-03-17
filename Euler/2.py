#Even Fibonacci numbers
F = [0,1]
i = 2
while(F[i-1] <= 4000000):
    F.append(F[i-1] + F[i-2])
    i += 1

print sum([f for f in F if f % 2 == 0])
