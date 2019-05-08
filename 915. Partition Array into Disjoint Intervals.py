915. Partition Array into Disjoint Intervals

Given an array A, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

Example 1:

Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        
        
        # 其实不难
        rmin=[None]*len(A)
        min_from_right=float('inf')
        
        for i in range(len(A)-1,-1,-1):
            min_from_right=min(min_from_right,A[i])
            rmin[i]=min_from_right# 记录每个位置从右看过去的最小值
        
        max_from_left=float('-inf')
        for i in range(len(A)-1):
            max_from_left=max(max_from_left,A[i])# 记录每个位置从左看过去的最大值
            if max_from_left<=rmin[i+1]:
                return i+1
                
        

