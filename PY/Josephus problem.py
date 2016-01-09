
#Josephus Problem

data = input()
data = data.split(' ')
k = int(data[1])
n = int(data[0])
num = []
for a in range(1,n+1):
    num.append(a)
i = 0
while(len(num) > 1):
    i = (i + k-1) % len(num)
    num.pop(i)
print(num[0])
    
