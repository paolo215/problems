# Unit test for Array
import unittest
from Array.sumPairs import sumPairs


class ArrayTest(unittest.TestCase):
    def test_sumPairs1(self):
        arr = [8, 7, 2, 5, 3, 1]
        total = 10
        pairs = sumPairs(arr, total)
        expectedPairs = [(8,2), (7,3)]

        isCorrect = True
        for pair in pairs:
            if not pair in expectedPairs:
                isCorrect = False

        self.assertTrue(isCorrect)
      


if __name__ == "__main__":
    unittest.main()

