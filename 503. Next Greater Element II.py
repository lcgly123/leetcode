503. Next Greater Element II

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.




class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack=[]
        res=[-1]*len(nums)# 没有的话就-1
        
        for i,num in enumerate(nums*2):# 要走两遍才能构成一个环，虽说会多一些
            while stack!=[] and nums[stack[-1]]<num:# 碰到一个大的num，栈外侧的很多就有了结果
                res[stack[-1]]=num
                stack.pop()
                
            if i<len(nums):# 要找结果的num的位置入栈，一定越来越小
                stack.append(i)
                
        return res
            
            
        
        
        
