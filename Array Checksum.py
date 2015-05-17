#pvprograms.weebly.com
#Array Checksum


test = int(input())
user = input()
user = user.split(' ')
for a in range(test):
    user[a] = int(user[a])

result = 0
for i in range(len(user)):
    result += user[i]
    result *= 113
    if(result >= 10000007):
        result = result % 10000007
print(result, end=' ')
    
