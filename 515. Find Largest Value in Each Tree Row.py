515. Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        if root==None:
            return []
        queen=[root]
        res=[]
        
        while(queen):
            new=[]
            temp=float('-inf')
            
            for node in queen:
                temp=max(temp,node.val)
                new+=[x for x in [node.left,node.right] if x!=None]
            
            res.append(temp)
            queen=new
        return res
        
        
        
