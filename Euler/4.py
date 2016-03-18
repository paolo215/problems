#Largest palindrome product
a = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a.append(i*j)

a = map(str, reversed(sorted(list(set(a)))))
for z in a:
    if z == "".join(reversed(list(z))):
        print z
        break
