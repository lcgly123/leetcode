650. 2 Keys Keyboard

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
 

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.


class Solution:
    def minSteps(self, n: int) -> int:
        
        
        dp=[0]*(n+1)# 如果没有是某个数的整数倍，就是1的多少倍-1，刚好是index(都会是1的倍数，所以只要dp【1】对就行其他无所谓)
        dp[0]=dp[1]=0
        
        for i in range(2,n+1):
            for j in range(i-1,0,-1):
                if i%j==0:
                    dp[i]=dp[j]+1+i//j-1#先复制一次，之后粘贴k-1次
                    break
        return dp[-1]

        
#         dp=[i for i in range(n+1)]
#         dp[0]=dp[1]=0 # 特别的
        
#         # for i in range(n+1):
#         #     for j in range(i-1,0,-1):
#         #         if i%j==0:
#         #             dp[i]=min(dp[i],dp[j]+1+i//j-1)
                    
#         # 稍好一点吧
#         for i in range(n+1):
#             for j in range(i-1,0,-1):
#                 if i%j==0:
#                     dp[i]=dp[j]+1+i//j-1
#                     break
                    
#         return dp[n]
                
