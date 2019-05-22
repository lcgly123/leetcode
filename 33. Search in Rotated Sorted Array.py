33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 注意，本题的顺序是从小到大
        # 算法：看看左边是否包含转折，如果包含再看看是否包含target
        # 同理看看右边
        # 如果都没有，就是正常的二分查找
        
        # 二分查找可以处理从任意多元素，包括0元素
     
  
        l,r=0,len(nums)-1
        while(l<=r):
            mid=(l+r)//2
            print(nums[l],nums[mid],nums[r])
            if nums[mid]==target:
                return mid
            if nums[l]>nums[mid]:# 因为本题的初始排列一定是从小到大的，所以包含转折等价于nums[l]>nums[mid]
                if (target>=nums[l] or target<nums[mid]):# 不会等于nums[mid],但有可能等于nums[l]
                    r=mid-1
                elif nums[l]>nums[mid]:
                    l=mid+1
            elif nums[mid]>nums[r]:
                if (target>nums[mid] or target<=nums[r]):# 不会等于nums[mid],但有可能等于nums[r]
                    l=mid+1
                elif nums[mid]>nums[r]:
                    r=mid-1
            else:
                if target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
        
        return  -1
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not nums or len(nums) == 0:
#             return -1
            
#         l,r = 0,len(nums)-1

#         while(l < r-1):# 确保能从循环里出来
#             mid = (l+r)//2
#             if nums[mid] < nums[r]:# 正序
#                 if nums[mid]<target and nums[r]>=target:# 单调区间
#                     l=mid
#                 elif nums[mid]==target:
#                     return mid
#                 else:
#                     r=mid
#             else:# 倒序
#                 if nums[mid]>target and nums[l]<=target:# 单调区间
#                     r=mid
#                 elif nums[mid]==target:
#                     return mid
#                 else:
#                     l=mid 
            
#         # 因为从while出来会剩下两个
#         if nums[l] == target:
#             return l
#         elif nums[r] == target:
#             return r
#         return -1
        
        
