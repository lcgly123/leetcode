865. Smallest Subtree with all the Deepest Nodes

Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

 

Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:



We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        # 求具有最高高度的非叶子节点。 
        # 就是一层层向上传，层数多的向上传，相同的话就把自己传上去
        def dfs(root):
            if root==None:
                return 0,None
            l,r=dfs(root.left),dfs(root.right)
            
            if l[0]>r[0]:
                return l[0]+1,l[1]
            elif l[0]<r[0]:
                return r[0]+1,r[1]
            else:
                return l[0]+1,root
            
        return dfs(root)[1]
        
        
        
        
        
        
        
