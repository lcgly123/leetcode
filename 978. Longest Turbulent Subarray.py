978. Longest Turbulent Subarray

A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.

 

Example 1:

Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:

Input: [4,8,12,16]
Output: 2

class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if A.count(A[0])==len(A):
            return 1
        if len(A)<=2:
            return len(A)
            
        # len（A）>3才用这个,滑窗法
        l=0
        res=1
        for r in range(2,len(A)):
            if (A[r-2]-A[r-1])*(A[r-1]-A[r])<0 :
                res=max(res,r-l+1)
            else:
                l=r-1
        return max(2,res)
        
            
