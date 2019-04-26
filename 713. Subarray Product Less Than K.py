713. Subarray Product Less Than K

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.



class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if len(nums)==0 or k<=1:
            return 0
        
        start,end,prod,res=0,0,1,0
        # 当list增加或者减少一个元素时，list的连续子串（注意是连续子串，不是所有子串）增加end-start个（end在外面），数学知识，记住就行
        while(end<len(nums)):
            prod*=nums[end]
            end+=1# 加到list外面
            while(prod>=k):
                prod/=nums[start]
                start+=1
            res+=end-start
        
        return res
                    
        
        
        


