import unittest
from karatsuba import karatsuba


class TestKaratsuba(unittest.TestCase):
    def test_small_numbers(self):
        for i in range(10):
            for j in range(10):
                self.assertEqual(karatsuba(i, j), i * j)

    def test_large_numbers(self):
        self.assertEqual(karatsuba(123456789, 987654321), 121932631112635269)
        self.assertEqual(karatsuba(1234567890, 9876543210), 12193263111263526900)


if __name__ == '__main__':
    unittest.main()
