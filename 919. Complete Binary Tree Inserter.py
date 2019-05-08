919. Complete Binary Tree Inserter

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.
 

Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:
    # 有意思
    # 建立完全二叉树，只保存了叶子节点
    def __init__(self, root: TreeNode):
        self.root=root
        self.nodes=[]
        
        queen=[self.root]
        while(queen):
            new=[]
            for node in queen:
                if node.left==None or node.right==None:
                    self.nodes.append(node)
                if node.left!=None:
                    new.append(node.left)
                if node.right!=None:
                    new.append(node.right)
            queen=new
        
        
            
        
    # 插入时，只需要叶子节点，返回值不知道为啥这么设置，随便吧
    def insert(self, v: int) -> int:
        res=None
        if self.nodes[0].left==None:
            node=TreeNode(v)
            self.nodes[0].left=node
            self.nodes+=[node]
            res=self.nodes[0]
        else:
            node=TreeNode(v)
            self.nodes[0].right=node
            self.nodes+=[node]
            res=self.nodes.pop(0)
        return res.val
        
        

    def get_root(self) -> TreeNode:
        return self.root
        
