# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
#
# ------------------------------------------------------------------------------------------------- #

from data_classes import Employee
from processing_classes import FileProcessor
from presentation_classes import IO

# Data -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'
FILE_WRITTEN_FLAG: bool = False # flag to track if data is saved to file before exit
DATA_ADDED_FLAG: bool = False #flag to track if data has been added

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

employees: list = []  # a table of employee data
menu_choice: str = ''

# Beginning of the main body of this script
employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                       employee_data=employees,
                                                       employee_type=Employee)  # Note this is the class name (ignore the warning)

# Repeat the following tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)  # Note this is the class name (ignore the warning)
        except Exception as e:
            IO.output_error_messages(e)
        else:
            IO.output_employee_data(employee_data=employees) #moved from try statement so it only executes if data successfully added
            DATA_ADDED_FLAG = True
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        else:
            FILE_WRITTEN_FLAG = True
            print(f"Data was saved to the {FILE_NAME} file.") #moved from try statement so it only executes if data successfully written
        continue

    elif menu_choice == "4":  # End the program
            #Check to see if data was saved and prompt user
            if (DATA_ADDED_FLAG == True) and (FILE_WRITTEN_FLAG == False): # data added file not saved.
                print(f"Data not saved to {FILE_NAME}.\n")  # prompt user
                menu_choice = input("Confirm you want to exit without saving your data (Y/N)?")

                if menu_choice == "Y":
                    print (f"Closing the program.  Thank you and have a great day!\n")
                    break  # out of the while loop
                else:
                    print("Returning to menu.\n")
                    continue

            else:
                if (DATA_ADDED_FLAG == False):
                    print("No new data added, closing the program.  Thank you and have a great day!\n")
                else:
                    print ("New employee ratings added and saved.  Closing the program. Have a great day!\n")
                break  # out of the while loop