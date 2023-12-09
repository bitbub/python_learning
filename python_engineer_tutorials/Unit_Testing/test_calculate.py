import unittest
import calculate


class TestCalculate(unittest.TestCase):

    def test_add(self):
        self.assertEqual( calculate.add(5, 20), 25 )
        self.assertEqual( calculate.add(5, -5), 0 )
        self.assertEqual( calculate.add(5, -20), -15 )

    def test_subtract(self):
        self.assertEqual( calculate.substract(5, 20), -15 )
        self.assertEqual( calculate.substract(5, -5), 10 )
        self.assertEqual( calculate.substract(5, -20), 25 )

    def test_multiply(self):
        self.assertEqual( calculate.multiply(5, 20), 100 )
        self.assertEqual( calculate.multiply(5, -5), -25 )
        self.assertEqual( calculate.multiply(5, 0), 0 )

    def test_divide(self):
        self.assertEqual( calculate.divide(15, 3), 5 )
        self.assertEqual( calculate.divide(5, -5), -1 )
        self.assertEqual( calculate.divide(5, 5), 1 )
        with self.assertRaises(ValueError): ## check divide by zero !!
            calculate.divide(5,0)


if __name__ == '__main__':
    unittest.main()