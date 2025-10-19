# The program is to filter out 'username' and 'domain' in the email address of some user

email = input("Enter your Email address : ")


if email.count("@") < 1:
    print("Invalid Email Address, it needs at least a '@' . ")
elif email.count("@") == 1:
    split_email = email.split("@")
    print(f"Username : {split_email[0]}")
    print(f"Domain : {split_email[1]}")
else:
    print("Uh..Oh!, more than one '@', not allowed in emails.")