# The program is a "Number Guessing Game"
import random

generated_num = random.randint(1,100) # Any number in inclusive range of 1 to 100
count = 0

query = True
while query:
    count += 1
    predicted_num = int(input("Enter the predicted number : "))
    if generated_num > predicted_num :
        if generated_num-predicted_num >= 40:
            print("Need to add a lot more!!!")
        elif generated_num-predicted_num >= 20:
            print("Need to add somwhere around 20 or more..")
        elif generated_num-predicted_num > 0:
            print("You are close -  yeah add a bit more..")
    elif generated_num == predicted_num:
        print("Great, predicted number is equal to generated number.")
        query = False

    else:
        if predicted_num-generated_num >= 40:
            print("Need to lessen a lot!!")
        elif predicted_num-generated_num >= 20:
            print("Need to lessen around 20 or more...")
        elif predicted_num-generated_num >0:
            print("Need to lessen a bit...")

print(f"In {count} tries.")