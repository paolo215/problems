#pvprograms.weebly.com
#Minimum of Two

test = int(input())
for i in range(test):
    a = input()
    a = a.split(' ')
    if(int(a[0]) < int(a[1])):
        print(a[0], end=' ')
    else:
        print(a[1], end=' ')
    
