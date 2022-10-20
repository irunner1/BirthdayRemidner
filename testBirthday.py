import unittest
import datetime
from BirthdayReminder import addToList, deleteFromList, showList, showNearestBirthday, showPersonBirthday, showTodayBirthday
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

    def test_deleteFromList_true(self):
        input = []
        input.append(BR("09/10/2010", "asd"))
        result = deleteFromList(input, "09/10/2010")
        self.assertEqual(result, 0)

    def test_deleteFromList_false(self):
        input = []
        input.append(BR("08/10/2010", "asd"))
        result = deleteFromList(input, "09/10/2010")
        self.assertEqual(result, 1)

    def test_showTodayBitrhday_true(self):
        input = []
        date = datetime.datetime.today().strftime("%d/%m/%Y")
        input.append(BR(date, "asd"))
        result = showTodayBirthday(input)
        self.assertEqual(result, "asd")

    def test_showTodayBitrhday_false(self):
        input = []
        input.append(BR("50/50/5000", "asd"))
        result = showTodayBirthday(input)
        self.assertEqual(result, "nah")
    
    def test_showPersonBirthday_true(self):
        input = []
        input.append(BR("09/10/2010", "asd"))
        result = showPersonBirthday(input, "asd")
        self.assertEqual(result, "asd 09/10/2010")

    def test_showPersonBirthday_false(self):
        input = []
        input.append(BR("09/10/2010", "asd"))
        result = showPersonBirthday(input, "bsd")
        self.assertEqual(result, "nah")
    
    def test_showNearestBirthday_true(self):
        input = []
        input.append(BR("08/10/2010", "asd"))
        input.append(BR("21/10/2010", "asd"))
        result = showNearestBirthday(input)
        self.assertEqual(result, 1) #до ближайшего дня рождения 1 день

    def test_showNearestBirthday_false(self):
        input = []
        input.append(BR("08/10/2010", "asd"))
        input.append(BR("09/10/2010", "asd"))
        result = showNearestBirthday(input)
        self.assertEqual(result, 366)

if __name__ == "__main__":
    unittest.main()
