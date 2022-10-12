import unittest
from BirthdayReminder import addToList, showList
from BirthdayReminder import BR


class birthdayTest(unittest.TestCase):
    def test_addition_false(self):
        input = []
        result = addToList(input, "10/10/2020", "asd")
        self.assertNotEqual(result, "10/10/2010 asd")
    
    def test_addition_true(self):
        input = []
        result = addToList(input, "10/10/2010", "asd")
        self.assertEqual(result, "10/10/2010 asd")

    def test_show_list_true(self):
        input = []
        input.append(BR("09/10/2010", "asd"))
        result = showList(input)
        self.assertEqual(result, 1)

    def test_show_list_false(self):
        input = []
        input.append(BR("09/10/2010", "asd"))
        input.append(BR("10/10/2010", "qwe"))
        result = showList(input)
        self.assertNotEqual(result, 1) # len should be 2


if __name__ == "__main__":
    unittest.main()
