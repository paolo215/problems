#pvprograms.weebly.com
#Collatz Sequence

test = int(input())

user = input()
user = user.split(' ')
for a in range(test):
    user[a] = int(user[a])

for b in range(test):
    Xnext = user[b]
    counter = 0
    while(Xnext != 1):
        if(Xnext % 2 == 0):
            Xnext = Xnext / 2
            counter += 1
        else:
            Xnext = (3*Xnext) + 1
            counter += 1
    print(counter, end=' ')
