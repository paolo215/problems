# Unit test for Array
import unittest
from Array.sumPairs import sumPairs

def sameArray(output, expected):
    if len(output) != len(expected):
        return False

    isCorrect = True
    for arr in output:
        if not arr in expected:
            isCorrect = False

    return isCorrect


class UtilityTest(unittest.TestCase):
    def test_utility_sameArray1(self):
        a = [(1,2)]
        b = [(1,2)]
        self.assertTrue(sameArray(a, b))

    def test_utility_sameArray2(self):
        a = []
        b = [(1,2)]
        self.assertTrue(not sameArray(a, b))

    
    def test_utility_sameArray3(self):
        a = [(3,5), (1,2)]
        b = [(1,2), (3,5)]
        self.assertTrue(sameArray(a, b))


    def test_utility_sameArray4(self):
        a = [(3,5), (1,2)]
        b = [(1,2), (3,5), (5,5)]
        self.assertTrue(not sameArray(a, b))


    def test_utility_sameArray4(self):
        a = [(3,5), (1,2)]
        b = [(1,2), (5,5)]
        self.assertTrue(not sameArray(a, b))


class ArrayTest(unittest.TestCase):


    def test_sumPairs1(self):
        arr = [8, 7, 2, 5, 3, 1]
        total = 10
        pairs = sumPairs(arr, total)
        expectedPairs = [(8,2), (7,3)]
       
        self.assertTrue(sameArray(pairs, expectedPairs))
      

    def test_sumPairs2(self):
        arr = [1, 2, 3, 4, 5]
        total = 10

        pairs = sumPairs(arr, total)
        expectedPairs = []

        self.assertTrue(sameArray(pairs, expectedPairs))



if __name__ == "__main__":
    unittest.main()

