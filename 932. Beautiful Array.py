932. Beautiful Array

For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

Given N, return any beautiful array A.  (It is guaranteed that one exists.)

 

Example 1:

Input: 4
Output: [2,1,4,3]
Example 2:

Input: 5
Output: [3,1,2,5,4]



class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        
        # 题意：给定一个排列，要求给出其满足对于任意一个数A[k]，使得i<k<j，2*A[k]!=A[i]+A[j].的一个排列
        # 一种构造方法，不懂为啥，记住吧
        res=[1]
        while(len(res)<N):
            res=[2*x-1 for x in res]+[2*x for x in res]
            
        return [x for x in res if x<=N]
