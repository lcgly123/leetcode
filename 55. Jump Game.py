55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        
        
# #         # dfs可以，但要搜索的一多就会超时
# #         def dfs(choices,index,path,res):# choices,index产生candidates
# #             if index>=len(choices):
# #                 return
# #             if index==len(choices)-1:# 也可以用index
# #                 res.append(True)
# #                 return
# #             for i in range(1,choices[index]+1):
# #                     dfs(choices,index+i,path+[index],res)
                    
# #         res=[False]
# #         dfs(nums,0,[],res)
        
# #         result=False
# #         for i in res:
# #             result=result or i
# #         return result

        max_=0
        for i in range(len(nums)):
            if i>max_:# 说明这个点已经不可达到
                return False
            max_=max(i+nums[i],max_)
      
        return True
