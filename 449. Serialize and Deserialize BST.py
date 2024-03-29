449. Serialize and Deserialize BST

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str 
        """ 
        def dfs(root,res):
            if root==None:
                return
            if root.left==None and root.right==None:
                res.append(root.val)
                return 
            res.append(root.val)
            dfs(root.left,res)
            dfs(root.right,res)
            
        res=[]
        dfs(root,res)
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(data):
            if data==[]:
                return
            root=TreeNode(data[0])
            i=1
            while(i<len(data) and data[i]<data[0]):
                i+=1
            root.left=dfs(data[1:i])
            root.right=dfs(data[i:])
            return root
        return dfs(data)
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
