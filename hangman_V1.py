import random

# List of words for the game
game_words_list = ["ant", "zee", "camel", "sam", "loe", "zaza"]

# A random word to be chosen!
game_chosen_word = random.choice(game_words_list)
print(game_chosen_word)


# Create the blanks to represent the word
blanks = "_ " * len(game_chosen_word)
print(blanks)

user_guess = input("Guess a letter matching the below blanks: ").lower()

# Create another variable to fill/display the guess letter in the blanks 
display = ""

for letter in game_chosen_word:
  if letter == user_guess:
    print("Right")
    display+= user_guess + " "
  else:
    print("Wrong")
    display+= "_ "

print(display)
