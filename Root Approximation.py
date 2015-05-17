#Root Approximation

test = int(input())
for i in range(test):
    a = input()
    a = a.split(' ')
    value = int(a[0])
    runs = int(a[1])
    r = 1

    for a in range(runs):
        d = value/r
        abs(r-d)
        r = (r+d)/2
    print(round(r,11), end = ' ')
   
        

    
