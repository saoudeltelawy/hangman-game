import random
# import hangman_words
# here there is no need to amend hangman_words.game_word_list
from hangman_words import game_words_list 
from hangman_art import hangman_logo, stages

print(hangman_logo)

# A random word to be chosen!
chosen_word = random.choice(game_words_list)
# print(chosen_word)

# Create the blanks to represent the word
blanks = "_ " * len(chosen_word)
print(blanks)


game_over = False   # Initial State of the Game
correct_letters_guessed = []
lives = 6   # Initial Lives (# Of Tries)


while not game_over:
    print(f"You have {lives}/6 trails")
    display = ""
    user_guess = input("Guess a letter matching the below blanks: ").lower()
   
    # Check Guess Repetition (UX)
    if user_guess in correct_letters_guessed:
        print(f"You have already guessed {user_guess}")
    for letter in chosen_word:
        if letter == user_guess:
            display += letter
            correct_letters_guessed.append(user_guess)
            # print(correct_letters_guessed)
        elif letter in correct_letters_guessed:
            display += letter
            # print(display)
        else:  
            display += "_"
            # lives -= 1
    print(display)

    if "_" not in display:
        game_over = True
        print("You Win")
    if user_guess not in chosen_word:
        lives -= 1
        print(f"You guessed {user_guess} that's not in the word, you lose a life. You have {lives} lives left")
        if lives == 0:
            game_over = True
            print("***** You Lose! *****")
            print(f"The word was {chosen_word}!")
    print(stages[lives])



