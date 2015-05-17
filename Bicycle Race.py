#Bicycle Race

test = int(input())
for i in range(test):
    a = input()
    a = a.split(' ')
    time = (int(a[0]) / (int(a[1]) + int(a[2])))
    dist = int(a[1])
    dist = dist * time
    print(str(round(dist,12)), end=' ')
    
