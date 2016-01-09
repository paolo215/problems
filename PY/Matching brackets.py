#https://github.com/paolo215
test = int(input())

for i in range(test):
    data = input()
    data = [f for f in data if f in "()[]{}<>"]
    data = "".join(data)
    current = len(data) + 1
    while(current != len(data)):
        current = len(data)
        data = data.replace("()","").replace("[]","").replace("{}", "").replace("<>", "")
    if len(data) > 0:
        print(0, end=" ")
    else:
        print(1, end=" ")
