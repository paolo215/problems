#pvprograms.weebly.com
#Weighted sum of digits

test = int(input())
user = input()
user = user.split(' ')
for i in range(test):
    num = 0
    for a in range(len(user[i])):
        num += (int(user[i][a]) * (a+1))
    print(num, end=' ')
