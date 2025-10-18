# The code is for rock-paper-scissors game with computer. Enjoy!!!!!!!!!'
# Importing random library, to randomly let computer choose its choice
import random
# function to get respective player and computer's choice
def make_choices():
    player_choice = input("Enter your choice ('rock','paper','scissors') : ")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choice = {"player" : player_choice , "computer" : computer_choice}
    return choice
# logic to check if the player won, lose or the game is a Tie!!!!!
def check_win(player, computer):
    score = 0
    if player == computer:
        output = "It's a tie!!!"
    elif player == 'rock':
        if computer == 'paper':
            output = "You lose."
        else:
            output = "You won!"
            score += 1
    elif player == 'paper':
        if computer == 'rock':
            output = 'You won!'
            score += 1
        else:
            output = 'You lose'
    elif player == 'scissors':
        if computer == 'rock':
            output = "You lose"
        else:
            output = 'You won!'
            score += 1
    else:
        output = "Enter a valid item!"
    print(f"You entered {player}, computer chose {computer}. {output}")
    # Returning score...and updating in next part to calculate overall score
    return score

print("Rock - Paper - Scissors".center(70, "-"))
# Initial score as a '0'
score = 0
output = ""
# Letting the user decide, how many times, it wants to play against computer
times = int(input("How many times do you want to play against computer? : "))
for i in range(times):
    choice = make_choices()
    # Updating score, to let user see its final score later
    score += check_win(choice["player"], choice["computer"])

# Displaying final score out of the games player decided tohave, against the computer
print(f"You scored {score}/{times}")

