import copy

class NQueens:
    def totalNQueens(self, n):
        '''
        There are n queens totally, and board is n * n
        Returns all possible board results with n queens such that
        no queens are attacking each other on the same board
        '''
        self.res = []
        self.board = [['.' for i in range(n)] for j in range(n)]
        self.cols = [False] * n
        self.diag1 = [False] * (2 * n - 1)
        self.diag2 = [False] * (2 * n - 1)
        
        self.nqueens(n, 0)
        print("Number of Solutions = ", str(len(self.res)))
        if len(self.res) > 0:
            print("One possible solution: ")
            for line in self.res[0]:
                print(line)
        return self.res
        
    def available(self, x, y, n):
        return (not self.cols[x]) \
           and (not self.diag1[x + y]) \
           and (not self.diag2[x - y + n - 1])

    def updateBoard(self, x, y, n, is_put):
        self.cols[x] = is_put
        self.diag1[x + y] = is_put
        self.diag2[x - y + n - 1] = is_put
        self.board[y][x] = 'Q' if is_put else '.'
    
    def nqueens(self, n, y):
        '''Try to put the queen on y-th row'''
        if y == n:
            # found the solution, add to the res set
            self.res.append(copy.deepcopy(self.board))
            return 
        
        # Try every column
        for x in range(n):
            if not self.available(x, y, n):
                continue
            self.updateBoard(x, y, n, True)
            self.nqueens(n, y + 1)
            self.updateBoard(x, y, n, False)


solver = NQueens()
solver.totalNQueens(8)
