# ------------------------------------------------------------------------------------------------- #
# Title: Test_data_classes
# # Description: A collection of methods to test the data classes Person and Employee.
# ChangeLog: (Who, When, What)
# Robby Hanovich, 7 June 2026, Created Script
# -------------------------------------------------------------------------------------------------

import unittest
from data_classes import Person, Employee

class TestPerson (unittest.TestCase):
    """ This test checks the Person class for valid and invalid entries

    ChangeLog: (Who, When, What)
    Robby Hanovich, 13 June 2026, created test script
    """

    # Test valid Person names; simple "Vic", compound "Mary Sue", allow ' "D'ante"
    def test_person_init (self):
        person = Person ("Vic", "Vu")

        # Simple first and last names
        self.assertEqual( "Vic", person.first_name)
        self.assertEqual( "Vu", person.last_name)

        # Compound first or last names
        person = Person ("Mary Sue", "Van Buran")
        self.assertEqual( 'Mary Sue', person.first_name)
        self.assertEqual( 'Van Buran', person.last_name)

        # Use of ' in first or last names
        person = Person("D'ante", "O'Connor")
        self.assertEqual( "D'Ante", person.first_name)
        self.assertEqual( "O'Connor", person.last_name)

        #Use of compound first or last name with '
        person = Person("Jeff D'Ante", "Smith O'Connor")
        self.assertEqual( "Jeff D'Ante", person.first_name)
        self.assertEqual( "Smith O'Connor", person.last_name)

    # Test invalid names; those with numbers or symbols
    def test_person_invalid_entries (self):
        with self.assertRaises(ValueError):
            person = Person ("Vic 1", "Vu%")
            person = Person("Vic$", "Vu232")

    # Test __str__ returns first and last name separated by a coma "Vic,Vu"
    def test_person_string (self):
        person = Person ("Vic", "Vu")
        self.assertEqual("Vic,Vu", str(person))

class TestEmployee (unittest.TestCase):
    """ This test checks the Employee class for valid and invalid entries

    ChangeLog: (Who, When, What)
    Robby Hanovich, 13 June 2026, created test script
    """

    # Test Employee class review_date and review rating init
    def test_employee_init (self):
        employee = Employee("Vic","Vu", "2026-03-23",4)
        self.assertEqual("2026-03-23",employee.review_date)
        self.assertEqual(4,employee.review_rating)

    def test_employee_invalid_entries (self):

        # Review_date should be in "YYYY-MM-DD" format
        with self.assertRaises(ValueError):
            # Test MM-DD-YYYY format
            Employee("Vic", "Vu", "03-23-2026", 4)
            # Test DD-MM-YYYY format
            Employee("Vic", "Vu", "23-03-2026", 4)

        # review_rating range is 1 - 5, check values > 5 and less than 1
        with self.assertRaises(ValueError):
            # Test review_rating > 5
            Employee("Vic", "Vu", "2026-03-23", 6)
            # Test review_rating <1
            Employee("Vic", "Vu", "2026-03-23", 0)
            # Test review_rating as decimal
            Employee("Vic", "Vu", "2026-03-23", 1.6)
            # Test review_rating as letter
            Employee("Vic", "Vu", "23-03-2026", "abc")

    def test_employee_string (self):
        employee = Employee("Vic","Vu", "2026-03-23",4)
        self.assertEqual("Vic,Vu,2026-03-23,4", str(employee))

if __name__ == "__main__":
    unittest.main ()

