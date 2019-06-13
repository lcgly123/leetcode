688. Knight Probability in Chessboard

On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

 

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

class Solution:
     #memo很有用
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def dfs(i,j,step,pro):
            if i<0 or i>=N or j<0 or j>=N:
                return 0
            if step==K:
                return pro
            if (i,j,step) in memo:
                return memo[(i,j,step)]
            
            direct=[(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
            res=0
            for dx,dy in direct:
                res+=dfs(i+dx,j+dy,step+1,pro/8)
            
            memo[(i,j,step)]=res
            return res
        
        memo={}
        return dfs(r,c,0,1)
       
       
       
       
       
    #memo很有用
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        #NB
        def dfs(i,j,step,p):
            if 0<=i<N and 0<=j<N and step<K:# 等于K就不能再往下搜了
                if (i,j,step) in memo:
                    return memo[(i,j,step)]
                sm=0
                move=[(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
                for mi,mj in move:
                    sm+=dfs(i+mi,j+mj,step+1,p/8)
                memo[(i,j,step)]=sm
                return sm
            else:
                return 0 <= i < N and 0 <= j < N and p # 如果这一点超界，
                                                        # 那这一点概率为0，如果没出界，
                                                        # 但step过了，应该返回p，其实多搜了一步 
        
        memo={}
        res=dfs(r,c,0,1)
        return res
                
        
        
        
