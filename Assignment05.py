# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # dictionary of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
except FileNotFoundError as e: # Added exceptions here in order to ensure the file exists
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except TypeError as e:
    print("Please check that the data is a valid .csv format\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("-- Technical Error Message -- ")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    for each_row in file.readlines():
        student_data = each_row.strip().split(',')
        student_data = {"FirstName": student_data[0], "LastName": student_data[1], "CourseName": student_data[2]}
        students.append(student_data)
    file.close()

# Present and Process the data
while (True):
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try: # writing an exception case if user enters numbers into the name input
            student_first_name = input("Enter the student's first name: ")
        except ValueError as e:
            print("Please make sure you only entered letters\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        try: # writing an exception case if user enters numbers into the name input
            student_last_name = input("Enter the student's last name: ")
        except ValueError as e:
            print("Please make sure you only entered letters\n")
            print("-- Technical Error Message -- ")
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        try: # writing general exception for course name
            course_name = input("Please enter the name of the course: ")
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        finally:
        # Collect the data
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("\n--- Displaying current data ---")
        for student_data in students:
            print(f'{student_data["FirstName"]},{student_data["LastName"]},{student_data["CourseName"]}')
        print("=" * 30)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file = open(FILE_NAME, 'w')
        for student in students:
            file.write(f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}\n')
        file.close()
        print('Data saved!')
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
