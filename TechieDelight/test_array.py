# Unit test for Array
import unittest
import array_problems as ar

def sameArray(output, expected):
    output = map(list, output)
    expected = map(list, expected)
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


    def test_utility_sameArray5(self):
        a = [(3,5), (1,2)]
        b = [(1,2), (5,5)]
        self.assertTrue(not sameArray(a, b))


class ArrayTest(unittest.TestCase):


    def test_sumPairs1(self):
        input_array = [8, 7, 2, 5, 3, 1]
        total = 10
        pairs = ar.sumPairs(input_array, total)
        expectedPairs = [(8,2), (7,3)]
       
        self.assertTrue(sameArray(pairs, expectedPairs))
      

    def test_sumPairs2(self):
        input_array = [1, 2, 3, 4, 5]
        total = 10

        pairs = ar.sumPairs(input_array, total)
        expectedPairs = []

        self.assertTrue(sameArray(pairs, expectedPairs))


    def test_sumPairs3(self):
        input_array = [0]
        total = 10

        pairs = ar.sumPairs(input_array, total)
        expectedPairs = [(1,1)]

        self.assertTrue(not sameArray(pairs, expectedPairs))

    def test_zero_sub_array1(self):
        input_array = [4, 2, -3, -1, 0, 4]
        pairs = ar.zero_sub_array(input_array)
        expectedPairs = [(-3,-1,0,4), (0,)]
        self.assertTrue(sameArray(pairs, expectedPairs))
    
    def test_zero_sub_array2(self):
        input_array = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
        pairs = ar.zero_sub_array(input_array)
        expectedPairs = [(3,4,-7), (4,-7,3), (3,1,-4), (3,1,3,1,-4,-2,-2), \
                        (3,4,-7,3,1,3,1,-4,-2,-2), (-7,3,1,3)]
        self.assertTrue(sameArray(pairs, expectedPairs))


    def test_zero_sub_array3(self):
        input_array = [10, 10]
        pairs = ar.zero_sub_array(input_array)
        expectedPairs = []
        self.assertTrue(pairs == expectedPairs)


    def test_binary_array_sort1(self):
        input_array = [1,0,1,0,1,0,0,1]
        output = ar.binary_array_sort(input_array)
        expectedOutput = [0,0,0,0,1,1,1,1]

        self.assertTrue(output == expectedOutput)


    def test_binary_array_sort2(self):
        input_array = [1, 0]
        output = ar.binary_array_sort(input_array)
        expectedOutput = [0, 1]

        self.assertTrue(output == expectedOutput)


    def test_binary_array_sort3(self):
        input_array = [1]
        output = ar.binary_array_sort(input_array)
        expectedOutput = [0]

        self.assertTrue(not (output == expectedOutput))


if __name__ == "__main__":
    unittest.main()

