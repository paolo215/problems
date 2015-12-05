#https://github.com/paolo215
suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

test = input()
data = input()
data = data.split(" ")
data = list(map(int, data))
for i in data:
    suit = int(i / 13)
    rank = int(i % 13)
    print("-".join([str(ranks[rank]), "of",str(suits[suit])]), end=" ")
