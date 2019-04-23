667. Beautiful Arrangement II

Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement: 
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different p

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        
        res=[i for i in range(1,n-(k-1))]# 之后只要插入k-1个就行，
        start,end=n-(k-1),n
        flag=True
        
        # 只能说记住吧，插入k-1个数，具有k个不同间隔
        while(start<=end):# =因为进去是还没插入
            if flag:
                res.append(end)
                end-=1
            else:
                res.append(start)
                start+=1
            flag=not flag
        
        return res
        

