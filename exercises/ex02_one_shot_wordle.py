"""EX02- One Shot Wordle."""
__author__ = "730668208"

# The word to user has to guess
secret_word = "python"

# The word the player is guessing and loops if the user does not input a six letter word
player_input = input("What is your 6-letter guess? ")
while (len(player_input) != 6):
    player_input = input("That was not 6 letters! Try again: ")

# Prints a message depending on whether the player got the word or not
if (player_input == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

# Making variables: index and alternate index is for the loops to check if they equal to each other, result is the boxes that shows what you got right and wrong aka green, yellow, green
index = 0
guess_word_list = []
secret_word_list = []
result = ""

# Adds the letters of the variable player_input and adds it to a list
for letters in player_input:
    guess_word_list.append(letters)

# Adds the letters of the variable secret_word and adds it to a list
for letters in secret_word:
    secret_word_list.append(letters)

# Different boxes 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Runs through the loop and if the index of each list matches, green is added to the variable result; else a boolean variable is made which determines if the letter the user inputted equals to any other letter in the secret word; if the boolean is false then it loops until it goes through the whole word
while (index < len(secret_word)):
    if (guess_word_list[index] == secret_word_list[index]):
        result += GREEN_BOX
        index += 1
    else:
        boolean = False
        alternate_index = 0
        while (boolean != True and alternate_index < len(secret_word)):
            if guess_word_list[index] == secret_word_list[alternate_index]:
                boolean = True                
            else:
                alternate_index += 1
        if (boolean != True):
            result += WHITE_BOX
        else:
            result += YELLOW_BOX

        index += 1

print(result)