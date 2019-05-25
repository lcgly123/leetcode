79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(x,y,target):
            if board[x][y]!=target[0]:
                return False
            if len(target[1:])==0:
                return True
            for dx,dy in [[0,-1],[-1,0],[1,0],[0,1]]:
                if 0<=x+dx<len(board) and 0<=y+dy<len(board[0]):
                        board[x][y]='#'
                        res=dfs(x+dx,y+dy,target[1:])
                        if res:
                            return True
                        board[x][y]=target[0]
         
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                    if dfs(i,j,word[:]):
                        return True
        return False
                    

        
        
        
        
#         import copy

        
#         def change_candidates(board,candidates,x,y):
#             if x-1>=0 and board[x-1][y]!='.':
#                 candidates.append([x-1,y])
#             if x+1<=len(board)-1:
#                 candidates.append([x+1,y])
#             if y-1>=0:
#                 candidates.append([x,y-1])
#             if y+1<=len(board[0])-1:
#                 candidates.append([x,y+1])
#             return candidates
        
#         def dfs(board,candidates,target,index,path):
#             res=False
#             if path==target:
#                 return True
#             if len(candidates)==0:
#                 return False
#             for ind,p in enumerate(candidates):
#                 if board[p[0]][p[1]]==target[index]:
#                     candidates_in=[]
#                     candidates_in=change_candidates(board,candidates_in,p[0],p[1])
#                     temp=board[p[0]][p[1]]
                    
#                     board_in=copy.deepcopy(board)# 注意浅拷贝和深拷贝的区别，切片是浅拷贝
#                     board_in[p[0]][p[1]]='.'
#                     res=dfs(board_in,candidates_in,target,index+1,path+temp)
#                     if res==True:# 这一步减少了减少量，一旦找到，后面的候选项就不找了
#                         return True
#             return res# 和最上面的res配合，使之一定有一个输出
        
#         candidates=[]
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j]==word[0]:
#                     candidates.append([i,j])
                    
                    
#         res=dfs(board,candidates,word,0,'')
#         return res
