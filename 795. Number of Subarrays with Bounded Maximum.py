795. Number of Subarrays with Bounded Maximum

We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

Example :
Input: 
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].


class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        
        # 本题的意思是找一个连续子数组，其中最大值在LR之间
        dp=[0]*len(A)# 表示包括这个点的所有符合条件的子串的个数
        start=0
        for i in range(len(A)):
            if L<=A[i]<=R:
                dp[i]=i-start+1# 从这个点往左数，包括这个点
            elif A[i]<L:
                dp[i]=dp[i-1]# 表示dp【i-1】代表的所有子串加一个A【i】
            else:
                start=i+1#如果A【i】>R，就得重新开始
        
        return sum(dp)
