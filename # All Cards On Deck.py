# All Cards On Deck
import random

# Create Deck
deck = []
# Define suits and ranks
suits = ['\u2660', '\u2663', '\u2665', '\u2666']
print(suits[0:5])

ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print(ranks[0:14])
# - Loop through suits
for suit in suits:
    # - Loop through ranks
    for rank in ranks:
        # - Assign suit and rank to card
        deck.append(rank + suit)


print(deck[0:52])


# Shuffle

# - Loop through the deck from the last card index to the first (deck[rightIndex])
for right_index in range(len(deck) - 1, 1, -1):
    #   - Randomly Pick a card index before the rightIndex (deck[LeftIndex])
    left_index = random.randint(0, right_index)
    #   - Assign the value of the deck[rightIndex] to leftCard
    left_card = deck[right_index]
    #   - Assign the value of deck[leftIndex] to rightCard
    right_card = deck[left_index]
    #   - Assign the value of rightCard to deck[rightIndex]
    deck[right_index] = right_card
    #   - Assign the value of leftCard to deck[leftIndex]
    deck[left_index] = left_card

print(deck[0:52])

# Deal the cards

# - Add the first 2 cards from the shuffled deck to the player hand
# - Show the 2 cards
# - Remove the 2 cards from the deck
