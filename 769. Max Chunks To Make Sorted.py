769. Max Chunks To Make Sorted

Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.



class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        # 这道题意思是：把list分开，分别排序后就是真的顺序，要求子list数目最小
        # 其实和上一个题一样
        # 要想一个子列排序后和真的排序一样，则真的排序的这一部分应该都在这个子列中
        # 注意，所有数值都在[0, 1, ..., arr.length - 1]
        res=0
        max_n=-1
        for i,n in enumerate(arr):
            max_n=max(n,max_n)
            if i==max_n:
                res+=1
        
        return res
