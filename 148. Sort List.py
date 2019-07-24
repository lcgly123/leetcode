148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        def merge(p1,p2):
            dummy=ListNode(0)
            head=dummy
            
            while(p1 and p2):
                if p1.val<p2.val:
                    head.next=p1
                    p1=p1.next
                else:
                    head.next=p2
                    p2=p2.next
                head=head.next
            head.next=p1 or p2
            return dummy.next
        def find_mid(p):
            fast,slow=p,p
            while(fast and fast.next and fast.next.next):
                fast=fast.next.next
                slow=slow.next
            return slow
        
        def sort_(head):
            if head==None or head.next==None:
                return head
            
            mid=find_mid(head)
            right_node=mid.next
            mid.next=None
            left=sort_(head)
            right=sort_(right_node)
            return merge(left,right)
        
        return sort_(head)
        
        
        
        
        
