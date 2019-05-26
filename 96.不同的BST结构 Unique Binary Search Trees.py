95. Unique Binary Search Trees 

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

1,一共有多少种，卡特兰数（虽然不懂）
class Solution:
    def numTrees(self, n: 'int') -> 'int':
        import math
        #公式： (2n)!/((n+1)!*n!)  
        return math.factorial(2*n)//(math.factorial(n+1)*math.factorial(n))
        
2，求出所有结构
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: 'int') -> 'List[TreeNode]':
        # 当数组为 1，2，3，4，.. i，.. n时，基于以下原则的BST建树具有唯一性：
        # 以i为根节点的树，其左子树由[1, i-1]构成， 其右子树由[i+1, n]构成。 
        
        # BST，左边的小于右边的
        
        # 大致流程是从最右边开始，改变结构的话从左边开始，太精巧了
        def gene_tree(first,last):
            tree=[]
            for root in range(first,last+1):
                for left in gene_tree(first,root-1):# 这里返回的是first到root-1构成的所有情况的树，所以要循环
                    for right in gene_tree(root+1,last): 
                        node=TreeNode(root)
                        node.left=left
                        node.right=right
                        tree+=[node]
                        # print(tree)
            return tree if tree else [None]
        if n==0:
            return []
        else:
            res=gene_tree(1,n)
        return res

