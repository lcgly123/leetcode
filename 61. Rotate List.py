61. Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return head
        
        p=head
        num_node=1
        while(p.next):
            num_node+=1
            p=p.next
        p.next=head
        for _ in range(num_node-k%num_node):# 正向移动就直接k，反向移动就这样算（更好，因为k可能大于一圈）
            head=head.next
            p=p.next
        p.next=None#断开循环
        return head
        

        
        
        
#         if head==None:
#             return head
#         p=head
        
#         num_node=1
#         while(p.next!=None):
#             p=p.next
#             num_node+=1
#         p.next=head
#         for i in range(num_node-k%num_node):# 漂亮
#             head=head.next
#             p=p.next
#         p.next=None
#         return head
