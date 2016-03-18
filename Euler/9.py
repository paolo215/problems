
limit = 1000
def check(a,b,c):
    return (a**2) + (b**2) == (c**2)

for a in range(1, limit):
    for b in range(a+1, limit):
        c = limit - (a + b)
        if check(a, b, c) == True and sum([a,b,c]) == limit:
            print a * b * c
            break
