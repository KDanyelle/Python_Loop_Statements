#Task 1

#Let's Play Uno 

#Card in Deck
uno_cards = ['blue', 'red', 'green', 'yellow', 'wild']
selected_card = random.choice(uno_cards)
while True: 
#Each player must be asked for their guess
    Guess = input("guess the Uno card color: ")
#Check to see if the player guess is correct
if guess.lower() ==selected_card:
    print("You're Winner! You got it right.")
else:
    print("Sorry, about your luck. Better luck next time!" )

    #Not sure what is going on here I now there is someting missing, from the error msg.. you want us to use ramdom.choice, but could random.randint work?

    