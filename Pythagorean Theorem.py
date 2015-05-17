#Pythagorean Theorem

test = int(input())
for i in range(test):
    num = input()
    num = num.split(' ')
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    add = a**2 + b**2
    if(c**2 < add):
        print("A",end=' ')
    elif(c**2 == add):
        print("R",end=' ')
    else:
        print("O",end=' ')
