#Collatz sequence
def collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return (3*n) + 1

a = []
for i in range(1, 1000000):
    count = 1
    b = collatz(i)
    while(b != 1):
        b = collatz(b)
        count += 1
    a.append((i, count))
print max(a, key=lambda x : x[1])
