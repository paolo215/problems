# Unit test for Array
import unittest
from Array.sumPairs import sumPairs


class ArrayTest(unittest.testCase):
    def test_sumPairs1(self):
        arr = [8, 7, 2, 5, 3, 1]
        total = 10
        pairs = sumPairs(arr, total)

        
        print(pairs)


if __name__ == "__main__":
    unittest.main()

