873. Length of Longest Fibonacci Subsequence

A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

 

Example 1:

Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].




class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        
        
        # 其实不难
        dic={n:0 for n in A}# 只是为了快速的in
        
        res=0
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                a,b,count=A[i],A[j],2
                while a+b in dic:
                    count+=1
                    a,b=b,a+b#好像能并行计算，NB,有用
                
                res=max(res,count)
                
        return 0 if res==2 else res
            
        


