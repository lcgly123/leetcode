775. Global and Local Inversions

We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        # 题意如果全局逆序大于局部逆序，其实只要有一个真全局逆序就行，因为局部逆序也是全局逆序
        max_=-1
        for i in range(len(A)-2):
            max_=max(max_,A[i])
            if max_>A[i+2]:
                return False
        
        return True

