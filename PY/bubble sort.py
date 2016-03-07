#pvprograms.weebly.com
#bubble sort

test = int(input())
user = input()
user = user.split(' ')
for a in range(test):
    user[a] = int(user[a])

#do work
swap1 = 0
pass1 = 0
while True:
    checker = False
    for i in range(1, test):
        if user[i-1] > user[i]:
            swap1+= 1
            t = user[i-1]
            user[i-1] = user[i]
            user[i] = t
            checker = True
    pass1 += 1
    if checker == False:
        break
print(pass1, swap1)
