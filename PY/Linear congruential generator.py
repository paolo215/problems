#https://github.com/paolo215
test = int(input())
for i in range(test):
    data = input()
    data = data.split(" ")
    data = list(map(int, data))
    A, C, M, X0, N = tuple(data)
    for z in range(N):
        X0 = (A * X0 + C) % M
    print(X0, end=" ")
