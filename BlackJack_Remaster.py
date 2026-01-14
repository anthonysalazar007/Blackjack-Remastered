#========================================
#To do; Figure out duplicate blackjack funcs
#========================================
import random
import pandas as pd
import seaborne as sns
cards = {
    'Ace of Hearts': 11, '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4, '5 of Hearts': 5,
    '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9, '10 of Hearts': 10,
    'Jack of Hearts': 10, 'Queen of Hearts': 10, 'King of Hearts': 10,

    'Ace of Diamonds': 11, '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4, '5 of Diamonds': 5,
    '6 of Diamonds': 6, '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9, '10 of Diamonds': 10,
    'Jack of Diamonds': 10, 'Queen of Diamonds': 10, 'King of Diamonds': 10,

    'Ace of Clubs': 11, '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4, '5 of Clubs': 5,
    '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9, '10 of Clubs': 10,
    'Jack of Clubs': 10, 'Queen of Clubs': 10, 'King of Clubs': 10,

    'Ace of Spades': 11, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5,
    '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10,
    'Jack of Spades': 10, 'Queen of Spades': 10, 'King of Spades': 10
}

playerCards = []
houseCards = []
playerWins = []
houseWins = []
ties = []
playerChips = [20]

def blackjack():
    global playerCards, houseCards, houseWins, playerWins  # Ensure you reference global variables here
    while True:
        print("Your hand is:")
        print(playerCards)
        print("The house has:")
        print(houseCards[0])  # Displaying only the house's first card

        call = input("What would you like to do?\n>>1. Stay\n>>2. Hit\n>>").lower()

        if call == "1" or call == "stay":
            print("The House had", houseCards)
            player_total = calculate_total(playerCards)
            house_total = calculate_total(houseCards)

            if house_total > player_total and house_total <= 21:
                print("House wins. The House had:")
                print(houseCards)
                houseWins += 1
            elif player_total < house_total or player_total > 21:
                print("You win. The house had:")
                print(houseCards)
                playerWins += 1
            else:
                print("It's a tie!")

            break  # Exit the while loop after determining the winner when the player stays

        elif call == "2" or call == "hit":
            playerCards.append(cards.pop())
            print("Your hand is:")
            print(playerCards)

            # Calculate the total value of playerCards and check if it exceeds 21
            player_total = calculate_total(playerCards)
            if player_total > 21:
                print("You busted!")
                break  # Exit the loop if the player busts (total > 21)

