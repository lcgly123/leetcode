679. 24 Game

You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False



class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        
        
        #NB，有用
        def dfs(nums):
            if len(nums)==1 and abs(nums[0]-24)<.0001:# len(nums)==1 必须的
                return True
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i!=j: # 所有不相同组合
                        base=[nums[k] for k in range(len(nums)) if k!=i and k!=j]
                        if dfs(base+[nums[i]+nums[j]]):return True
                        if dfs(base+[nums[i]-nums[j]]):return True
                        if dfs(base+[nums[j]-nums[i]]):return True
                        if dfs(base+[nums[i]*nums[j]]):return True
                        if nums[i]!=0:
                            if dfs(base+[nums[j]/nums[i]]):
                                return True
                        if nums[j]!=0:
                            if dfs(base+[nums[i]/nums[j]]):
                                return True
            return False
        
        return dfs(nums)
        








