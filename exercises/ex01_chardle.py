"""EX01 - Chardle - A cute step toward Wordle."""
__author__ =730668208



word = input("What is your five letter word?")


if(len(word) != 5):
    print("Word must contain 5 letters")
    exit()


letter_character = input("What is your letter?")

if (len(letter_character) != 1):
    print("Character must a single character")
    exit()


word_list = []
instance_count = 0

for letter in word:
    word_list.append(letter)

if(word_list[0] == letter_character):
    instance_count += 1
    print("There is the letter " + str(letter_character) + " in your word. Your letter is found at index 0")

if(word_list[1] == letter_character):
    instance_count += 1
    print("There is the letter " + str(letter_character) + " in your word. Your letter is found at index 1")

if(word_list[2] == letter_character):
    instance_count += 1
    print("There is the letter " + str(letter_character) + " in your word. Your letter is found at index 2")

if(word_list[3] == letter_character):
    instance_count += 1
    print("There is the letter " + str(letter_character) + " in your word. Your letter is found at index 3")

if(word_list[4] == letter_character):
    instance_count += 1
    print("There is the letter " + str(letter_character) + " in your word. Your letter is found at index 4")

if(instance_count > 0):
    print("There are " + str(instance_count) + " instance found in " + str(word))
else:
    print ("There are no instances of " + str(letter_character) + " in " + str(word))









