209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.


class Solution:
    # 答案有错，我的答案是对应本题的
    def minSubArrayLen(self, s: 'int', nums: 'List[int]') -> 'int':
        if nums==[]:
            return 0
        if nums[0]==s:
            return 1
        elif nums[0]>s:
            mid=[[]]
        else:
            mid=[[nums[0]]]
            
        
        res=[]
        for i in range(1,len(nums)):
            new_mid=[[nums[i]]+x for x in mid]+[[nums[i]]]
            print(new_mid)
            for i in range(len(new_mid)-1,-1,-1):
                if sum(new_mid[i])==s:
                    res.append(new_mid.pop(i))
                elif sum(new_mid[i])>s:
                    new_mid.pop(i)
            mid=new_mid
        
        print(res)
        
        if len(res)==0:
            return 0
        min_=len(nums)
        for i in res:
            min_=min(len(i),min_)
        
        return min_
