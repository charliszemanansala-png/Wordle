import random

def alphabet(guessed_letters):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    for letter in guessed_letters:
        if letter in alphabet:
            guessed_letters.append(letter)
            alphabet.remove(letter)

    print(''.join(alphabet)) 
    return

def guess_feedback(guess, secret_word):

    feedback = [''] * 5
    remaining = list(secret_word)

    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback[i] = guess[i].upper()
            remaining[i] = None        

    for i in range(5):
        if feedback[i] == "":
            if guess[i] in remaining:
                feedback[i] = "!"
                remaining[remaining.index(guess[i])] = None
            else:
                feedback[i] = "?"  

    print(f"Feedback: {''.join(feedback)}") 

def play_game():

    words = ["APPLE", "ARISE", "BROKE", "BEACH", "CRAZY", "CATCH", "DAIRY", "DROWN", "EAGLE", "EBONY", "FAITH", "FARTS",
              "GRAVE", "GRAND", "HEART", "HENCE", "IDIOM", "IDEAL", "JERKY", "JEWEL", "KNIFE", "KNOWN", "LEMON", "LAUGH", 
              "MOURN", "MINDS", "NORTH", "NAVAL", "OFFER", "ORDER", "PRIZE", "PURSE", "QATAR", "QUEEN", "ROCKS", "ROLES",
              "STING", "SINGS", "TURNS", "TILES", "UNCLE", "ULTRA", "VALUE", "VAULT", "WHALE", "WAGES", "XEROX", "XENON",
              "YEAST", "YOUNG", "ZEBRA", "ZEROS"]

    secret_word = random.choice(words)

    attempts = 6
    guessed_letters = []

    while attempts > 0:

        print("Enter you guess: ")
        guess = input().upper()

        if guess == "QUIT":
            quit()

        if guess == "ALPHABET":
           guess = guessed_letters
           alphabet(guessed_letters)
           continue

        elif len(guess) != 5 or not guess.isalpha():
            print("Please Enter a 5 letter word!")
            continue

        for char in guess:
            if char not in guessed_letters:
                guessed_letters.append(char)
                
        else:
            if guess == secret_word:
                print(f"Congratulations! You guess the word {secret_word}!")
                return
            else:
                guess_feedback(guess, secret_word)
                attempts -= 1
                print(f"Attempts left:  {attempts}")

    print(f"Game Over! The word is: {secret_word}")

def wordle():
    print("Hello and welcome to Wordle!")

    while True:
        print("Choose 1 for Game or 2 for Quit!")

        choose = int(input("Enter a number: "))
    
        if choose == 1:
            play_game()
        elif choose == 2:
            print("Thank you for playing!")
            return False
        else:
            print("Not valid! Choose a mode again!")
            
wordle()