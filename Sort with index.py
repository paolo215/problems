#pvprograms.weebly.com
#Sort with Indexes

test = input()
data = input()
data = data.split(' ')
for i in range(len(data)):
    data[i] = int(data[i])

new = sorted(data)
rank = []
for a in range(len(data)):
    for b in range(len(data)):
        if new[a] == data[b]:
            rank.append(b + 1)
    print(rank[a], end=' ')
