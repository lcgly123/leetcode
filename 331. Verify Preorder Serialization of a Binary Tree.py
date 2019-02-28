331. Verify Preorder Serialization of a Binary Tree

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:

Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: "1,#"
Output: false


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        count=0
        # 就是数产生的none，然后碰见一个消除一个，中途为0就是错的，只能最后为0
        if preorder=='#':
            return True
        for i,node in enumerate(preorder.split(',')):
            if i==0:
                if node=='#':
                    count-=1
                if node!='#':
                    count+=2
            else:
                if node=='#':
                    count-=1
                else:
                    count+=1
            if count==0 and i!=len(preorder.split(','))-1:
                return False
   
        if count!=0:
            return False
        else:
            return True
