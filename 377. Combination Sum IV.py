377. Combination Sum IV

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        dp=[0]*(target+1)
        dp[0]=1
        if nums==[]:
            return 0
        
        for i in range(target+1):
            for j in nums:
                if i-j>=0:
                    dp[i]+=dp[i-j]
                
        return dp[-1]
            
        
        
        # 会超时
#         nums=sorted(nums)
#         def dfs(candidates,target,path,res):
#             if sum(path)==target:
#                 if path not in res:
#                     res.append(path)
#                 return
#             if sum(path)>=target:
#                 return
            
#             for i in range(len(candidates)):
#                 path_in=path+[candidates[i]]
#                 if sum(path_in)>target:
#                     return
#                 else:
#                     dfs(candidates,target,path+[candidates[i]],res)
        
#         res=[]
#         dfs(nums,target,[],res)
#         return len(res)
                
        
