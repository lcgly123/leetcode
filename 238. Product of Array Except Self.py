238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)

对于某一个数字，如果我们知道其前面所有数字的乘积，同时也知道后面所有的数乘积，那么二者相乘就是我们要的结果，所以我们只要分别创建出这两个数组即可，
分别从数组的两个方向遍历就可以分别创建出乘积累积数组。


class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        left=[1]*len(nums)
        right=[1]*len(nums)
        
        # 一个小DP
        left[0]=1# 只是为了接下来相乘
        for i in range(1,len(nums)):
            left[i]=left[i-1]*nums[i-1]
        
        right[0]=1
        for i in range(len(nums)-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
            
        res=[]
        for i in range(len(nums)):
            res.append(left[i]*right[i])
            
        return res
