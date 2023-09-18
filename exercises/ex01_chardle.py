"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730668208"

word = input("Enter a 5-character word: ")


if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()


letter_character = input("Enter a single character: ")

if (len(letter_character) != 1):
    print(" Error: Character must be a single character.")
    exit()

print("Searching for " + str(letter_character) + " in " + str(word))

word_list = []
instance_count = 0

for letter in word:
    word_list.append(letter)

if (word_list[0] == letter_character):
    instance_count += 1
    print(str(letter_character) + " found at index 0")

if (word_list[1] == letter_character):
    instance_count += 1
    print(str(letter_character) + " found at index 1")

if (word_list[2] == letter_character):
    instance_count += 1
    print(str(letter_character) + " found at index 2")

if (word_list[3] == letter_character):
    instance_count += 1
    print(str(letter_character) + " found at index 3")

if (word_list[4] == letter_character):
    instance_count += 1
    print(str(letter_character) + " found at index 4")

if (instance_count >= 2):
    print(str(instance_count) + " instances of " + str(letter_character) + " found in " + str(word))
elif (instance_count >= 1):
    print(str(instance_count) + " instance of " + str(letter_character) + " found in " + str(word))
else:
    print("No instances of " + str(letter_character) + " found in " + str(word))