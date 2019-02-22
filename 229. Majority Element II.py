229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        # defaultdict很有用
        dic=defaultdict(lambda :0)
        flag=len(nums)/3
        res=[]
        for i in range(len(nums)):
            dic[nums[i]]+=1
            if dic[nums[i]]>flag:
                res.append(nums[i])
                
        return list(set(res))

