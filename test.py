import random


def card_Draw():
#This function distributes unique cards to the 'n' number of players.
    i = 1
    first_Draw = random.randrange(1, 10)
    pile = []
    pile.append(first_Draw)
    stash = []
    while i<8:
        i = i+1
        draw = random.randrange(1, 10)
        if draw in pile:
            i = i-1
            continue
        else:
            pile.append(draw)
    return pile


def players(n):
#This function inputs number of players and takes the card set for future use.
    i = 0
    card_Holder = []
    while i<n:
        card_Draw()
        i = i + 1
        card_Holder.extend([card_Draw()])
    for val in card_Holder:
        print(val)


m = int(input("Number of players in the game: "))
print("Your cards are: ")
players(m)