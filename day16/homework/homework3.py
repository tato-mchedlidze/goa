correct_password = "tatuka_2008"
correct_username = "tatomchedlidze"
user_guess = input("Enter password: ")
user_guess = input("Enter username: ")
counter = 0

while user_guess != correct_password or correct_username:
    user_guess = input("Enter password: ")
    user_guess = input("Enter username: ")
    counter += 1


print("Access granted")
print("Your guess count:", str(counter))