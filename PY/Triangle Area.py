#https://github.com/paolo215

def distance(v1, v2):
    return ((v2[0] - v1[0]) ** 2 + (v2[1] - v1[1]) ** 2) ** (1/2)

def hero(v1, v2, v3):
    a = distance(v1, v2)
    b = distance(v2, v3)
    c = distance(v3, v1)
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** (1/2)

test = int(input())
for i in range(test):
    data = input()
    data = data.split(" ")
    iterable = iter(data)
    arr = []
    for z in iterable:
        arr.append((int(z), int(next(iterable))))
    print("{:.7f}".format(hero(*arr)), end=" ")
