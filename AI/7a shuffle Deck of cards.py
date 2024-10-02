import random

print("04_Jayprabha Nadar")

# Initialize lists for card faces and suits
cardfaces = []
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
royals = ["J", "Q", "K", "A"]
deck = []

# Add number cards 2-10
for i in range(2, 11):
    cardfaces.append(str(i))  # Convert numbers to strings and add to card faces

# Add royal cards J, Q, K, A
for royal in royals:
    cardfaces.append(royal)

# Create the full deck of cards by combining card faces with suits
for suit in suits:
    for face in cardfaces:
        card = f"{face} of {suit}"
        deck.append(card)

# Shuffle the deck
random.shuffle(deck)

# Print out all 52 shuffled cards
for card in deck:
    print(card)
