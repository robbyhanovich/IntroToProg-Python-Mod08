# ------------------------------------------------------------------------------------------------- #
# Title: Test_processing_classes.
# # Description: A collection of methods to test the processing class FileProcessor.
# ChangeLog: (Who, When, What)
# Robby Hanovich, 7 June 2026, Created Script
# -------------------------------------------------------------------------------------------------

import os
import stat
import json
import tempfile
import unittest
from json import JSONDecodeError
from stat import S_IWRITE

from processing_classes import FileProcessor
from data_classes import Employee

class TestFileProcessor (unittest.TestCase):
    """ This test checks the FileProcessor class to ensure it can read and write data to a JSON file.

        ChangeLog: (Who, When, What)
        Robby Hanovich, 13 June 2026, created test script
    """

    def setUp (self):
        self.temp_file = tempfile.NamedTemporaryFile(delete = False)
        self.temp_file_name = self.temp_file.name
        self.employee_info: list[Employee] = []

    def tearDown (self):
        self.temp_file.close()

    def test_read_employee_file (self): # Create test data and write to file

        """ This test checks the FileProcessor class to ensure it can read data from a JSON file.

            ChangeLog: (Who, When, What)
            Robby Hanovich, 13 June 2026, created test script
        """
        # Create sample data
        sample_data = [
              {"FirstName": "Vic","LastName": "Vu", "ReviewDate": "2025-02-12","ReviewRating": 5},
              {"FirstName": "Sue","LastName": "Jones","ReviewDate": "2025-03-12","ReviewRating": 4}
            ]

        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data,file)

        # read in the test data
        self.employee_info = FileProcessor.read_employee_data_from_file(file_name=self.temp_file_name,
                                                               employee_data=self.employee_info,
                                                               employee_type=Employee())
        # Check test data length matches data read in
        self.assertEqual(len(sample_data),len (self.employee_info))

        #check each value
        for i in range (len (sample_data)):
            self.assertEqual(sample_data[i]['FirstName'],self.employee_info[i].first_name)
            self.assertEqual(sample_data[i]['LastName'],self.employee_info[i].last_name)
            self.assertEqual(sample_data[i]['ReviewDate'],self.employee_info[i].review_date)
            self.assertEqual(sample_data[i]['ReviewRating'],self.employee_info[i].review_rating)

    def test_read_employee_file_errors (self):

        # Test file not found
        with self.assertRaises(FileNotFoundError):
            self.employee_info = FileProcessor.read_employee_data_from_file(file_name="",
                                                                   employee_data=self.employee_info,
                                                                   employee_type=Employee())

        # Test JSON Decode Error
        with self.assertRaises(JSONDecodeError): #
            # Create file with some data
            with open (self.temp_file_name,"w") as file:
                file.write( "Hello World")
                file.close()

            # Try to read the file in as JSON
            with open(self.temp_file_name, "r") as file:
                file_data = json.load(file)

        # Test file permission error
        with self.assertRaises(PermissionError): # ("Please check the data file's read/write permission")
            os.chmod(self.temp_file_name,stat.S_IREAD)
            with open (self.temp_file_name,"w") as file:
                file.close()

            #reset permissions
            os.chmod(self.temp_file_name,stat.S_IREAD | S_IWRITE)

    def test_write_employee_file (self):

        """ This test checks the FileProcessor class to ensure it can write data to a JSON file.

            ChangeLog: (Who, When, What)
            Robby Hanovich, 13 June 2026, created test script
        """
        # Create sample data
        self.employee_info= []
        self.employee_info.append(Employee("Vic","Vu", "2023-03-12",3))
        self.employee_info.append(Employee("Mary Sue","Lu", "2023-03-16",5))

        # Write the data to the file
        FileProcessor.write_employee_data_to_file(self.temp_file_name, employee_data= self.employee_info)

        # Read the data from the file and check it matches the expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data),len (self.employee_info))

        #check each value
        for i in range (len(file_data)):
            self.assertEqual(file_data[i]['FirstName'],self.employee_info[i].first_name)
            self.assertEqual(file_data[i]['LastName'],self.employee_info[i].last_name)
            self.assertEqual(file_data[i]['ReviewDate'],self.employee_info[i].review_date)
            self.assertEqual(file_data[i]['ReviewRating'],self.employee_info[i].review_rating)

if __name__ == "__main__":
    unittest.main ()
