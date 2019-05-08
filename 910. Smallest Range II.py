910. Smallest Range II

Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

 

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]





class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        
        # res至少是(A[-1]-K)-(A[0]+K)，很有可能比这个范围大

        A.sort()
        res=A[-1]-A[0]
        for i in range(len(A)-1):
            ma=max(A[-1]-K,A[i]+K)# 记住吧，不懂为啥，但感觉也对
            mn=min(A[0]+K,A[i+1]-K)
            res=min(res,ma-mn)
        return res
        
