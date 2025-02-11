# Personalized library
'''
    This program allows users to create a personalized library. Users can add, view, edit and delete books from their library.
    Users can also search for books in their library.
    Program stores user details (name and password) and books in a list. - not efficient but for learning purposes
    Program does not use any functions. 
'''
print("Welcome to your personalized library.")
#functions
# start_program()
# user_details()
# program_menu()

users = {}
books_dir = {}

# Program start
username = str (input("Enter your name?\n")).title()
if username not in users:
# Creating new user
    print(f"Hello {username}! Let's set you up.")           # add new user to the list of users
    # users.append(username)
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
        users.update({"name": username, "password": password})
        print(f"Welcome {username}! Verified successfully.")                        
    print("Let's get started with your library!")
else:
    print(f"Welcome back {username}!")
 

while True:
    # Program menu
    print("Choose menu list\n1. Add new book\n2. View all books in your library\n3. Edit a book\n4. Delete a book\n5. Restart program\n6. Exit library")
# Program menu - User inputs
    choice = (input("Enter your choice: "))
    if choice == "1":
        bookTitle = input("Enter title of book:\n").title()
        print(f"Let's add {bookTitle} to your library...\nIndexing...")

        if bookTitle in books_dir:
            print(f"You already have {bookTitle} in your library")
        else:
            while True:
                confirm_book = int (input(f"Select\n1. To confirm and add {bookTitle} to library\n2. To go back\nYour choice here: "))
                if confirm_book == 1:
                    print(f"You have added {bookTitle} to your library")
                    try:
                        author = str (input(f"Enter author of {bookTitle}\n")).title()
                    except ValueError:
                        print("Author must be a name")  
                        continue      
                    while True:
                        try:
                            year = int (input("Enter year of publication:\n"))
                            if year >= 1000:
                               break
                            else:
                                print("Enter valid year")
                        except ValueError:
                            print("Year of publication must be a number")
                        
                    print(f"Adding {bookTitle} by {author} published in {year} to your library...\nIndexing...")
                    # for book, publisher, date in  :
                    books_dir.update({bookTitle: author})
                    break
                
                elif confirm_book == 2:
                    pass
           
                else:
                    print("Please enter a valid input")
                break
        
    #User input 2 - View all books in library
    elif choice == "2":
        print("Loading all books in library")
        if len(books_dir) >= 1:
            for title, writer in books_dir.items():
                print(f"- {title}, {writer}")
        else:
            print("You have not added a book yet.\nLet's add a book")
        # code should run program menu screen line 41

    #Option 3 to edit a book in library
    elif choice == "3":
        print("Let's pick a book to edit")
        if len(books_dir) >= 1:
            for book in books_dir:
                print(books_dir)
            for title, writer, year in books_dir.items():
                edit_book = input(f"BookOption: {i+1}, Title: {books_dir}")
        else:
            print("You have not added a book yet")

    elif choice == "4":
        search_query = input("Search title, author or publication year of book to delete:\n").split()
        print("Listing all matches of books, authors and years found in your library")
        for word in search_query:
            if word in books_dir.item():
                print(f"{len(word)} matches found")
                print(f"-{books_dir}")
                for num in range(len(word)):
                    delete_options = input(f"{num}. -{books_dir}")
                    if delete_options == num:
                        books_dir.pop()
                        print(f"{books_dir} deleted from library")
                    else:
                        pass
    else:
        print("Enter a valid number")



    # user_search = input("Enter title to search")
    # if user_search in bookTitle(*bookTitle):
    #     for book in books_dir:
    #         print(*books_dir)
    # add_new
    # del_book
    # view_all
    # delete_all_books_dir
    # delete_history
    #