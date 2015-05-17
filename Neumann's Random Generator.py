#pvprograms.weebly.com
#Neumann's Random Generator

test = int(input())
user = input()
user = user.split(' ')
for a in range(len(user)):
    user[a] = int(user[a])
for i in range(len(user)):
    values = []
    add_zero = user[i]
    loop = 0
    while True:
        loop += 1
        add_zero = add_zero ** 2
        add_zero = str(add_zero)
        if(len(add_zero) < 8):
            length = len(add_zero)
            add_zero = ('0'*(8-length)) + add_zero
        add_zero = add_zero[2:6]
        add_zero = int(add_zero)
        if add_zero  in values:
            print(loop, end=' ')
            break
        elif add_zero == user[i]:
            print(loop, end=' ')
            break
        values.append(add_zero)
    
    




