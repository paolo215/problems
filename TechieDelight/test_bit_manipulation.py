import bit_manipulation_problems as bm
import unittest

class BitManipulationTest(unittest.TestCase):
    def test_isOdd(self):
        output = bm.isOdd(20)
        expected = 0
        self.assertTrue(output == expected) 

        output = bm.isOdd(21)
        expected = 1
        self.assertTrue(output == expected) 


if __name__ == "__main__":
    unittest.main()

