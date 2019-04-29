740. Delete and Earn

Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:

Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        
        if nums==[]:
            return 0
        
        dic=collections.Counter(nums)
        keys=sorted(dic)
        
        
        # 好像见过这种解法,跟抢劫那个题类似，连续的不能抢
        pre_pre=0
        pre=keys[0]*dic[keys[0]]
        for i in range(1,len(keys)):
            if keys[i]-keys[i-1]==1:#再这个和前一个直接选择一个
                cur=max(pre,pre_pre+keys[i]*dic[keys[i]])# 更好懂
                pre_pre=pre
                pre=cur
            else:# 不用选择了，都要
                cur=pre+keys[i]*dic[keys[i]]
                pre_pre=pre
                pre=cur
        
        return pre
                
