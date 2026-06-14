# ------------------------------------------------------------------------------------------------- #
# Title: Data Classes
# # Description: Contains the Person Class and Employee classes.
# ChangeLog: (Who, When, What)
# Robby Hanovich, 7 June 2026, Created Script
# -------------------------------------------------------------------------------------------------

from datetime import date

class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    - Robby Hanovich, 7 June 2026, imported the class to Data Classes Module and added ability
        to enter compound first, compound last names, and names with '.  For example Mary Sue O'Connor.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        # Allow for compound first names like Mary Sue
        # Strip extra spaces
        while value.find("  ") != -1:
            value = value.replace("  ", " ")

        for char in value: # Allow for ' in name like D'ante
            if (char.isalpha() or char in "'" or char in " "):
                continue
            else:
                raise ValueError("The first name should not contain numbers.")
        self.__first_name = value.title()

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        # Allow for compound first names like Van Burry or D'ante
        # Strip extra spaces
        while value.find("  ") != -1:
            value = value.replace("  ", " ")

        for char in value: #allow for ' in last name like O'Connor
            if (char.isalpha() or char in "'" or char in " "):
                continue
            else:
                raise ValueError("The last name should not contain numbers.")
        self.__last_name = value.title()

    def __str__(self):
        return f"{self.first_name},{self.last_name}"


class Employee(Person):
    """
    A class representing employee data.

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (date): The data of the employee review.
    - review_rating (int): The review rating of the employee's performance (1-5)

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    - Robby Hanovich, 7 June 2026, imported the class to Data Classes Module.
    """

    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):

        super().__init__(first_name=first_name,last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError ("Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: int):
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError ("Please choose only values 1 through 5")

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.review_date},{self.__review_rating}"

if __name__ == '__main__':
    print("\n\nThis file contains the Person and Employee classes and is not meant to execute stand-alone. "
          "Please run main.py\n\n")