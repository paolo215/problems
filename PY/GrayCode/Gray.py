
def Gray(n):
    if n == 1:
        return [0,1] 
    G = list(Gray(n-1))
    S = list(reversed(G))
    G = prepend(0, G)
    S = prepend(1, S)
    G += S
    return G

def prepend(b, G):
    output = []
    for i in G:
        if isinstance(i, list):
            output.append([b] + i)
        else:
            output.append([b,i])
    return output
num = 3
a =   Gray(num) 
print a
