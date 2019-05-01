799. Champagne Tower

We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup (250ml) of champagne.
Example 1:
Input: poured = 1, query_glass = 1, query_row = 1
Output: 0.0
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

Example 2:
Input: poured = 2, query_glass = 1, query_row = 1
Output: 0.5
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)).
There is one cup of excess liquid. 
The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally,
and each will get half cup of champange.


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        # NB
        n=100
        dp=[[0 for _ in range(n)] for _ in range(n)]
        dp[0][0]=poured
        
        for i in range(query_row):# 只到查询行的上面一行
            for j in range(i+1):#注意
                if dp[i][j]>1:
                    dp[i+1][j]+=(dp[i][j]-1)/2
                    dp[i+1][j+1]+=(dp[i][j]-1)/2# 注意
                    
        return min(dp[query_row][query_glass],1)
