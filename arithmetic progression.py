#pvprograms.weebly.com
#arithmetic progression

test = int(input())
for i in range(test):
    data = input()
    data = data.split(' ')
    total = 0
    for a in range(len(data)):
        data[a] = int(data[a])
    A = data[0]
    B = data[1]
    N = data[2]
    for b in range(N):
        total += A + b*B
    print(total, end=' ')
