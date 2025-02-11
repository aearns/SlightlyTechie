# Personalized system
'''
    This program allows users to create a School Management System. Users can add, view, edit and delete student records.
    Users can also search for students in their system.
    Program stores user details (name and password) and student details in a list. - not efficient but for learning purposes
    Program does not use any functions. 
'''
print("Welcome to your personalized system.")
#functions
# start_program()
# user_details()
# program_menu()

users = {}
student_dir = {}

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
    print("Let's get started with your system!")
else:
    print(f"Welcome back {username}!")
 

while True:
    # Program menu
    print("Choose menu list\n1. Add new student\n2. View all students\n3. Edit student record\n4. Delete record\n5. Restart program\n6. Exit system")
# Program menu - User inputs
    choice = (input("Enter your choice: "))
    if choice == "1":
        studentName = input("Enter name of student:\n").title()
        print(f"Adding {studentName} to your system...\nIndexing...")

        if studentName in student_dir:
            print(f"You already have {studentName} in your system")
        else:
            while True:
                confirm_book = int (input(f"Select\n1. To confirm and add {studentName} to system\n2. To go back\nYour choice here: "))
                if confirm_book == 1:
                    print(f"You have added {studentName} to your system")
                    try:
                        author = str (input(f"Enter programme of {studentName}:\n")).title()
                    except ValueError:
                        print("Programme must be a text")  
                        continue      
                    while True:
                        try:
                            year = int (input("Enter level:\n"))
                            if year >= 1000:
                               break
                            else:
                                print("Enter valid year")
                        except ValueError:
                            print("Year of publication must be a number")
                        
                    student_dir[studentName]= (author, year)
                    print(f"Adding {studentName} by {author} published in {year} to your system...\nIndexing...")
                    # for book, publisher, date in  :
                    break
                
                elif confirm_book == 2:
                    pass
           
                else:
                    print("Please enter a valid input")
                break
        
    #User input 2 - View all books in system
    elif choice == "2":
        print("Loading all books in system")
        if len(student_dir) >= 1:
            print(f"You have {len(student_dir)} in your system")
            for text, (title, (writer, year)) in enumerate(student_dir.items(), start=1):
                print(f"{text}. {title}, {writer}, {year}")
        else:
            print("You have not added a book yet.\nLet's add a book")
        # code should run program menu screen line 41

    #Option 3 to edit a book in system
    elif choice == "3":
        print("Let's pick a book to edit")
        if len(student_dir) >= 1:
            for book, (title, (writer, year)) in enumerate(student_dir.items(), start=1):      #b
                edit_book = print(f"{book}. {title}, {writer}, {year}")
                if edit_book == range(len(student_dir)):
                    new_title = input("Enter new title of book:\n")
                    new_author = input("Enter new author of book:\n")
                    new_year = input("Enter new year of publication:\n")
                    student_dir.pop(title)
                    student_dir[new_title]= (new_author, new_year)

            else:
                print("You have not added a book yet")

    elif choice == "4":
        search_query = input("Enter title, author or publication year of book to delete:\n").split()
        print("Listing all matches of books, authors and years found in your system")
        for word in search_query:
            if word in student_dir.item():
                print(f"{len(word)} matches found")
            #   for word, (title, (writer, year)) in enumerate(student_dir.items(), start=1)
                print(f"-{student_dir}")
                for num in range(len(word)):
                    delete_options = input(f"{num}. - {student_dir} \n")
                    if delete_options == num:
                        student_dir.pop()
                        print(f"{student_dir} deleted from system")
                    else:
                        pass
    else:
        print("Enter a valid number")



    # user_search = input("Enter title to search")
    # if user_search in studentName(*studentName):
    #     for book in student_dir:
    #         print(*student_dir)
    # add_new
    # del_book
    # view_all
    # delete_all_student_dir
    # delete_history
    #