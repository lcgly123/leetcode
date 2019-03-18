456. 132 Pattern

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 流程就是先把他们都存进来，当碰到一个大的时候，把比它小的都放到另一个栈了（先进去的最小，外面的最大）
        # 这时第一个栈里最外面的可以和第二个栈里的所有元素构成3,2组合，只要下一个数比第二个栈了最外面的元素小
        # 就构成1,3,2了
        # 接下来能进第一个栈的数一定比第二个栈的数都大，（不然构成1,3,2就返回True了）
        # 这么依次下去，感觉是不错的，但不知道为什么一定行，不是太懂
        max_stack=[]
        min_stack=[]
        nums=nums[::-1]
        for n in nums:
            if max_stack==[]:
                max_stack.append(n)
            else:
                if min_stack!=[]:
                    if n<min_stack[-1]:
                        return True
                while(max_stack!=[] and n>max_stack[-1]):
                    min_stack.append(max_stack.pop())
                max_stack.append(n)
        
        return False
                
        
        
