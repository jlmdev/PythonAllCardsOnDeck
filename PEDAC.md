# PEDAC

## Problem

- Deck should contain 52 unique cards
- All cards should be represented as a string
- Once the program starts, create a new deck
- After deck creation, shuffle the deck
- After the deck is shuffled, display the top 2 cards

## Examples

- Ace of Spades, 10 of Clubs

## Data Structures

- Create Deck
  - Suits List
  - Rank List
  - Card (string: combination of suit and rank)
  - Deck List
- Shuffle Deck (Fisher-Yates shuffle Algorithm)

  - Cards
    - Left Card
    - Right Card
  - Indices
    - LeftIndex
    - RightIndex

- Player Hand
  - first 2 cards

## Algorithm

### Create Deck

- Loop through suits
  - Loop through ranks
    - Assign suit and rank to card

### Shuffle

- Loop through the deck from the last card index to the first (deck[rightIndex])
  - Randomly Pick a card index before the rightIndex (deck[LeftIndex])
  - Assign the value of the deck[rightIndex] to leftCard
  - Assign the value of deck[leftIndex] to rightCard
  - Assign the value of rightCard to deck[rightIndex]
  - Assign the value of leftCard to deck[leftIndex]

### Deal the cards

- Add the first 2 cards from the shuffled deck to the player hand
- Show the 2 cards
- Remove the 2 cards from the deck
