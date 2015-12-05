#https://github.com/paolo215

def RPS(a, b):
    if a == b:
        return 0
    
    if a == "R" and b == "S":
        return 1
    elif a == "S" and b == "R":
        return 2
    elif a == "S" and b == "P":
        return 1
    elif a == "P" and b == "S":
        return 2
    elif a == "P" and b == "R":
        return 1
    else:
        return 2
    
test = int(input())
for i in range(test):
    data = input()
    data = data.split(" ")
    win = []
    for z in data:
        win.append(RPS(z[0], z[1]))
    if win.count(1) > win.count(2):
        print(1, end=" ")
    else:
        print(2, end= " ")
