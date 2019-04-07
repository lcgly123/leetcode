560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # 连续子串经常用累加的方法
        dic=collections.defaultdict(int)
        dic[0]=1
        
        res,num_sum=0,0
        for n in nums:
            num_sum+=n
            if num_sum-k in dic:# 如果sum-k在，就有连续子串为k
                res+=dic[num_sum-k]
            dic[num_sum]+=1# 有0的话会多次到达一个地点，有多少次，就有多少可能
            
        return res
        


