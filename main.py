# ------------------------------------------------------------------------------------------------- #
# Title: Presentation Classes
# # Description: A collection of classes for managing presentation
# ChangeLog: (Who, When, What)
# Robby Hanovich, 7 June 2026, Created Script
# -------------------------------------------------------------------------------------------------

# Data -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'

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
menu_choice = ''