#https://github.com/paolo215
def primes(idxLimit, cap=5000000):
    primes = []
    sieves = [True] * (cap + 1)
    for i in range(2, cap+1):
        if idxLimit and len(primes) >= idxLimit:
            break
        if sieves[i]:
            primes.append(i)
            for z in range(i*i, cap + 1, i):
                sieves[z] = False
    return primes 

if __name__ == "__main__":
    primes()
