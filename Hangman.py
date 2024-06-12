import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

import os
def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux (os.name is 'posix')
    else:
        os.system('clear')

print(logo)

end_of_game = False
chosen_word = random.choice(word_list)

print(f"Psst, the word is: {chosen_word}")
# print(len(chosen_word))

display = []
for letter in range (1, len(chosen_word) + 1):
    display += "_"
print(display)
print(stages[6])
lives = int(6)

while not end_of_game:
    guess = input("Guess a letter\n").lower()

    clear()
    print(logo)
    if guess in display:
        print("You've already entered this letter.")

    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(f"{' '.join(display)}")
    print(f"Your remaining lives are {lives}")
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("you win")