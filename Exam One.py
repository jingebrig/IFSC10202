print("Winners and Losers - Human is Even, Computer is Odd")
hum_score = 0
com_score = 0

for i in range (1, 6):
    print("Round: ", i )
    hum_guess = int(input("Enter your guess: "))
    from random import randint
    com_guess = randint(1,5)

    print(f"Human Guess: {hum_guess} - Computer Guess: {com_guess}")

    guess_sum = hum_guess + com_guess
    guess_sum %= 2
    if guess_sum == 0:
        print("Sum is Even")
        hum_score += 1
    else:
        print("Sum is Odd")
        com_score += 1
    
    print(f"Human Score: {hum_score} - Computer Score: {com_score}")

if hum_score > com_score:
    print("Human Wins")
else:
    print("Computer Wins")