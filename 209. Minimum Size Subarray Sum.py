209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        
        # 滑窗法，sum会超时
        # if sum(nums)<s:
        #     return 0
        # res=len(nums)
        # l=0
        # for r,n in enumerate(nums):
        #     if sum(nums[l:r+1])>=s:
        #         while(l<=r and sum(nums[l:r+1])>=s):
        #             res=min(res,r-l+1)
        #             l+=1
        # return res 
                
        # 加一个临时变量就快好多
#         if sum(nums)<s:
#             return 0
#         res=len(nums)
#         l=0
        
#         temp=0
#         for r,n in enumerate(nums):
#             temp+=n
#             if temp>=s:
#                 while(l<=r and temp>=s):
#                     res=min(res,r-l+1)
#                     temp-=nums[l]
#                     l+=1
#         return res 
