# test_calc
# Created by JKChang
# 10/01/2018, 11:08
# Tag:
# Description: test calc

import unittest

from DSH import calc


class testClac(unittest.TestCase):

    # must start with test_
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-15, -5), -20)
        self.assertEqual(calc.add(0, 0), 0)

    def test_substract(self):
        self.assertEqual(calc.substract(10, 5), 5)
        self.assertEqual(calc.substract(-1, 1), -2)
        self.assertEqual(calc.substract(-15, -5), -10)
        self.assertEqual(calc.substract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-15, -5), 75)
        self.assertEqual(calc.multiply(0, 0), 0)

    def test_devide(self):
        self.assertEqual(calc.devide(10, 5), 2)
        self.assertEqual(calc.devide(-1, 1), -1)
        self.assertEqual(calc.devide(-15, -5), 3)

        # self.assertEqual(calc.devide(5, 0), 0)
        self.assertRaises(ValueError, calc.devide, 10, 0)

        with self.assertRaises(ValueError):
            calc.devide(10, 0)


if __name__ == '__main__':
    unittest.main()
