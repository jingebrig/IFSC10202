#There was a set of cards with numbers from 1 to N. One of the cards is now lost.
#Determine the number on that lost card given the numbers for the remaining cards.
#Hint: This solution has three parts. Suppose you have 10 cards.
    #First, sum the values from 1 to 10. This the total value of the cards.
    #Next, read each card (there will be 9 of them) and sum of their values.
    #Finally, subract the two sums. The difference is the missing card.

# Prompt the user for the total number of cards
N = int(input("Enter Number of Cards: "))

# Step 1: Calculate the total sum of all cards from 1 to N
total_sum = 0
for i in range(1, N + 1):
    total_sum += i

# Step 2: Read the remaining cards and sum their values
sum_remaining = 0
for i in range(N - 1):
    card = int(input("Enter Card: "))
    sum_remaining += card

# Step 3: Find and print the missing card
missing_card = total_sum - sum_remaining
print("Missing Card:", missing_card)