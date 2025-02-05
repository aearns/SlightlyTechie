
user = str (input("Please enter your name: "))
print(f"Hello, {user}!")

number_of_friends = int (input("How many friends do you have? "))
friend_list = []
print(f"You will be prompted to enter the name of each of your {number_of_friends} friends")
confirm_number = input("Type 'Yes' to continue, or 'No' to exit or change the number of friends")
if confirm_number == "Yes":
    for friend in range(number_of_friends):
        

if number_of_friends == 0:
    print("You don't have any friends. That's okay, we all have our own company")
    else:
        for i in range(number_of_friends):
# for friend in range(number_of_friends):
#     name_of_friend = str(input("Please enter your friend's name: "))
#     friend_list.append(name_of_friend)
friend_names = str(input(f"Please enter the names of your {number_of_friends} separated by a comma:\n"))

print("Nice to have friends such as:")
for names in friend_list:
    print(names)
    
    
