import random as r
from hangman_art import stages,logo
from hangman_words import word_list

# word_list = ["ardvark", "baboon", "camel", "flower"]


lives = len(stages)-1

print(logo)

while True:
    user_choice = input("Type '1', if you want to write your own word or '2', if you want a random word to be generated: ")
    if user_choice == '1':
        chosen_word = input("Enter your word: ")
        break
    elif user_choice == '2':
        # select a random word in a list
        chosen_word = r.choice(word_list)
        break
    else:
        print("Invalid choice! Please select '1' or '2'.")

# Fill a list with blanks
display = []
for i in chosen_word:
    display.append("_")

# Check user input
def check_user_input(a):
    # Replace blanks with guess
    for i,j in enumerate(chosen_word):
        if a == j.lower():
            display[i] = a.lower()
        else:
            pass

    # Print display
    for k,l in enumerate(display):
        if k != len(display)-1:
            print(l,end=" ")
        else:
            print(l)


# print(f"Pssst, the solution is {chosen_word}")
guessed = []

while True:
    guess = input("Guess a letter: ").lower()
    print("")
    if guess in guessed:
        print("You have already guessed this letter")
        guessed.append(guess)
        continue
    guessed.append(guess)

    check_user_input(guess)
    # print(stages[lives])

    if guess not in chosen_word:
        lives -= 1
    print(stages[lives])
    print(guessed)

    if "_" not in display:
        print("You Won!")
        break
    elif lives == 0:
        print("You Lose!")
        print(f"The word was {chosen_word}")
        break
    else:
        pass