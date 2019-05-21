19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count=0
        p=head
        while(p):
            count+=1
            p=p.next
        
        use_c=count-n
        
        # 其实不难
        if use_c==0:
            return head.next
        p=head
        while(p):
            # print(use_c,p.val)
            use_c-=1
            if use_c!=0:
                p=p.next
                continue
            else:
                p.next=p.next.next
                return head
        
        
        
        
        
        
        
        
        
        
        
        
        
#         ptemp=ListNode(0)
#         ptemp=head
#         count=0
#         while(ptemp!=None):
#             ptemp=ptemp.next
#             count+=1
        
#         index=count-n
        
#         # 两种情况，一种删第一个，一种删中间的和最后一个，都一样
#         if index==0:
#             head=head.next
#             return head
#         else:
#             ptemp=head
#             for i in range(index-1):
                
#                 ptemp=ptemp.next
#             ptemp.next=ptemp.next.next
#             # print(ptemp.val,head.val)

#             return head
            
            
