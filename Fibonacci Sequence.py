#pvprograms.weebly.com
#Fibonacci Sequence
test = int(input())
seq = [0,1]
for i in range(2,100000):
        seq.append(seq[i-1] + seq[i-2])
find = []
while test > 0:
    data = int(input())
    find.append(data)
    test -= 1

for a in range(len(find)):
    for b in range(len(seq)):
        if find[a] == seq[b]:
            print(b, end=' ')
            break
    
    
    
