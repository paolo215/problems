#pvprograms.weebly.com
#Smoothing the weather

test = int(input())
data = input()
data = data.split(' ')
for i in range(len(data)):
    data[i] = float(data[i])

print(float("{0:.10f}".format(data[0])), end=' ')
for a in range(1, len(data) - 1):
    total = 0
    total += (data[a-1] + data[a] + data[a+1]) / 3
    total = float("{0:.10f}".format(total))
    if total.is_integer() == True:
        total = int(total)
    print(total, end=' ')
print(float("{0:.10f}".format(data[len(data) - 1])), end=' ')
