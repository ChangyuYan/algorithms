class SudokuSolver:
    def solveSudoku(self, board):
        '''
        Do not return anything, modify board in-place
        Board is a 9 * 9 matrix
        '''
        self.rows = [[0 for y in range(10)] for x in range(9)]
        self.cols = [[0 for y in range(10)] for x in range(9)]
        self.boxs = [[0 for y in range(10)] for x in range(9)]
        self.board = board
        
        # intialize constrains before filling
        for i in range(9):
            for j in range(9):
                c = self.board[i][j]
                if c != ".":
                    n = int(c)
                    bx = int(j / 3)
                    by = int(i / 3)
                    self.rows[i][n] = 1
                    self.cols[j][n] = 1
                    self.boxs[by * 3 + bx][n] = 1
        
        self.fill(0, 0)

    def fill(self, x, y):
        if y == 9:
            return True

        nx = (x + 1) % 9
        ny = y + 1 if nx == 0 else y

        if self.board[y][x] != '.':
            return self.fill(nx, ny)

        for i in range(1, 10):
            bx = int(x / 3)
            by = int(y / 3)
            box_key = by * 3 + bx

            if not self.rows[y][i] and not self.cols[x][i] and not self.boxs[box_key][i]:
                self.rows[y][i] = 1
                self.cols[x][i] = 1
                self.boxs[box_key][i] = 1
                self.board[y][x] = str(i)
                if self.fill(nx, ny):
                    return True
                self.board[y][x] = "."
                self.boxs[box_key][i] = 0
                self.cols[x][i] = 0
                self.rows[y][i] = 0
                
        return False

# Test
board = [["5","3",".",".","7",".",".",".","."], 
         ["6",".",".","1","9","5",".",".","."], 
         [".","9","8",".",".",".",".","6","."], 
         ["8",".",".",".","6",".",".",".","3"], 
         ["4",".",".","8",".","3",".",".","1"], 
         ["7",".",".",".","2",".",".",".","6"], 
         [".","6",".",".",".",".","2","8","."], 
         [".",".",".","4","1","9",".",".","5"], 
         [".",".",".",".","8",".",".","7","9"]]

solver = SudokuSolver()
solver.solveSudoku(board)
print(board)
'''
And the result becomes:
[['5', '3', '4', '6', '7', '8', '9', '1', '2'],
 ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
 ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
 ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
 ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
 ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
 ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
 ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
 ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
'''
