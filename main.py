import random

words = ["fire","small","purple","copper","moon"]
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

def display_word():
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter,end=" ")
        else:
            print("_",end=" ")

def check_game_status(incorrect_guesses,max_guesses,secret_word,guessed_letters):
    allLettersGuessed = True
    for letter in secret_word:
        if letter not in guessed_letters:
            allLettersGuessed = False
    if allLettersGuessed == True:
        print("You win!")
        return False
    elif incorrect_guesses >= max_guesses:
        print("You lose!")
        return False
    else:
        return True

def play_game(incorrect_guesses,max_guesses,secret_word,guessed_letters):
    continueGame = True
    while continueGame:
        display_word()
        guess=input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed this letter!")
        elif guess not in secret_word:
            print("That letter is not in the word!")
            guessed_letters.append(guess)
            incorrect_guesses += 1
        else:
            print("Letter is in the word!")
            guessed_letters.append(guess)
        if continueGame:
            print(f"Remaining guesses: {max_guesses-incorrect_guesses}")
        print(f"Guessed letters: {guessed_letters}")
        continueGame = check_game_status(incorrect_guesses,max_guesses,secret_word,guessed_letters)


play_game(incorrect_guesses,max_guesses,secret_word,guessed_letters)


