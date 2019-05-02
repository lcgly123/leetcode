823. Binary Trees With Factors

Given an array of unique integers, each integer is strictly greater than 1.

We make a binary tree using these integers and each number may be used for any number of times.

Each non-leaf node's value should be equal to the product of the values of it's children.

How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

Example 1:

Input: A = [2, 4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: A = [2, 4, 5, 10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].


class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        
        A.sort()
        A_set=set(A)#其实用处不大
        
        import collections
        factor=collections.defaultdict(set)
        
        for i,n in enumerate(A):
            for test in A[:i]:
                if n%test==0 and n//test in A_set:
                    factor[n].add(test)
        
        # NB
        tree={}
        for i,n in enumerate(A):
            tree[n]=1# 代表以n为根节点的数有多少
            for f in factor[n]:
                tree[n]+=tree[f]*tree[n//f]
                
        return sum(tree.values()) % ((10 ** 9) + 7)
        
