869. Reordered Power of 2

Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.

 

Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false



class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        
        # 给你一个数N（1 <= N <= 10^9），你可以对这个数中的每个数字进行重排组成另外一个数字，
        # 只要存在一个使得这个数是2的幂，则返回True；例如N=46,你可以重组为64，这样64就是2的幂了，则返回True，
        
        #2的指数背小于10^9的也就30个数，全部求出来放到set里面，然后求N的permutation判断在不在set了
        
        return sorted(str(N)) in [sorted(str(1<<i)) for i in range(30)]#NB
        
