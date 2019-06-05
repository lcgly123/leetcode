228. Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res=[]
        i=0
        while(i<len(nums)):
            next_n=nums[i]+1
            j=i+1
            while(j<=len(nums)):# 最后一个比较麻烦
                if j==len(nums):
                    if j!=i+1:
                        res.append('->'.join([str(nums[i]),str(nums[j-1])]))
                        break
                    else:
                        res.append(str(nums[i]))
                        break
                        
                elif nums[j]==next_n:
                    j+=1
                    next_n+=1
                else:
                    if j!=i+1:
                        res.append('->'.join([str(nums[i]),str(nums[j-1])]))
                        break
                    else:
                        res.append(str(nums[i]))
                        break
            i=j
        return res
                    
                
            
        
        
#         res=[]
#         i=0
#         while(i<len(nums)):
#             j=i+1
#             flag=nums[i]+1
#             if j<len(nums) and nums[j]==flag:
#                 while(nums[j]==flag):
#                     j+=1
#                     flag+=1
#                     if j==len(nums):
#                         break
#                 res.append('->'.join([str(nums[i]),str(nums[j-1])]))
#                 i=j
#             else:
#                 res.append(str(nums[i]))
#                 i+=1
            
#         return res
                
