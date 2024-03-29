80. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.


class Solution:
    def removeDuplicates(self, nums):
        """
        import copy
        :type nums: List[int]
        :rtype: int
        """
        dic=collections.defaultdict(int)
        res=[]
        i=0
        while(i<len(nums)):# while会重新计算len，for不会
            if dic[nums[i]]==2:
                nums.pop(i)
            else:
                dic[nums[i]]+=1
                i+=1
        return len(nums)
        
        

        
        
        
        
