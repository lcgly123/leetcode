287. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 根据鸽笼原理，给定n + 1个范围[1, n]的整数，其中一定存在数字出现至少两次。

        # 假设枚举的数字为 n / 2：

        # 遍历数组，若数组中不大于n / 2的数字个数超过n / 2，则可以确定[1, n /2]范围内一定有解，

        # 否则可以确定解落在(n / 2, n]范围内。
        
        l,r=1,len(nums)# 因为题目给定的数字是1-n
        while(l<=r):
            mid=(l+r)//2 # 中间数
            add=sum([x<=mid for x in nums])
            
            if add>mid:
                r=mid-1
            else:
                l=mid+1
        
        return l# 得是l
        

        
        
#         # 见过好多次了
#         from collections import defaultdict
        
#         dic=defaultdict(lambda :0)
#         for i in nums:
#             dic[i]+=1
            
#         for k,v in dic.items():
#             if v>1:
#                 return k
        
        
        
        
        
        
        
        
        
        
