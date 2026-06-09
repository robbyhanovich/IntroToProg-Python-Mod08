# ------------------------------------------------------------------------------------------------- #
# Title: Processing Classes
# # Description: A collection of classes for managing file processing.
# ChangeLog: (Who, When, What)
# Robby Hanovich, 7 June 2026, Created Script
# -------------------------------------------------------------------------------------------------

from data_classes import Employee
import json

class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    Robby Hanovich, 7 June 2026, imported class to File Processor class module.
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee):
        """ This function reads data from a JSON file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param file_name: string data with name of file to read from
        :param employee_data: list of dictionary rows to be filled with file data
        :param employee_type: a reference to the Employee class
        :return: list
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_data.append(Employee(first_name=employee['FirstName'],
                                                  last_name= employee['LastName'],
                                                  review_date=employee['ReviewDate'],
                                                  review_rating=employee['ReviewRating']))

        except FileNotFoundError:
            raise FileNotFoundError("Text file must exist before running this script!")
        except Exception:
            raise Exception("There was a non-specific error!")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """ This function writes data to a JSON file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file, indent=2)
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permission")
        except Exception as e:
            raise Exception("There was a non-specific error!")


if __name__ == '__main__':
    print("\n\nThis file contains the File Processor and is not meant to execute stand-alone. "
          "Please run main.py\n\n")