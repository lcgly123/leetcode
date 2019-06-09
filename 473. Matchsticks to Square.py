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
        def dfs(can,path,target):
            if path[0]==path[1]==path[2]==path[3]==target:
                return True
            if can==[]:
                return False
            
            for j in range(len(path)):
                if path[j]+can[0]>target:
                    continue
                path_in=path[:]
                path_in[j]+=can[0]
                if dfs(can[1:],path_in,target):
                    return True
            return False
        
        if len(nums)<4:
            return False
        if sum(nums)%4!=0:
            return False
        nums.sort(reverse=True)# 能够减少时间
        target=sum(nums)//4
        path=[0]*4
        return dfs(nums,path,target)
                
        
                

