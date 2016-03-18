#10,001th prime number
#Referencing ../PY/Sieves of Erathosthenes.py

limit = 5000000
a = [True] * (limit + 1)
primes = []

for i in range(2, limit+1):
    if len(primes) >= 10001:
        break
    if a[i]:
        primes.append(i)
        for z in range(i*i, limit + 1, i):
            a[z] = False
    
print primes[1000-1]
