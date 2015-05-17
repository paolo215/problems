#pvprograms.weebly.com
#Array counters

user = input()
user = user.split(' ')
r = int(user[0]) #range
n = int(user[1])
numlist = []
counter = []
for a in range(n):
    numlist.append(a+1)
    counter.append(0)

user = input()
user = user.split(' ')
for b in range(len(user)):
    user[b] = int(user[b])

#do work
for c in range(len(user)):
    if user[c] in numlist:
        counter[user[c]-1] += 1

for d in counter:
    print(d, end=' ')
