#https://github.com/paolo215
string = input()
string = string.split(" ")
a = []
for i in string:
    add = [i, string.count(i)]
    if add not in a:
        a.append(add)

a = sorted(a, key=(lambda s: s[0]))
current = a[0]
idx = 0
for i in a:
    if i[1] > 1:
        print(i[0], end=" ")

