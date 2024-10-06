import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch

class TestStudent(unittest.TestCase):

    @classmethod
    def setUp(cls):
        print('setUpClass')

    
    def tearDownCloss(cls):
        print('tearDownClass')


    def setUp(self):
        print('SetUp')
        self.student = Student('John', 'Doe')


    def tearDown(self):
        print('tearDown')


    def test_full_name(self):
        print('test_full_name')
        student = Student('John', 'Doe')

        self.assertEqual(student.full_name, 'John Doe')


    def test_email(self):
        print('test_email')
        student = Student('John', 'Doe')

        self.assertEqual(student.email, 'johndoe@email.com')


    def test_alert_santa(self):
        print('test_alert_santa')
        student = Student('John', 'Doe')
        student.alert_santa()

        self.assertTrue(student.naughty_list) 


    def test_apply_extensions(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")


    def test_course_schedule_failled(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Somthing went wrong with the request!")


if __name__ == '__main__':
    unittest.main()
