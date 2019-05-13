1004. Max Consecutive Ones III

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        l=0
        res=0
        count=0
        # 分类讨论
        for r in range(len(A)):
            if A[r]==0:
                count+=1
                if count<K:
                    res=max(res,r-l+1)# 防止一直小于K，没有值
                elif count==K:
                    res=max(res,r-l+1)
                elif count>K:# 这时候才移动l，来去掉一个0
                    while(A[l]!=0):
                        l+=1
                    count-=1
                    l+=1
            else:
                if count<K:
                    res=max(res,r-l+1)
                elif count==K:
                    res=max(res,r-l+1)
                    
 
        
        return res
                        
        
