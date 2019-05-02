801. Minimum Swaps To Make Sequences Increasing

We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation: 
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        
        # It is guaranteed that the given input always makes it possible.所以只需要考虑下面两种情况
        no_swap=[0]*len(A)
        swap=[1]+[0]*(len(A)-1)# 表示决定每一步交换或者不交换，在这步使得数组都有序的最少交换次数，边界是根据递推试出来的
        
        for i in range(1,len(A)):
            mid_swap,mid_noswap=[],[]
            if A[i-1]<A[i] and B[i-1]<B[i]:
                mid_swap.append(swap[i-1]+1)
                mid_noswap.append(no_swap[i-1])
            if A[i-1]<B[i] and B[i-1]<A[i]:
                mid_swap.append(no_swap[i-1]+1)
                mid_noswap.append(swap[i-1])
            
            swap[i]=min(mid_swap)
            no_swap[i]=min(mid_noswap)
            
        return min(swap[-1],no_swap[-1])
        
        
