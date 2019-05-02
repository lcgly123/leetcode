817. Linked List Components

We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:

Input: 
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        
        p=head
        G=set(G)
        pre=False
        
        # NB
        res=0
        while(p!=None):
            if p.val in G and pre==False:# 说明连在一起的只能算一个
                res+=1
            pre=p.val in G
            p=p.next
        
        return res
        
        
        
        


