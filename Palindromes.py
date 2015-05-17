#Palindromes

test = int(input())


for i in range(test):
    a = input()
    z = 0
    a = a.lower()
    while(z < len(a)):
        if a[z] < 'a' or a[z] > 'z':
            a = a.replace(a[z], "")
        z += 1
    a = a.split(' ')
    a = ''.join(a)
    backwards = a[::-1]
    if a == backwards:
        print("Y ")
    else:
        print("N ")
    

