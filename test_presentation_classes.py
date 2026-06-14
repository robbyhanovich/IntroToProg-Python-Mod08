# ------------------------------------------------------------------------------------------------- #
# Title: Test_presentation_classes
# # Description: A collection of methods to test the Presentation class IO.
# ChangeLog: (Who, When, What)
# Robby Hanovich, 7 June 2026, Created Script
# -------------------------------------------------------------------------------------------------

import unittest
from unittest.mock import patch

from data_classes import Employee
from presentation_classes import IO


class TestIO (unittest.TestCase):

    def setUp (self):
        self.employee_info: list[Employee] = []


    def test_input_menu_choice_valid (self):
        # Test valid entries 1 - 4
        with patch ('builtins.input', return_value = "1"):
            choice = IO.input_menu_choice()
            self.assertEqual("1",choice)
        with patch ('builtins.input', return_value = "2"):
            choice = IO.input_menu_choice()
            self.assertEqual("2",choice)
        with patch ('builtins.input', return_value = "3"):
            choice = IO.input_menu_choice()
            self.assertEqual("3",choice)
        with patch ('builtins.input', return_value = "4"):
            choice = IO.input_menu_choice()
            self.assertEqual("4",choice)

    def test_input_employee_data (self):
        # Test capturing user input and validate input captured in employee_info
       with patch ('builtins.input',side_effect=["Vic", "Vu", "2026-04-25",5]):
            self.employee_info = IO.input_employee_data(employee_data= self.employee_info,employee_type= Employee())

            self.assertEqual(1, len(self.employee_info))
            self.assertEqual("Vic",self.employee_info[0].first_name)
            self.assertEqual("Vu",self.employee_info[0].last_name)
            self.assertEqual("2026-04-25",self.employee_info[0].review_date)
            self.assertEqual(5,self.employee_info[0].review_rating)



if __name__ == "__main__":
    unittest.main ()
