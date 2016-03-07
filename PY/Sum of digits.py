#pvprograms.weebly.com
#Sum of digits

test = int(input())
for i in range(test):
    user = input()
    user = user.split(' ')
    for a in range(len(user)):
        user[a] = int(user[a])
    summ = (user[0]*user[1])+user[2]
    summ= str(summ)
    ans = 0
    for b in range(len(summ)):
        ans += int(summ[b])
    print(ans, end=' ')
