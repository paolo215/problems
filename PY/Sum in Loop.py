#pvprograms.weebly.com
#Sum in Loop

test = int(input())
a = input()
a = a.split(' ')
for i in range(test):
    a[i] = int(a[i])
print(sum(a))
