# test_employee
# Created by JKChang
# 10/01/2018, 14:03
# Tag:
# Description: test employee

import unittest
from unittest.mock import patch

from DSH.Employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee(first='David', last='Ch', pay=50000)
        self.emp_2 = Employee('Amy', 'Wang', 20000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'David.Ch@email.com')
        self.assertEqual(self.emp_2.email, 'Amy.Wang@email.com')

        self.emp_1.first = 'Mike'
        self.emp_2.last = 'Xue'
        self.assertEqual(self.emp_1.email, 'Mike.Ch@email.com')
        self.assertEqual(self.emp_2.email, 'Amy.Xue@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'David Ch')
        self.assertEqual(self.emp_2.fullname, 'Amy Wang')

        self.emp_1.first = 'Mike'
        self.emp_2.last = 'Xue'
        self.assertEqual(self.emp_1.fullname, 'Mike Ch')
        self.assertEqual(self.emp_2.fullname, 'Amy Xue')

    def test_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 21000)

    def test_monthly_schedule(self):
        with patch('Employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Ch/May')
            self.assertEqual(schedule, 'Success')

            # ---
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Wang/June')
            self.assertEqual(schedule, 'Bad response')

if __name__ == '__main__':
    unittest.main()
