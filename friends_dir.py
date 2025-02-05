
#Friend list of a user

user = str(input("Please enter your name: "))                       #user input
print(f"Hello, {(user.title())}!\nWelcome")

while True:                                                         #
    number_of_friends = input("How many friends do you have? ")
    if number_of_friends.isdigit():
        number_of_friends = int(number_of_friends)
        break                                                           # Exit the loop if the input is a valid number
    else:
        print("Please enter a valid number")

print(f"You have {number_of_friends} friends.\nYou will be prompted to enter the name of each of your {number_of_friends} friends")
    
friend_list = []
confirm_number = input("Type 'Yes' to continue, 'No' to exit or 'Change' the number of friends:\n")
if confirm_number.upper() == "YES":
    for friend in range(number_of_friends):
        name_of_friend = str(input("Please enter your friend's name: "))
        friend_list.append((name_of_friend.title()))
elif confirm_number.upper() == "CHANGE":
    print("Let's change the number of friends you have")
    number_of_friends = int(input("How many friends do you have?\n "))
    print(f'You now have {number_of_friends} friends')
else:
    if confirm_number.upper() == "NO":
        print(f"Goodbye, {user}! Have a nice day!")
    exit()


friend_name = str(input(f"Please enter the names of your {number_of_friends} separated by a comma:\n"))

for names in friend_list:
    friend_list.append(name_of_friend)
    print(names)
print(f"Nice to have friends such as {name_of_friend} ")
    
    
