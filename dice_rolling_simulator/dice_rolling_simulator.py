# This code is dice rolling simulator, playing 6 faced die

import random 

query = True
while query:
    num = random.randint(1,6)
    print(f"Number on die : {num}")
    question = input("Wanna play once more (y/n) ? : ")
    if question.lower() == 'y':
        query = True
    elif question.lower() == 'n':
        query = False
    else:
        print("Invalid Entry")
        query = False
