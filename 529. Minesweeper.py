529. Minesweeper

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
 
 
 
 class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        
        def dfs(x,y,board):
            if board[x][y]!='E':# 走过了
                return
            
            directs=[(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
            count=0
            for dx,dy in directs:
                if 0<=x+dx<len(board) and 0<=y+dy<len(board[0]):
                    if board[x+dx][y+dy]=='M':
                        count+=1
            if count==0:
                board[x][y]='B'
            else:
                board[x][y]=str(count) 
                return # 如果周围没有雷就继续探索，如果有雷就不探索了，扫雷游戏就是这样
            for dx,dy in directs:
                if 0<=x+dx<len(board) and 0<=y+dy<len(board[0]):
                    dfs(x+dx,y+dy,board)
                        
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board
        dfs(click[0],click[1],board)
        return board
            
            
 
 
