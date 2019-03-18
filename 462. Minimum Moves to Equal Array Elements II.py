462. Minimum Moves to Equal Array Elements II

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 题目意思就是每次只对一个数+1-1，最少多少次所有数都一样，使他们都变成中位数最少
        nums.sort()
        mid=nums[len(nums)//2]# 如果是奇数刚好就是中间的一个，如果是偶数，中位数应该是这一个和下一个之间任意数都行
        
        res=sum([abs(n-mid) for n in nums])
        return res
