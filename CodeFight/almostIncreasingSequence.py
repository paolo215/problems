import unittest


def almostIncreasingSequence(sequence):
    canBeSeq = False
    
    length = len(sequence)
    strikes = 0
    
    for i in range(length):
        copy = list(sequence)
        copy.pop(i)
        if isIncreasing(copy) == True:
            return True
        
        else:
            strikes += 1
                
    return strikes < 2
        
def isIncreasing(arr):
    length = len(arr)
    for i in range(1, length):
        a = arr[i-1]
        b = arr[i]
        if b - a <= 0:
            return False
            
    return True
            
    
class Test(unittest.TestCase):
    def test_almostIncreasingSeq(self):
        self.assertFalse(almostIncreasingSequence([1,3,2,1]))
        self.assertTrue(almostIncreasingSequence([1,3,2])) 

        self.assertFalse(almostIncreasingSequence([1,2,1,2])) 

if "__main__" == __name__:
    unittest.main()

