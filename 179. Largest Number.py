179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def mycmp(x,y):
            if x+y>y+x:
                return 1
            elif x==y:
                return 0
            else:
                return -1
        import functools
        nums=list(map(str,nums))
        nums.sort(key=functools.cmp_to_key(mycmp),reverse=True)
        return str(int(''.join(nums)))
