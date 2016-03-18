
def count(n):
    return sum([1 for i in range(1, (n//2) + 1) if not n % i])


def triangle(i):
    return int((i * (i+1))/2)

assert count(21) == 3
assert count(28) == 5
i = 1
while(count(triangle(i)) <= 500):
    i += 1
print triangle(i)
