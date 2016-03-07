

def perm(n):
    if len(n) <= 1:
        return n
    P = perm(n[1:])
    first = n[0]
    allPerm = []
    for i in range(0, len(P)):
        p = P[i]
        for z in range(0, len(p)+1):
            allPerm.append(p[0:z] + first + p[z:len(p)])
    return allPerm

print perm("".join(map(str, range(5))))
