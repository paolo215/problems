#Amicable numbers
#Slightly optimized




def amicable(j):
    a = []
    for i in range(1,int(j//2) + 1):
        if j % i == 0:
            a.append(i)
    return sum(a)

assert amicable(220) == 284 and amicable(284) == 220



S = {}
a = []

for i in range(1, 10000):
    S[i] = amicable(i)

for i in range(1, 10000):
    for j in range(1, i - 1):
        if S[i] == j and i == S[j] and i != j:
            print i,j
            if j not in a:
                a.append(j)
            if i not in a:
                a.append(i)
print sum(a)
