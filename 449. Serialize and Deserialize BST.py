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
        #居然是自己想到的，NB
        def dfs(data,pre):# pre的意思是上一个比本节点大的值
            if data==[]:# 只是防止第一次就啥都没
                return 
            root=TreeNode(data[0])
            data.pop(0)
            if data!=[]:
                if data[0]<root.val:
                    root.left=dfs(data,root.val)
                    
            if data!=[]:# 上面的递归完可能就没了
                if data[0]>root.val:
                    if data[0]<pre:
                        root.right=dfs(data,pre)# 这里应为pre，上一个比本节点大的值
                   
            return root
        return dfs(data,float('inf'))# 有用
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
