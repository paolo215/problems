#pvprograms.weebly.com
#Triangles

test = int(input())
for i in range(test):
    data = input()
    data = data.split(' ')
    for z in range(len(data)):
        data[z] = int(data[z])
    a = data[0]
    b = data[1]
    c = data[2]
    if a + b > c and b + c > a and a + c > b:
        print(1, end=' ')
    else:
        print(0, end=' ')
