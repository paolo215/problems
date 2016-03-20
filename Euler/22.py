#Names scores
import string
alpha = string.lowercase
f = open("p022_names.txt","r")
a = f.read().lower()
f.close()

a = sorted(a.replace("\"", "").split(","))
s = 0
for i in range(len(a)):
    s += (i+1) * sum([alpha.index(f)+1 for f in list(a[i])])
print s
