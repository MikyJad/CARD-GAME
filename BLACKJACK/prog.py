import random
import sys
import os
import time

def printcard(rand):
    print(" -------------------")
    print("| 2                 |")
    print(f"| {rand}                 |")
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print(f"|         {rand}         |")
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print(f"|                 {rand} |")
    print("|                 2 |")
    print(" -------------------")

def pickcard(kind, num):
    rand1 = random.choice(kind)
    rand2 = random.choice(rand1)
    num.remove(rand2)
    return rand2

def processcard(card, total):
    if card == "2":
        return 2
    elif card == "3":
        return 3
    elif card == "4":
        return 4
    elif card == "5":
        return 5
    elif card == "6":
        return 6
    elif card == "7":
        return 7
    elif card == "8":
        return 8
    elif card == "9":
        return 9
    elif card == "10":
        return 10
    elif card == "J" or card == "Q" or card == "K":
        return 10
    elif card == "A":
        if total == 0:
            return 11
        else:
            return 1


kindcard = ["♠", "♥", "♦", "♣"]
numcard = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]

for i in range(len(kindcard)):
    kindcard[i] = numcard

dealercard = []
playercard = []
playersum = 0
dealersum = 0

randcard = pickcard(kindcard, numcard)
playercard.append(randcard)
playersum += processcard(randcard, playersum)

randcard = pickcard(kindcard, numcard)
playercard.append(randcard)
playersum += processcard(randcard, playersum)

randcard = pickcard(kindcard, numcard)
dealercard.append(randcard)
dealersum += processcard(randcard, dealersum)
dealercard.append("?")

print(f"Dealer's Card : {dealercard}")
print(f"Total : {dealersum}\n")

print(f"Player's Card : {playercard}")
print(f"Total : {playersum}\n")

if playersum == 21:
    print("BLACKJACK! YOU WIN")
    sys.exit()

time.sleep(3)

dealercard.remove("?")
randcard = pickcard(kindcard, numcard)
dealercard.append(randcard)
dealersum += processcard(randcard, dealersum)

dealercardtemp = dealercard
dealersumtemp = dealersum

if dealersum == 21:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Dealer's Card : {dealercard}")
    print(f"Total : {dealersum}\n")

    print(f"Player's Card : {playercard}")
    print(f"Total : {playersum}\n")

    print("DEALER BLACKJACK! YOU LOSE")
    sys.exit()

print("1. Hit || 2. Stand")
playchoice = input("-> ")
print()
            
if playchoice == "1":
    while playchoice == "1" and playersum <= 21:
        os.system('cls' if os.name == 'nt' else 'clear')
        randcard = pickcard(kindcard, numcard)
        playercard.append(randcard)
        playersum += processcard(randcard, playersum)

        print(f"Dealer's Card : {dealercardtemp}")
        print(f"Total : {dealersumtemp}\n")

        print(f"Player's Card : {playercard}")
        print(f"Total : {playersum}\n")

        if playersum < 21:
            print("1. Hit || 2. Stand")
            playchoice = input("-> ")
            print()
        elif playersum == 21:
            print("YOU WIN")
            sys.exit()
        else:
            print("BUST! YOU LOSE")
            sys.exit()

os.system('cls' if os.name == 'nt' else 'clear')
print(f"Dealer's Card : {dealercard}")
print(f"Total : {dealersum}\n")

print(f"Player's Card : {playercard}")
print(f"Total : {playersum}\n")

while dealersum <= 21 and dealersum < playersum:
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    randcard = pickcard(kindcard, numcard)
    dealercard.append(randcard)
    dealersum += processcard(randcard, dealersum)

    print(f"Dealer's Card : {dealercard}")
    print(f"Total : {dealersum}\n")

    print(f"Player's Card : {playercard}")
    print(f"Total : {playersum}\n")

if dealersum == 21:
    print("YOU LOSE")
elif dealersum > 21:
    print("DEALER BUST! YOU WIN")
elif dealersum > playersum:
    print("DEALER WIN")
elif dealersum == playersum:
    print("TIE! NEITHER WIN")

        

