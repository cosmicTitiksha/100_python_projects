# The code is for rock-paper-scissors game with computer. Enjoy!!!!!!!!!'
# Importing random library, to randomly let computer choose its choice

import random
# function to get choices of both the player and the computer
def get_choices():
    options = ['rock', 'paper', 'scissors']
    # if choice entered by user is not in 'options', user will be asked to re-enter
    while True:
        player_choice = input("Enter your choice (rock/paper/scissors) : ").lower()
        if player_choice in options:
            break
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue
    
    computer_choice = random.choice(options)
    choices = {'player' : player_choice, 'computer' : computer_choice}
    return choices

# function to check the score
def check_win(player, computer):
    score = 0
    if player == computer:
        result = 'Tie'
    elif player == 'rock':
        if computer == 'paper':
            result = 'Lose'
            score -= 1
        else:
            result = 'Win'
            score += 1
    elif player == 'paper':
        if computer == 'rock':
            result = 'Win'
            score += 1
        else:
            result = 'Lose'
            score -= 1
    elif player == 'scissors':
        if computer == 'rock':
            result = 'Lose'
            score -= 1
        else:
            result = 'Win'
            score += 1

    print(f"You chose {player}, computer chose {computer}. It's a {result}. ")
    # score is returned so as 'score' can be displayed in later stage
    return score


# program starts from here-------------------------------------
query = int(input("How many times do you want to play ? : "))
score = 0
# loop to let user play as many times it wants
for i in range(query):
    choices = get_choices()
    # score is added to global 'score' variable everytime loop runs
    score += check_win(choices['player'], choices['computer'])

# final score displayed
print(f"Your score : {score}/{query}")