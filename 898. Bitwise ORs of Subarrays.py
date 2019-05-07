898. Bitwise ORs of Subarrays

We have an array A of non-negative integers.

For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j), we take the bitwise OR of all the elements in B, obtaining a result A[i] | A[i+1] | ... | A[j].

Return the number of possible results.  (Results that occur more than once are only counted once in the final answer.)

 

Example 1:

Input: [0]
Output: 1
Explanation: 
There is only one possible result: 0.



class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        
        # 对于每个（连续的）子数组 B = [A[i], A[i+1], ..., A[j]] （ i <= j），
        # 我们对 B 中的每个元素进行按位或操作，获得结果 A[i] | A[i+1] | ... | A[j]。
        # 返回可能结果的数量。

        cur,res=set(),set()
        
        for i in A:
            cur={i|x for x in cur}|{i}# 连续的
            res|=cur
        
        return len(res)
        
        



