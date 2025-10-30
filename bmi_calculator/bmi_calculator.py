# | **Beginner** | **Data Manipulation** | **14. BMI Calculator** | Basic math, user input, conditional output. |

while True:
    # mass for user input
    mass = input("Entering the mass in (kg/pounds) ? ")
    if mass.lower() == 'kg':
        in_mass = float(input("Enter the mass in kilograms : "))
    elif mass.lower() == 'pounds':
        in_mass = float(input("Enter the mass in pounds : "))
        in_mass *= 0.453592
    else:
        continue
    # height for user input
    height = float(input("Enter the height in meters : "))
    bmi = in_mass/(height)**2
    print(f"Your BMI is : {bmi}")

    # BMI-based feedback
    if bmi >= 30:
        print("You are Obese!....you should seriously take care of your health.")
    elif 25 <= bmi < 30:
        print("You are overweight, run for a while, it will help you.")
    elif 18.5 <= bmi < 25:
        print("Healthy bud!!!!!...Well done.")
    else:
        print("You are underweight.")

    query = input("Want to check more (y/n) : ")
    # exit- if user wants to
    if query.lower() == 'n':
        print("Thanks for using BMI calculator 👋...Stay healthy.")
        break
