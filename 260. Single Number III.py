260. Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        
        xor=0
        for n in nums:
            xor^=n # 俩数异或的结果
        mask=1
        while(xor&mask==0):# 找到俩数不同的最低位
            mask<<=1
        
        a,b=0,0
        # 用与mask与的结果（0或非0）就行分组，一对数一定被分到一组里，一组包括a，一组包括b
        for n in nums:
            if n&mask:# 有值，不一定是1
                a^=n
            else:
                b^=n
        return [a,b]
                
