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

def user():
    '''
    This function returns a user in the system.
    This function creates user if one does not already exist
    '''
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

def add_student():
    '''
    This function adds a new student to the system
    '''
    studentName = input("Enter name of student:\n").title()
    print(f"Adding {studentName} to your system...\nIndexing...")

    if studentName in student_dir:
        print(f"You already have {studentName} in your system")
    else:
        while True:
            confirm_student = int (input(f"Select\n1. To confirm and add {studentName} to system\n2. To go back\nYour choice here: "))
            if confirm_student == 1:
                print(f"You have added {studentName} to your system")
                try:
                    programme = str (input(f"Enter programme of {studentName}:\n")).title()
                except ValueError:
                    print("Programme must be a text")  
                    continue      
                while True:
                    try:
                        level = int (input("Enter level:\n"))
                        if 1>= level <=4 :
                            break
                        else:
                            print("Enter valid level")
                    except ValueError:
                        print("Student level must be 1-4")
                    
                student_dir[studentName]= (programme, level)
                print(f"Adding {studentName}, {programme} in level {level} to your system...\nIndexing...")
                # for book, publisher, date in  :
                break
            
            elif confirm_student == 2:
                pass
        
            else:
                print("Please enter a valid input")
            break

def view_all():
    print("Loading all students in system")
    if len(student_dir) >= 1:
        print(f"You have {len(student_dir)} in your system")
        for text, (student_dir, (programme, level)) in enumerate(student_dir.items(), start=1):
            print(f"{text}. {title}, {programme}, {level}")
    else:
        print("You have not added a book yet.\nLet's add a book")
# Program start

def edit_record():
    print("Let's pick a student to edit")
    if len(student_dir) >= 1:
        for book, (title, (programme, level)) in enumerate(student_dir.items(), start=1):      #
            edit_book = print(f"{book}. {title}, {programme}, {level}")
            if edit_book == range(len(student_dir)):
                new_name = input("Enter new student:\n")
                new_programme = input("Enter new programme:\n")
                new_level = input("Enter new level of student:\n")
                student_dir.pop(title)
                student_dir[new_name]= (new_programme, new_level)

        else:
            print("You have not added a book yet")

def delete_record(student_dir, word):
    search_record()
    for num in range(len(word)):                                                 
        delete_options = int(input(f"{num}. - {student_dir} \n"))
        if delete_options == num:
            student_dir.pop(num)
            print(f"Record{num} deleted from system")
        else:
            print("No record found")

def search_record():
    search_query = input("Enter student name, programme or level of studente:\n").split()
    print("Listing all matches of books, programmes and levels found in your system")
    for word in search_query:
        if word in student_dir.item():
            print(f"{len(word)} matches found")
        #   for word, (title, (programme, level)) in enumerate(student_dir.items(), start=1)
            print(f"-{student_dir}")

def exit():
    exit
username = str (input("Enter your name?\n")).title()

while True:
    # Program menu
    print("Choose menu list\n1. Add new student\n2. View all students\n3. Edit student record\n4. Delete record\n5. Exit system")
# Program menu - User inputs
    choice = (input("Enter your choice:\n "))
    if choice == "1":
        user()
    #User input 2 - View all books in system
    elif choice == "2":
        add_student()
        # code should run program menu screen line 41

    #Option 3 to edit a book in system
    elif choice == "3":
        view_all()

    elif choice == "5":
        search_record()
    
    elif choice == "4":
        delete_record()

    elif choice == "6":
        exit()
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