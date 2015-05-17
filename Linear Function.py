#Linear Function

test = int(input())

for i in range(test):
    a = input()
    a = a.split(' ')
    y = int(a[1]) - int(a[3])
    x = int(a[0]) - int(a[2])
    slope = int(y / x)
    b = (int(a[1]) - int((slope * int(a[0]))))
    print("(" + str(slope) + " " + str(b) + ") ")
