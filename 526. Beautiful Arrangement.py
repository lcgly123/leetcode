526. Beautiful Arrangement

Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
 

Now given N, how many beautiful arrangements can you construct?

Example 1:

Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.


class Solution:
    def countArrangement(self, N: int) -> int:
        # 其实挺简单，就是题意不好理解，其实就是pos%n==0 or n%pos==0这一个条件
        def dfs(candidates,n,res):
            if candidates==[]:
                res[0]+=1
                return 
            
            for i,pos in enumerate(candidates):
                if pos%n==0 or n%pos==0:
                    can_in=candidates[:]
                    can_in.pop(i)
                    dfs(can_in,n+1,res)
                    
        res=[0]
        candidates=list(range(1,N+1))
        dfs(candidates,1,res)
        return res[-1]