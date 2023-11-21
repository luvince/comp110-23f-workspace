"""EX03- Structured Wordle."""
__author__ = "730668208"


def contains_char(word: str, letter: str) -> bool: 
    """This function checks if the letter is anywhere in the word."""
    assert len(letter) == 1
    index = 0
    while index < len(word): 
        if word[index] == letter:
            return True
        index += 1
    return False

       
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """This function is the connatocated emojis, if the letter of the guessed word is the same as the secret word, then it is a green box, it calls the earlier contains_char function to check for yellow boxes and white boxes."""
    assert len(guess) == len(secret)
    index = 0
    result = ""
    while index < len(secret):
        if guess[index] == secret[index]:
            result += GREEN_BOX
            index += 1
        else:
            if contains_char(secret, guess[index]):
                result += YELLOW_BOX
                index += 1
            else: 
                result += WHITE_BOX
                index += 1
    return result


def input_guess(integer: int) -> str:
    """This function prompts the user for input based off a certain length and loops until the equirement is met."""
    player_input = input("Enter a " + str(integer) + " character word: ")
    while (len(player_input) != integer):
        player_input = input("That wasn't " + str(integer) + " chars! Try again: ")
    return player_input


def main() -> None:
    """Made variables necessary to keep track of the turns and whether the user won and uses the other functions to prompt the user, check the boxes and print the result."""
    secret_code = "codes"
    turn_number = 1
    turn_max = 6
    while turn_number < turn_max + 1:
        print("=== Turn " + str(turn_number) + "/6 ===")
        guess_word = input_guess(len(secret_code))
        if secret_code == guess_word:
            print(emojified(guess_word, secret_code))
            print("You won in " + str(turn_number) + "/6 turns!")
            return
        else:
            print(emojified(guess_word, secret_code))
        turn_number += 1
    print("X/6 - Sorry, try again tomorrow!")