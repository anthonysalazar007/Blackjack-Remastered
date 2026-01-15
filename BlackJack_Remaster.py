#========================================
#To do;
#========================================
import random
import pandas as pd
import seaborn as sns

#Game Values
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

#Data Values
playerWins = []
houseWins = []
pushes = [] #pushes are ties in blackjack
ties = []
playerChips = [200]

def blackJack(): # entire AREA SUBJECT TO REVIEW
    # Scramble the deck three times
    # Assign 2 cards to player
    # Assign 2 cards to house, displaying only the first
    print("Your hand is:")
    print(playerCards)
    print("The house has:")
    print(houseCards[0])  # Displaying only the house's first card

    call = input("What would you like to do?\n>>1. Stay\n>>2. Hit\n>>").lower()
    
    def stay():
        #calculate total value of cards
            #if total > 21
                #if ace in hand
                    #player hand -= 10
                #else
                    #you busted
        #if player cards > house cards 
            #upload data
        #elif player cards < house cards 

        #elif player cards < house cards 

    def hit():
        #placeholder
    if call == "1" or call == "stay":
        stay()
    elif call == "2" or call == "hit":
        hit()


def dataAnalysis():
    print("Placeholder text. Also, did you know that when you out of the in, you had out in of your?")