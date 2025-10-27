# | **Beginner** | **Console/CLI** | **2. Number Guessing Game** | `random` module, `while` loops, conditional logic. |

# importing random library
import random

# Computer choosing a number in inclusive range of 1-100
print("A number in inclusive range of 1-100 has been selected".center(20, "-"))
num = random.randint(1,100)

# print(f"Computer chose {num}")

# initializing the counter
count = 0 

# loop to make user guess the number
while True:
    # with every iteration, count is increased by 1.
    count += 1
    guess = int(input("What do you think the number is (1-100)? : "))

    # when user's guessed number is greated than computer's
    if guess > num:
        if guess-num > 30:
            print("You are nearly '30' or more ahead.")
        elif guess-num > 20:
            print("Nearly 20 or more ahead.")
        elif guess-num > 10:
            print("Nearly 10 or more ahead")
        elif guess-num > 5:
            print("You are close...nearly 5 ahead.")
        elif guess-num > 0:
            print("You are super close. Keep diminishing bit-by-bit.")

    # When computer's guessed number is greater than user's
    elif num > guess:
        if num-guess > 30:
            print("You are lagging by nearly '30', adden up!!.")
        elif num-guess > 20:
            print("You are lagging by nearly '20'.")
        elif num-guess > 10:
            print("You are lagging by nearly '10'")
        elif num-guess > 5:
            print("You are lagging by nearly '5'")
        elif num-guess > 0:
            print("You are super close. Keep increasing bit-by-bit.")

    # when user's guess = computer's guess
    elif num == guess:
        print("Ta-Da !!!! , You did it champ.")
        break # break the loop, when user makes the right guess

# After the loop - print the number of tries, it took to make the right guess.
print(f"In {count} tries.")


# Feedback function over, how well the user played.
def well_played(count):
    if 20 < count <= 30:
        print("You can do better!")
    elif 10 < count <= 20:
        print("Well played!!")
    elif 5 < count <= 10:
        print("Amazing, Guessing master!")
    elif 1 <= count <= 5:
        print("Man, You are damn good!.")
    else:
        print("You can do better!")

# Calling the feedback function
well_played(count)