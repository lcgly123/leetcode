36. Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # 不重复就行
        def is_valid(unit):
            unit=[x for x in unit if x!='.']
            if len(set(unit))==len(unit):
                return True
            else:
                return False
        def is_row_valid(board):
            result=True
            for row in board:
                result =result and is_valid(row)
            return result
        def is_col_valid(board):
            result=True
            for col in zip(*board):
                result =result and is_valid(col)
            return result
        def is_box_valid(board,box_index_x,box_index_y):
            box= []
            for x in range(box_index_x*3,(box_index_x+1)*3):
                for y in range(box_index_y*3,(box_index_y+1)*3):
                    box.append(board[x][y])
            result = is_valid(box)
            return result
        
        
        fin_result=True
        if len(board)==0:
            return fin_result
        fin_result=fin_result and is_row_valid(board)
        fin_result=fin_result and is_row_valid(zip(*board))
            
        for x in [0,1,2]:
            for y in [0,1,2]:
                fin_result=fin_result and is_box_valid(board,x,y)
        return fin_result
        
        
        
