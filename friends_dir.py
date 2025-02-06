# Creating a friend list

user = str(input("Please enter your name: "))                       #user input
print(f"Hello {(user.title())}, Welcome!")

while True:                                                         #
    number_of_friends = input("How many friends do you have? ")
    if number_of_friends.isdigit():
        number_of_friends = int(number_of_friends)
        break                                                       # Exit the loop if the input is a valid number
    else:
        print("Please enter a valid number")

print(f"You have {number_of_friends} friends.\nYou will be prompted to enter the name of each of your friends")
    
friend_list = []
confirm_number = input("Type 'Yes' to continue, 'No' to exit or 'Change' the number of friends:\n")
while True:
    if confirm_number.upper() == "YES":
        for friend in range(number_of_friends):
            name_of_friend = str(input("Please enter your friend's name: "))
            friend_list.append((name_of_friend.title()))
    elif confirm_number.upper() == "CHANGE":
        print("Let's change the number of friends you have")
        number_of_friends = int(input("How many friends do you have?\n "))
        print(f'You now have {number_of_friends} friends')
    elif confirm_number.upper() == "NO":
        print(f"Goodbye {user.title}! Have a nice day!")
        exit()
    else: 
        print("Please enter 'Yes', 'No', or 'Change'")
    break

print(f"You have {number_of_friends} friends,", *friend_list, sep=" and ")

# friend_name = str(input(f"Please enter the names of your {number_of_friends} separated by a comma:\n"))
'''

for names in friend_name:
    friend_list.append(name_of_friend)
    print(friend_list)
print(f"Nice to have friends such as {name_of_friend} ")
    
'''
# friends_age = input(f"Please provide the age of your friend {(friend_list[0])}(separated by a comma (,)):\n")

ages = []
while True:                   #initialize empty list to store the ages
    for name in friend_list:
        age = input(f"What is the age of {name}? ")
        if age.isdigit():
            ages.append({name:age})
            break
        else:
            print("Please enter a valid age")
    break

while True:   
    colors = {}
    for name in friend_list:
        color = input(f"What is the favorite color of {name}? ")
        if color.isalpha():
            colors[name] = color
        else:
            print("Please enter a color")
    break

print(friend_list, ages, colors)

