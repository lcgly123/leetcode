328. Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
    
    # O(1)空间复杂度
        dummy1=odd=ListNode(0)
        dummy2=even=ListNode(0)
        
        while(head):
            odd.next=head
            even.next=head.next
            
            odd=odd.next
            even=even.next
            
            if head.next:
                head=head.next.next
            else:
                head=head.next# 也就是None
        
        odd.next=dummy2.next
        return dummy1.next

                
        
        
        
