525. Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        count=0
        maxlen=0
        dic={0:-1}# 只有o这个水平特殊
        
        for i,n in enumerate(nums):
            count+=(1 if n==1 else -1)
            if count not in dic:
                dic[count]=i# 记录达到这一水平的index
            else:
                maxlen=max(maxlen,i-dic[count])# 因为不同水平的之间要比较，如果只是同一水平就直接i-dic[count]
                
        return maxlen
        
        
