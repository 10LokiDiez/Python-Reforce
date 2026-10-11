from random import choice, randint, shuffle

#Elige aleatoriamente el dato
coin =choice(["Heads", "Tails"])
print(coin)

#numero random
random_integer = randint(1,100)
print(random_integer)

#pone aleatorias las cartas
cards = ["jack","queen", "king"]
shuffle(cards)
for card in cards:
    print(card, end=" ")
