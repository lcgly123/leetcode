698. Partition to K Equal Sum Subsets

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        sums=[0]*k
        if sum(nums)%k!=0:
            return False
        target= sum(nums)//k
        nums.sort(reverse=True)# 就是为了加速
        
        def dfs(candi,i):
            if i==len(candi):
                if len(set(sums))==1:
                    return True
                else:
                    return False
            for j in range(len(sums)):
                sums[j]+=candi[i]
                if sums[j]<=target and dfs(candi,i+1):# 如果candi[i]安排到sums[j]成了，就直接返回true，不然要再试别的j
                    return True
                sums[j]-=candi[i]
                if sums[j]==0: # 如果有一共是大于target，就不用再搜了，False
                    break
            return False
        
        return dfs(nums,0)
        
        
        
        

