from collections import defaultdict
class Solution:
    # create rows, columns and squares default dicts(initializes with
    # empty list when key not found. keep pushing each element to 
    # respective rows, cols and squares, if its already found , then
    # the sudoku is invalid)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(list)
        cols=defaultdict(list)
        squares=defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if(board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i//3, j//3)]):
                    return False
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                squares[(i//3,j//3)].append(board[i][j])
        return True
        