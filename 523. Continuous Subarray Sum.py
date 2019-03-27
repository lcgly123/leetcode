523. Continuous Subarray Sum

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.





class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # 答案有误
        if len(nums)<2:
            return False
        
        # 如果有连续两个0，就都可以
        prezero=False
        for i,n in enumerate(nums):
            if n==0:
                if prezero==False:
                    prezero=True
                else:
                    return True
            else:
                prezero=False
        
        # 0,0都可以
        if k==0:
            return False
        
        
        
        dic ={}
        s=0
        for i,n in enumerate(nums):
            s+=n
            mod=s%k
            if i!=0 and (mod==0 or (mod in dic and dic[mod]<i-1)):# mod in dic就说明中间的加和为k的倍数，dic[mod]<i-1表示至少要两个
                return True
            dic[mod]=i
            
        return False
                
        







