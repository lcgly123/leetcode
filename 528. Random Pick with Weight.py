528. Random Pick with Weight

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]


class Solution:

    def __init__(self, w: List[int]):
        self.w=w
        for i in range(1,len(w)):
            self.w[i]+=self.w[i-1]# 变成类似累积函数，NB

    def pickIndex(self) -> int:
        import random
        val=random.randint(1,self.w[-1])
        return bisect.bisect_left(self.w,val)# 二分查找，看看应该插哪，返回插入后左边的index，有用
        
        
        
        
