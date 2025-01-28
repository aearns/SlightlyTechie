# First python class - SlightlyTechie

print('Welcome to SlightlyTechie\n')

while True:
    StudentName = str (input("Please enter your name:\n"))
    if len(StudentName) == 1:
        print("Please type a valid name") 
    elif StudentName is int:
        print("Name cannot be a number")
    break
    
cohortList = range(1,4)
cohort = int (input("Choose your cohort: "))
if cohort not in cohortList:
    print("Choose between 1 and 4")

ListSpecialization = ["Backend", "Frontend", "Devops", "Data Analytics"]
StudentSpecialization = input("Please choose your specialization: ")
if StudentSpecialization not in ListSpecialization:
   print(f"Please select, %s \n", item.ListSpecialization) 


