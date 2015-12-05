#https://github.com/paolo215
test = int(input())

for i in range(test):
    data = input()
    data = data.split(" ")
    data = list(map(int, data))
    current = data[0]
    goal = data[1]
    interest = data[2] / 100
    year = 0
    while(current < goal):
        add = current * interest
        current += add
        year += 1
    print(year, end=" ")
