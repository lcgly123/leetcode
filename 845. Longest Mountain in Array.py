845. Longest Mountain in Array

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        
        # 其实很简单，就是两个while
        res=0
        for i in range(1,len(A)-1):
            if A[i-1]<A[i]>A[i+1]:
                l,r =i-1,i+1
                while l>=0:
                    if A[l]<A[l+1]:
                        l-=1
                    else:
                        break
              
                while r<len(A):
                    if A[r]<A[r-1]:
                        r+=1
                    else:
                        break
                
                res=max(res,r-l-1)
        
        return res
