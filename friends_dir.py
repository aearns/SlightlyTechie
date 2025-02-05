
user = str (input("Please enter your name: "))
print(f"Hello, {user}!, welcome")

number_of_friends = int (input("How many friends do you have? "))
friend_list = []
print(f"You will be prompted to enter the name of each of your {number_of_friends} friends")
confirm_number = input("Type 'Yes' to continue, 'No' to exit or 'Change' the number of friends:\n")
if confirm_number.upper() == "YES":
    for friend in range(number_of_friends):
        name_of_friend = str(input("Please enter your friend's name: "))
        friend_list.append(name_of_friend)
elif confirm_number.upper() == "CHANGE":
    print("Let's change the number of friends you have")
    number_of_friends = int(input("How many friends do you have?\n "))
    print(f'You now have {number_of_friends} friends')
else:
    if confirm_number.upper() == "NO":
        print("Goodbye, {user}! Have a nice day!")
    exit()


friend_name = str(input(f"Please enter the names of your {number_of_friends} separated by a comma:\n"))

for names in friend_list:
    friend_list.append(name_of_friend)
    print(names)
print("Nice to have friends such as:")
    
    
