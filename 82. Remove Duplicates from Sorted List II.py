82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res=TreeNode(0)
        res.next=head
        pre=res
        
        while(head and head.next):# 防止head为None
            if head.val==head.next.val:
                while(head.next and head.val==head.next.val):# 这一段用来删除重复的
                    head=head.next
                head=head.next# 这是都删了，要留一个的话就不要这句
                pre.next=head
            else:
                head=head.next# 这就是直接往后退
                pre=pre.next
        return res.next
        
        
        
