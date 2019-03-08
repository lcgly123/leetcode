390. Elimination Game

There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6

class Solution:
    def lastRemaining(self, n: int) -> int:
        nums=range(1,n+1)# 真的是只要range就可以啊
        
        while(len(nums)>1):
            nums=nums[1::2][::-1]#NB,题目的意思应该是奇数开始一次，偶数开始一次，循环来
            
        return nums[-1]
        







