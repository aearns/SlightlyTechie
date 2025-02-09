

print("Welcome to your personalized library.")
users = []
AllBooks = []
start_program = ()

user_name = str (input("Enter your name?\n")).title()
if user_name not in users:
    print(f"Hello {user_name}! Let's set you up")           # add new user to the list of users
    # users.append(user_name)
    password = (input("Enter a new password:\n"))
    if len(password) >= 8 and password.isalnum():
        confirm_password = str (input("Confirm your password:\n "))
    else:
        print("Password must be longer than 8 characters and must contain numbers")
    while password != confirm_password:
        print("Passwords do not match. Please try again.")
        # password = str (input("What is your password? "))
        # confirm_password = str (input("Confirm your password: "))
        break

    if password == confirm_password:
        users.append({"name": user_name, "password": password})
        print(f"Welcome {user_name}! Verified successfully")
                     
else:
    print(f"Welcome back {user_name}!")
 
print("Let's get started with your library!")

print("Choose menu list\n1. Add new book\n2. View all AllBooks in library\n3. Edit a book\n4. Delete a book\n5. Exit library")

choice = (input("Enter your choice: "))


if choice == "1":
    bookTitle = input("Enter title of book:\n").title()
    print(f"Let's add {bookTitle} to your library...\nIndexing...")

    if bookTitle in AllBooks:
        print(f"You already have {bookTitle} in your library")
    else:
        while True:
            confirm_book = input(f"Press\n1. To confirm {bookTitle} and add to library\n2. To edit title\n3. To exit:\n")
            if confirm_book == "1":
                print(f"You have added {bookTitle} to your library")
                author = str (input("Enter author of {bookTitle}\n")).title()
                year = input("Enter year of publication:\n")
                print(f"Adding {bookTitle} by {author} published in {year} to your library...\nIndexing...")
                AllBooks.append((bookTitle, author, year))
            elif confirm_book == "2":
                bookTitle = input("Enter title of book:\n")
                AllBooks.append(bookTitle)
            elif confirm_book == "3":
                print("Goodbye")
            else:
                print("Please enter a valid input")
            break

elif choice == "2":
    print("Loading all AllBooks in library")
    for book in AllBooks:
        print(book)
elif choice == "3":
    print("Let's pick a book to edit")
    if len(AllBooks) > 1:
        for book in AllBooks:
            print(AllBooks)
        for i, book in enumerate(AllBooks):
            print(f"BookOption: {i+1}, Title: {AllBooks}")

    else:
        print("You have not added a book yet")
else:
    print("Enter a valid number")


# user_search = input("Enter title to search")
# if user_search in bookTitle(*bookTitle):
#     for book in AllBooks:
#         print(*AllBooks)
# add_new
# del_book
# view_all
# delete_all_AllBooks
# delete_history
#