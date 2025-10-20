# The program generates random password of any number of digits
import random
import string 

num = int(input("How many characters are needed for password ? : "))
# options = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+={}[]:;,.<>/?`~'
# Using string methods instead of writing as commented just as above.
options = string.ascii_letters + string.digits + string.punctuation
options = list(options) #converting string to list so that random.choice can be used.

password_string = ''
for i in range(num):
    random_letter = random.choice(options)
    # Adding letter generated each time to password_String
    password_string += random_letter

# Printing the final password string
print(f"Your generated password is : {password_string}")
