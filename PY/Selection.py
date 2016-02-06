
import random
n = 10
A = [random.randint(0, 10) for f in range(n)]
print A

for i in range(0, n-1):
    smallest = i
    for j in range(i+1, n):
        if A[j] < A[smallest]:
            smallest = j
    A[i], A[smallest] = A[smallest], A[i]


print A
