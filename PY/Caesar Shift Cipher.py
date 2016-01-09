import string
alpha = string.ascii_lowercase
a = input()
a = a.split(" ")
test = int(a[0])
key = int(a[1])
for i in range(test):
    enc = ""
    s = input()
    s = s.lower()
    s = list(s)
    for letter in s:
        if letter in alpha:
            idx = alpha.index(letter)
            enc += alpha[(idx - key) % len(alpha)]
        else:
            enc += letter
    print(enc.upper(), end=" ")
        
