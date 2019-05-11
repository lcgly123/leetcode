967. Numbers With Same Consecutive Differences

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        # 下一个数字可能是加K或减K，简单的搜索
        def dfs(path,res):
            if len(path)==N:
                res.append(int(''.join(str(x) for x in path)))
                return
            
            next_num=path[-1]+K
            if next_num<10:
                dfs(path+[next_num],res)
            
            next_num=path[-1]-K
            if next_num>=0:
                dfs(path+[next_num],res)
        
        if N == 1:
            return list(range(10))
        
        if K == 0:
            return [ int(''.join(str(_) * N)) for _ in range(1, 10)]
        
        res=[]
        
        for i in range(1,10):
            dfs([i],res)
        
        return res
                
        
        
        
        
        
        
        
        
        
        
        
