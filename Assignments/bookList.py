# Personalized library
'''
    This program allows users to create a personalized library. Users can add, view, edit and delete books from their library.
    Users can also search for books in their library.\n 
'''
print("Welcome to your personalized library.")
#functions
# start_program()
# user_details()
# program_menu()

users = []
AllBooks = []

# Program start
user_name = str (input("Enter your name?\n")).title()
if user_name not in users:
# Creating new user
    print(f"Hello {user_name}! Let's set you up.")           # add new user to the list of users
    # users.append(user_name)
    while True:
        password = input("Enter a new password:\n")
        if len(password) >= 8 and password.isalnum():
            print("Let's confirm your password!")
            confirm_password = input("Confirm your password:\n")
            while password != confirm_password:
                print("Passwords do not match. Please try again.")
                # password = str (input("What is your password? "))
                # confirm_password = str (input("Confirm your password: "))
                break
            break
        else:
            print("Password must contain letters and numbers.\nIt must be at least 8 characters.")
    
    if password == confirm_password:
        users.append({"name": user_name, "password": password})
        print(f"Welcome {user_name}! Verified successfully.")                        
else:
    print(f"Welcome back {user_name}!")
 
print("Let's get started with your library!")

# Program menu
print("Choose menu list\n1. Add new book\n2. View all books in your library\n3. Edit a book\n4. Delete a book\n5. Restart program\n6. Exit library")

# Program menu - User inputs
while True:
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
                    author = str (input(f"Enter author of {bookTitle}\n")).title()
                    while True:
                        try:
                            year = int (input("Enter year of publication:\n"))
                            if year <= 1000:
                                print("Year of publication must be greater than 1400")
                            else:    
                                continue
                        except ValueError:
                            print("Year of publication must be a number")
                            break
                    print(f"Adding {bookTitle} by {author} published in {year} to your library...\nIndexing...")
                    AllBooks.append((bookTitle, author, year))
                    break
                elif confirm_book == "2":
                    bookTitle = input("Enter title of book:\n")
                    AllBooks.append(bookTitle)
                elif confirm_book == "3":
                    print(f"Goodbye, {user_name}")
                else:
                    print("Please enter a valid input")
                break

    #User input 2 - View all books in library
    elif choice == "2":
        print("Loading all AllBooks in library")
        if len(AllBooks) >= 1:
            for book in AllBooks:
                print(book)
        else:
            print("You have not added a book yet.\n Let's add a book")
        # code should run program menu screen line 41

    #Option 3 to edit a book in library
    elif choice == "3":
        print("Let's pick a book to edit")
        if len(AllBooks) >= 1:
            for book in AllBooks:
                print(AllBooks)
            for i, book in enumerate(AllBooks):
                edit_book = input(f"BookOption: {i+1}, Title: {AllBooks}")
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