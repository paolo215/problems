#Rotate String

test = int(input())
for a in range(test):
    a = input()
    a = a.split(' ')
    num = int(a[0])
    if num > 0:
        k = a[1][0:num]
        a[1] = a[1][num:len(a[1])]
        print(a[1] + k, end=' ')
    else:
        k = a[1][num:]
        a[1]  = a[1][0:num]
        print(k + a[1], end=' ')
        
