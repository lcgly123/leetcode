473. Matchsticks to Square

Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.


class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 实际上也是搜索，有点像排列组合
        def dfs(candidates,target,nums,pos):
            if pos==len(nums):
                if candidates[0]==candidates[1]==candidates[2]==candidates[3]==target:
                    return True  
                else:
                    return
            
            for i in range(len(candidates)):
                if candidates[i]+nums[pos]>target:#有用
                    continue
                candidates_in=candidates[:][:]
                candidates_in[i]=candidates[i]+nums[pos]
                res=dfs(candidates_in,target,nums,pos+1)
                if res:
                    return True
                
        if len(nums)<4:
            return False
        if sum(nums)%4!=0:#空集不能求和
            return False
        nums.sort(reverse=True)# 能够减少时间
        candidates=[0]*4
        target=sum(nums)/4
        res=dfs(candidates,target,nums,0)
        if res:
            return True
        else:
            return False
                
                
                
                

