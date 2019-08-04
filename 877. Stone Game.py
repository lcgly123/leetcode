877. Stone Game

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 

Example 1:

Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        
        # dp代表【i】[j]先手比后手多的数
        # dp的初始状态是 i = j 即只有一个石子堆，由于亚历克斯先拿，则 dp[ i ][ j ] = piles[ i ]
        dp=[[0]*len(piles) for _ in range(len(piles))]
        for i in range(len(piles)):
            dp[i][i]=piles[i]
        
        for start in range(len(piles)-2,-1,-1):# 见微信讲解（五分钟学算法）
            for end in range(start+1,len(piles)):
                chooseleft=piles[start]-dp[start+1][end]
                chooseright=piles[end]-dp[start][end-1]
                dp[start][end]=max(chooseleft,chooseright)
                
        return True if dp[0][len(piles)-1]>0 else False
        
        
        
