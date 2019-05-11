974. Subarray Sums Divisible by K

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        
        dic=collections.defaultdict(int)
        dic[0]=1
        
        num_sum=0
        res=0
        for n in A:
            num_sum=(num_sum+n)%K
            if num_sum in dic:# 说明中间有一段是K的整数倍
                res+=dic[num_sum]
            dic[num_sum]+=1
        
        return res
            
        

