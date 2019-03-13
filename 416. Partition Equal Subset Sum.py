416. Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
#         # 会超时
#         # 其实只有搜到一组数，和为sum(nums)//2就行
#         def dfs(nums,target):
#             if target==0:
#                 return True
#             if len(nums)==0:
#                 return False
            
#             for i in range(len(nums)):
#                 nums_in=nums[:]
#                 nums_in.pop(i)
#                 res=dfs(nums_in,target-nums[i])
#                 if res:
#                     return True
#             return False
            
#         if sum(nums)%2==1:
#             return False
#         target=sum(nums)//2
#         res=dfs(nums,sum(nums)//2)
#         return res
            
            
        
        # 就是把搜索问题变为可达问题
        if sum(nums)%2==1:
            return False
        target=sum(nums)//2
        
        dp=[0]*(target+1)# 该点是否可达
        dp[0]=1
        
        nums.sort()
        for n in nums:
            dp_d=dp[:]# 一个用于判断本点是否可达，一个用于改变后面的点
            for i in range(len(dp)):
                if dp[i]==1 and n+i<len(dp):
                    dp_d[n+i]=1
                    if dp_d[-1]==1:
                        return True
            dp=dp_d[:]
        return dp[-1]==1
        
        
