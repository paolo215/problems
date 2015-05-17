#pvprograms.weebly.com
#Minimum of Three

test = int(input())
for i in range(test):
    a = input()
    a = a.split(' ')
    #turn it to int
    for b in range(len(a)):
        a[b] = int(a[b])
    #find min
    minimum = a[0]
    for c in range(len(a)):
        if a[c] < minimum:
            minimum = a[c]
    print(minimum, end=' ')

