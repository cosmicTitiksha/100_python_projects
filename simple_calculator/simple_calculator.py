# This program is a Simple calculator, which can perform Addition, Subtraction, Multiplication, Division, remainder, exponent.
# | **Beginner** | **Console/CLI** | **1. Simple Calculator** | Basic operators, functions, user input. |
# (+, -, *, /, **, %)


# Functions for various operations
def add(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    sub = num1 - num2
    return sub

def mul(num1, num2):
    mul = num1 * num2
    return mul

def div(num1, num2):
    if num2 == 0:
        return "Invalid, num2 can not be zero!"
    else:
        div = num1 / num2
        return div
    
def exp(num1, num2):
    exp = num1 ** num2
    return exp

def rem(num1, num2):
    rem = num1 % num2
    return rem

# Running the loop for letting user perform different operations and calculations
while True:
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    operation = input("Enter the operation you want to perform(+, -, *, /, **, %) : ")
    if operation == '+':
        print(add(num1, num2))
    elif operation == '-':
        print(sub(num1, num2))
    elif operation == '*':
        print(mul(num1, num2))
    elif operation == '/':
        print(div(num1, num2))
    elif operation == '**':
        print(exp(num1, num2))
    elif operation == '%':
        print("Please enter both numbers as 'integers' only for correct results as modulo operation is for integers only. ")
        print(rem(int(num1), int(num2)))
    else:
        print("Invalid Operation, you can only +,-,*,/,**,%. ")

    # Asking the user, whether they have more calculations to perform
    query = input("Have more calculations to perform (y/n): ")
    if query.lower() == 'y':
        continue
    elif query.lower() == 'n':
        break
    else:
        print("Invalid entry...write either 'y' or 'n'.")
        continue

# Out of the loop
print("Thanks 👋 for using Simple Calculator...See you again, Soon ✌️")