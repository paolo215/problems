import unittest
import backtracking_problems as bt

class BackTrackingTest(unittest.TestCase):
    def test_N_Queens(self):
        n_queens = [bt.N_Queens(f) for f in range(1, 5+1)]
        [n_queen.solve(1) for n_queen in n_queens]
        expected = [1,0,0,2,10]
        answers = [len(n_queen.answers) for n_queen in n_queens]

        self.assertTrue(answers == expected)

if __name__ == "__main__":
    unittest.main()

