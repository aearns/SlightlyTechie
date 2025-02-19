# Personalized system
import logging

logging.basicConfig(filename='stud_ms.log', level=logging.DEBUG)

'''
    This program allows users to create a School Management System. Users can add, view, edit and delete student records.
    The program creates a secured (basic) admin/user. Access is granted to verified user to CRUD student records in the system.
    Program stores user details (name and password) and student details in a dict.
    This program implements data types, controls, functions, error handling and  logging module. 
'''

logging.basicConfig(filename='stud_ms.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
logging.info("App launch")

print("Welcome to your personalized system.")
#functions
users = {}
student_dir = {}

def user():
    '''
    This function returns a user in the system.
    This function creates user if one does not already exist
    '''
    username = str (input("Enter your name?\n")).title()
    if username not in users:
        logging.info("User not in DB. Creating a new user")
# Creating new user
        print(f"Hello {username}! Let's set you up.")           # add new user to the list of users
        while True:
            password = str(input("Enter a new password:\n"))
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
            logging.info("New user successfully created")                        
            print(f"Welcome {username}! Verified successfully.")                        
            print("Let's get started with your system!")
            
    else:
        print(f"Welcome back {username}!")
        logging.info("User found in system")
        confirm_password = input("Enter your password:\n")
        while password != confirm_password:
                print("Passwords do not match. Please try again.")
                # password = str (input("What is your password? "))
                # confirm_password = str (input("Confirm your password: "))
                break
        if password == confirm_password:
            print(f"Welcome back {username}! Verified successfully.")                        
            logging.INFO("User logged in successfully")
            

def add_student():
    '''
    This function adds a new student to the system
    '''
    global student_dir, username
    studentName = input("Enter name of student:\n").title()
    print(f"Adding {studentName} to your system...\nIndexing...")
    logging.info("Creating new student details")
    if studentName in student_dir:
        print(f"You already have {studentName} in your system")
        logging.info("Student already in system")
    else:
        while True:
            confirm_student = int (input(f"Select\n1. To confirm and add {studentName} to system\n2. To go back\nYour choice here: "))
            if confirm_student == 1:
                print(f"You have added {studentName} to your system")
                try:
                    programme = str (input(f"Enter programme of {studentName}:\n")).title()
                except ValueError:
                    print("Programme must be a text")
                    logging.error("User error. Wrong details entered")  
                    continue                      
                try:
                    level = int (input("Enter level:\n"))
                    if 100>= level <=400 :
                        continue
                    else:
                        print("Enter valid level")
                except ValueError:
                    print("Student level must be 100 - 400")
                    logging.error(f"User input {level} is incorrect.")
                    break
                student_dir[studentName]= (programme, level)
                print(f"Adding {studentName}, {programme} in level {level} to your system...\nIndexing...")
                logging.info(f"New student successfully added by {username}")
                # for book, publisher, date in  :
                break
            
            elif confirm_student == 2:
                pass
        
            else:
                print("Please enter a valid input")
                logging.error("User failed to enter valid input")
            break

def view_all():
    '''
    This function view all records of students
    '''
    global student_dir
    logging.info("User request for all records")
    if len(student_dir) >= 1:
        print("Loading all students in system")
        print(f"You have {len(student_dir)} in your system")
        for num, (student_dir, (programme, level)) in enumerate(student_dir.items(), start=1):
            print(f"{num}. {programme}, {level}")
        logging.info("Data request/pull successful")
    else:
       print("You have no record of students.\nLet's add students.")
    add_student()

def edit_record():
    '''
    Use this function to edit records
    '''
    print("Let's pick a student to edit")
    if len(student_dir) >= 1:
        for book, (title, (programme, level)) in enumerate(student_dir.items(), start=1):      
            edit_book = print(f"{book}. {title}, {programme}, {level}")
            if edit_book == range(len(student_dir)):
                new_name = input("Enter new student:\n")
                new_programme = input("Enter new programme:\n")
                new_level = input("Enter new level of student:\n")
                student_dir.pop(title)
                student_dir[new_name] = (new_programme, new_level)

    else:
        new_add = int (input("No student found in the system:\nPress 1. Add student\n2. Exit"))
        if new_add == 1:
            add_student()
        else:
            exit() 

def delete_record(student_dir, word):
    '''
    This function deletes student record
    '''
    search_record()
    for num in range(len(word)):                                                 
        delete_options = int(input(f"{num}. - {student_dir} \n"))
        if delete_options == num:
            student_dir.pop(num)
            print(f"Record{num} deleted from system")
        else:
            print("No record found")

def search_record(student_dir, word):
    '''
    Use this function to search details of record in the system
    '''
    #global student_dir
    search_query = input("Enter student name, programme or level of studente:\n").split()
    print("Listing all matches of students, programmes and levels found in your system")
    for word in search_query:
        if word in student_dir.item():
            print(f"{len(word)} matches found")
            for word, (student_dir, (programme, level)) in enumerate(student_dir.items(), start=1):
                print(f"-{word}")

def exit():
    exit

def courses():
    courses = []
    courses = str (input("Please enter student course:\n")).title
    while courses.isalpha():
        logging.info(f"{courses} successfully added")
        print(f"{courses} added successfully")
    else:
        print("Invalid course enter.")

def grades():
    student_grades = input("Please select student course to add grade:\n") 
    for i in courses:
        pass


while True:
    # Program menu
    user()
    print("Choose menu list\n1. Add new student\n2. View all students\n3. Edit student record\n4. Search student record\n5. Delete record\n6. Logout of account\n7. Exit system")
# Program menu - User inputs
    choice = (input("Enter your choice:\n "))
    if choice == "1":
        add_student()

    #User input 2 - View all books in system
    elif choice == "2":
        view_all()

    #Option 3 to edit a book in system
    elif choice == "3":
        edit_record()

    elif choice == "4":
        search_record()
    
    elif choice == "5":
        delete_record()

    elif choice == "6":
        user()

    elif choice == "7":
        exit()
    else:
        print("Enter a valid number")
