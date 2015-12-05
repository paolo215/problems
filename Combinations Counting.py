#https://github.com/paolo215
import math

test = int(input())
for i in range(test):
    a = input()
    a = a.split(" ")
    a = list(map(int, a))
    top = math.factorial(a[0])
    bottom = math.factorial(a[1]) * math.factorial((a[0] - a[1]))
    print(int(top/bottom), end=" ")
