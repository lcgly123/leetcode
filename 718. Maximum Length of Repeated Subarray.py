718. Maximum Length of Repeated Subarray

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].



class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        
        
        
        # 有用
        dp=[[0]*(len(B)+1) for _ in range(len(A)+1)]
        
        res=0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]:
                    dp[i+1][j+1]=dp[i][j]+1# 这样ij记录的就是此处的最长相同子串，不相同的话不会改，还是0
                    res=max(res,dp[i+1][j+1])
         
        
        return res
        
        # 这个是最长公共子串（只要都有就行）
        # 而本题是子串相同子串，不仅都有还有相同
#         dp=[[0]*(len(B)+1) for _ in range(len(A)+1)]
        
#         for i in range(len(A)):
#             for j in range(len(B)):
#                 if A[i]==B[j]:
#                     dp[i+1][j+1]=dp[i][j]+1
#                 else:# 这样ij记录的就是此处的有多少次相同
#                     dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        
#         return dp[-1][-1]
        
