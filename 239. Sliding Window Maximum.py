239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
 
 
 class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if nums==[]:
            return []
        
        
        
        # 只能记录坐标，直接记录值会错
        stack=[]
        res=[]
        for i in range(len(nums)):
            if stack and stack[0]<i-k+1:
                stack.pop(0)
            
            while(stack and nums[stack[-1]]<nums[i]):
                stack.pop()
            stack.append(i)
            
            
            if i>=k-1:
                res.append(nums[stack[0]])
        
        return res
        
