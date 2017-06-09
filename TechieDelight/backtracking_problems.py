
class N_Queens(object):
    """
    Print all possible solutions to N Queens problem

    The N queens puzzle is the problem of placing N chess queens on an N x N
    chessboard so that no two queens threaten each other. Thus, a solution
    requires that no two queens share the same row, column, or diagonal
    """
    def __init__(self, n):
        self.n = n

        # Set up N x N board
        self.board = [['.' for i in range(self.n)] for ii in range(self.n)]

        # Collect answers
        self.answers = []

    def solve(self, num_added_pieces):
        """
        Recursively solve the N x N Quuens problem
        """
        import copy
        for x in range(self.n):
            for y in range(self.n):
                if self.board[x][y] != '.':
                    continue

                # Generate all possible moves and see if it's threaten or not
                threaten, moves = self.moveGen((x,y))

                # Skip if threatened
                if threaten == True:
                    continue

                # Put it in the board
                self.board[x][y] = 'Q'

                # Recursive call
                self.solve(num_added_pieces+1)

                # See if we managed to put all the pieces in the board
                if num_added_pieces == self.n:
                    if not self.board in self.answers:
                        # We found an answer
                        self.answers.append(copy.deepcopy(self.board))

                # Undo move
                self.board[x][y] = '.'

        return num_added_pieces 

    def moveGen(self, coord):
        """
        Generate all possible moves of the Queen piece in the position
        """
        threaten1, moves1 = self.rotate(coord, 0, 1)  # Moves for column and row
        threaten2, moves2 = self.rotate(coord, 1, 1)  # Mvoes for diagnoal

        # See if threatened
        if any([threaten1, threaten2]):
            return True, [moves1 + moves2]

        return False, [moves1 + moves2]


    def rotate(self, coord, deltaX, deltaY):
        """
        Symmetrical rotation and linear move scan
        """
        moves = []
        dx = int(deltaX)
        dy = int(deltaY)

        for i in range(4):
            data = self.scan(coord, dx, dy)
            threaten, moveList = data
            moves += moveList
            if threaten == True:
                return True, moves
            dx, dy = dy, -dx

        return False, moves

    def scan(self, coord, deltaX, deltaY):
        """
        Linear scan
        """
        x, y = coord
        moves = []
        while True:
            x += deltaX
            y += deltaY
            if not(x >= 0 and x < self.n) or not(y >= 0 and y < self.n):
                break
            if self.board[x][y] == 'Q':
                return True, moves
            moves.append([x, y])

        return False, moves
                

