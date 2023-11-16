import unittest
import io
from unittest.mock import patch
from lab2 import get_data, save_data, addNewElement, deleteElement, updateElement, printAllList

class TestLab2Script(unittest.TestCase):
    def setUp(self):
        self.test_file = "test.csv"
        self.test_data = [
            {"name": "Alice", "phone": "734586290", "gender": "woman", "country": "Ukraine"},
            {"name": "John", "phone": "9675643454", "gender": "man", "country": "USA"},
        ]


    def test_get_data(self):

        data = get_data(self.test_file)
        self.assertEqual(data, self.test_data)

    def test_save_data(self):
        save_data(self.test_file, self.test_data)
        loaded_data = get_data(self.test_file)
        self.assertEqual(loaded_data, self.test_data)

    def test_addNewElement(self):
        with patch('builtins.input', side_effect=["Ihor", "1234567890", "man", "USA"]):
            addNewElement(self.test_data)
            self.assertEqual(len(self.test_data), 3)

    def test_deleteElement(self):
        with patch('builtins.input', return_value="Ihor"):
            deleteElement(self.test_data)
            self.assertEqual(len(self.test_data), 2)

    def test_updateElement(self):
        with patch('builtins.input', side_effect=["John", "Bob", "5555555555", "man", "Canada"]):
            updateElement(self.test_data)
            self.assertEqual(self.test_data[1]["name"], "Bob")

    def test_printAllList(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            printAllList(self.test_data)
            output = mock_stdout.getvalue()
            self.assertIn("J", output)
            self.assertIn("Alice", output)

if __name__ == '__main__':
    unittest.main()