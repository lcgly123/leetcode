347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        dic=defaultdict(lambda :0)
        for i in nums:
            dic[i]+=1
            
        res=sorted(dic.keys(),key=lambda x:dic[x],reverse=True)#太好用了
        
        return res[:k]
