289. Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        sur_i=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                sur_in=[[i+xy[0],j+xy[1]] for xy in sur_i if 0<=i+xy[0]<len(board) and 0<=j+xy[1]<len(board[0])]
                sur=[board[xy[0]][xy[1]]%2 for xy in sur_in]# %2可以得到之前的值，NB
                
                if sum(sur)<2:
                    if board[i][j]==1:
                        board[i][j]=3
                    else:
                        board[i][j]=0
                elif sum(sur)==2 or sum(sur)==3:
                    if board[i][j]==1:
                        board[i][j]=1
                elif sum(sur)>3:
                    if board[i][j]==1:
                        board[i][j]=3
                if sum(sur)==3 and board[i][j]==0:# 注意这个不是elif
                    board[i][j]=2
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==2:
                    board[i][j]=1
                if board[i][j]==3:
                    board[i][j]=0












