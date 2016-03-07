#https://github.com/paolo215


a = input()
a = a.split(" ")
a = a[0]

guesses = input()
guesses = guesses.split(" ")


for g in guesses:
    score = [0,0]
    for i in range(len(g)):
        if a[i] == g[i]:
            score[0] += 1
        elif g[i] in a and g[i] != a[i]:
            score[1] += 1
    print("-".join(list(map(str, score))), end=" ")

