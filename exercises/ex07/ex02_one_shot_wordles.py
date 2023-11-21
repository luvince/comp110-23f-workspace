"""EX02- One Shot Wordle"""
__author__ = "730668208"

secret_word = "python"

player_input = input("What is your 6-letter guess? ")
while (len(player_input) != 6):
    player_input = input("That was not 6 letters! Try again: ")

if (player_input == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

index = 0
emoji = ""
guess_word_list = []
secret_word_list = []
result = ""

for letters in player_input:
    guess_word_list.append(letters)

for letters in secret_word:
    secret_word_list.append(letters)

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


while (index < len(secret_word)):
    if (guess_word_list[index] == secret_word_list[index]):
        result += GREEN_BOX
        index += 1
    else:
        boolean = False
        alternate_index = 0
        while (boolean == False and alternate_index < len(secret_word)):
            if guess_word_list[index] == secret_word_list[alternate_index]:
                boolean = True                
            else:
                alternate_index += 1
        if (boolean == False):
            result += WHITE_BOX
        else:
            result += YELLOW_BOX

        index +=1

print(result)