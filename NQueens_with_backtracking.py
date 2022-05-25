
class NQueens:

    def __init__(self, n):
        self.n = n
        self.chess_table = [[0 for i in range(n)] for j in range(n)]

    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print( ' Q ', end = '')
                else:
                    print( ' - ', end = '')
            print('\n')
            
    def isPlaceSafe(self, row_index, col_index):
        # checks row 
        for i in range(self.n):
            if self.chess_table[row_index][i] == 1:
                return False 
        # check diagonial left top  - bottom right 
        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j-1
        # check diagonial top right - bottom left
        j = col_index
        for i in range(row_index, self.n):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j-1
        return True

    def solve(self, col_index):
        if col_index == self.n:
            return True 

        for row_index in range(self.n):
            if self.isPlaceSafe(row_index, col_index):
                self.chess_table[row_index][col_index] = 1
                if self.solve(col_index+1):
                    return True
                self.chess_table[row_index][col_index] = 0
        return False 

    def solveNQueens(self):
        if self.solve(0):
            self.print_queens()
        return print('There is no solution to this problem') 



# queens = NQueens(4)
# queens.print_queens()
# queens.solveNQueens()

new_list = [1,2,3,4,6]

for i in range(len(new_list), -1, -1):
    print(i)
