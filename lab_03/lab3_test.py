import unittest 
import io 
from unittest.mock import patch 
from Utils import FileManager
from Student import Student
from StudentList import StudentList
class TestStudentList(unittest. TestCase):
    def setUp(self):
        self.student_list = StudentList()
        self.student_list.students=[Student("John", "1234567890", "Male", "USA")]
    def test_addNewElement(self):
        with patch('builtins.input', side_effect=["Ihor", "1234567890", "Male", "USA"]):
            self.student_list.addNewElement()
            self.assertEqual(len(self.student_list.students), 2)
    def test_updateElement(self):
        with patch('builtins.input', side_effect=["John", "Bob", "5555555555", "Male", "Canada"]):
            self.student_list.updateElement()
            self.assertEqual(self.student_list.students[0].name, "Bob")
    def test_deleteElement(self):
        with patch('builtins.input', return_value="Bob"):
            self.student_list.deleteElement()
            self.assertEqual(len(self.student_list.students), 1)


if __name__ == 'main': unittest.main()

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.filemanager= FileManager()
        self.student_list = StudentList()
        self.test_file = "test.csv"
        self.test_data = [Student("Ann", "098765432", "Female", "USA"),
                          Student("John", "1234567890", "Male", "USA")]


    def test_get_data(self):

        self.filemanager.get_data(self.test_file,self.student_list)
        self.assertEqual(self.student_list.students[0].name, self.test_data[0].name)
        self.assertEqual(self.student_list.students[1].phone, self.test_data[1].phone)

    def test_save_data(self):
        self.filemanager.get_data(self.test_file,self.student_list)
        self.filemanager.save_data(self.test_file,self.student_list)
        self.filemanager.get_data(self.test_file,self.student_list)
        self.assertEqual(self.student_list.students[0].name, self.test_data[0].name)
        self.assertEqual(self.student_list.students[1].phone, self.test_data[1].phone)
if __name__ == 'main': unittest.main()