764. Largest Plus Sign

In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000
Example 1:

Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:

    
        mines={(i, j) for i, j in mines}#变成字典
        # 其实是做了四个dp，NB
        dp=[[[0,0,0,0] for _ in range(N)] for _ in range(N) ]
        res=0
        
        for i in range(N):
            for j in range(N):
                if (i,j) not in mines:# 字典的in要比list的in快，有用
                    try:
                        dp[i][j][0]=dp[i][j-1][0]+1
                    except:
                        dp[i][j][0]=1
                    try:
                        dp[i][j][1]=dp[i-1][j][1]+1
                    except:
                        dp[i][j][1]=1
        for i in range(N-1,-1,-1):
            for j in range(N-1,-1,-1):
                if (i,j) not in mines:
                    try:
                        dp[i][j][2]=dp[i][j+1][2]+1
                    except:
                        dp[i][j][2]=1
                    try:
                        dp[i][j][3]=dp[i+1][j][3]+1
                    except:
                        dp[i][j][3]=1
                    
                    res=max(res,min(dp[i][j]))
                    
        return res
