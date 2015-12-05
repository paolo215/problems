#https://github.com/paolo215
test = int(input())
for i in range(test):
    data = input()
    data = data.split(" ")
    data = list(map(int, data))
    data = [f**2 for f in data]
    print(sum(data), end=" ")
        
