655. Print Binary Tree

Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
 
 
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        
        # NB
        def get_height(root):
            if root==None:
                return 0
            return 1+max(get_height(root.left),get_height(root.right))
        
        # NB
        def update_res(root,row,l,r):
            if root==None:
                return
            mid=(l+r)//2
            res[row][mid]=str(root.val)
            update_res(root.left,row+1,l,mid-1)
            update_res(root.right,row+1,mid+1,r)
            
        h=get_height(root)
        w=2**h-1#每一层都包括所有的节点
        res=[['']*w for _ in range(h)]
        update_res(root,0,0,w-1)
        
        return res
        
 
 
 
 
 
