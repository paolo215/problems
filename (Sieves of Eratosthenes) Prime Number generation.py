#https://github.com/paolo215
def primes(cap=5000000):
    a = input()
    data = input()
    data = data.split(" ")
    data = list(map(int, data))
    primes = []
    sieves = [True] * (cap + 1)
    for i in range(2, cap+1):
        if len(primes) > max(data):
            break
        if sieves[i]:
            primes.append(i)
            for z in range(i*i, cap + 1, i):
                sieves[z] = False
    answers = [str(primes[f-1]) for f in data]
    print(" ".join(answers))


primes()
