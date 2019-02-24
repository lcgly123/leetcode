287. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 见过好多次了
        from collections import defaultdict
        
        dic=defaultdict(lambda :0)
        for i in nums:
            dic[i]+=1
            
        for k,v in dic.items():
            if v>1:
                return k
