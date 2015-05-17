#pvprograms.weebly.com
#Median of Three

test = int(input())
for i in range(test):
    user = input()
    user = user.split(' ')

    for a in range(len(user)):
    user[a] = int(user[a])
    #sorted - increasing
    user = sorted(user)
    #Since there are just three index[1] shoud be the median
    print(user[1], end=' ')
