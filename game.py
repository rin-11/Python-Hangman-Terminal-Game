print('Welcome to Python Hangman')


# random module -- used to generate random word selection from the word bank
import random

# Define the word class
class Word():
    # pass chosen_word as a parameter
    def __init__(self, chosen_word):
        # initialize self.word attribute as an empty list 
        self.word = []
        # loops through every character in the chosen_word and appends a dictionary (display)
        # append() method takes an object as an argument and adds it to the end of list
        # characters (char) have two attributes: letter and whether or not the letter appears in the word (boolean)
        for char in chosen_word:
            self.word.append({'letter': char, 'guessed': False})

    def display_word(self):
        display = ""
        # generate a display string, '_' or letter, representation of the word based on the guessed/unguessed letters
        # if the character guessed is true --> append the character to the display 
        for char in self.word:
            if char['guessed']:
                # show tht character/letter if guessed = true
                display += char['letter'] + " "
            else:
                # otherwise show _
                display += "_ "
        # return the display string
        return display


    def guess_letter(self, letter):
        # takes a letter parameter and checks if the guessed letter is present in the word
        found = False
        # iterate over each character in self.word 
        for char in self.word:
            if char['letter'] == letter:
                char['guessed'] = True
                found = True
        return found

# word bank with all of the word options
word_bank = ['tomato', 'potato', 'ratatouille', 'artichoke', 'rigatoni', 'ballet', 'pianist', 'deepfake', 'oligarchy', 'engender', 'florescence']
# word selected at random from the word bank
chosen_word = random.choice(word_bank)
# pass word selected from the word bank to the Word class
word = Word(chosen_word)

# initialize the guesses variable to 8
guesses = 8
# keep track of letters already guessed
letters_used = []

# print guesses remianing/letters guess/word display each time a key is pressed
while guesses > 0:
    print("Remaining guesses:", guesses)
    print("Letters used:", ", ".join(letters_used))
    print("Guess the word:", word.display_word())

    # characters can be guessed lower case or capital using .lower()
    guess = input("Guess a letter: ").lower()

    if guess in letters_used:
        print("You have already guessed that letter.")
        continue

    letters_used.append(guess)
    # if guess is correct and character is appended to the word display 
    if word.guess_letter(guess):
        print("Good choice!")
    else:
        print("Try again!")
        # subtract from the guesses (8) each time a guess is incorrect
        guesses -= 1
    # win when all the characters in the word string are guessed
    if all(char['guessed'] for char in word.word):
        print("Great job! You figured it out!")
        break
    # lose when guesses = 0
if guesses == 0:
    print("GAME OVER! The word was", chosen_word)


