#Smallest multiple

start = 20
a = range(1,start)

def isDiv(n):
    return all([n % f == 0 for f in a])

i = start
while(isDiv(i) == False):
    i += 20

print i
