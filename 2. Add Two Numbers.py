2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1=''
        while l1:
            s1+=str(l1.val)
            l1=l1.next
        s2=''
        while l2:
            s2+=str(l2.val)
            l2=l2.next
        res=str(int(s1[::-1])+int(s2[::-1]))[::-1]
        return list(map(int,list(res)))

        
        
#         remain = 0
#         result = ListNode(None)
#         presult = result
        
#         while l1 != None or l2 != None:
#             if l1 == None:
#                 l1 = ListNode(0)
#             elif l2 == None:
#                 l2 = ListNode(0)
#             total = l1.val + l2.val + remain
#             if total >=10 :
#                 total = total - 10
#                 remain =1
#             else:
#                 remain = 0
#             presult.val = total
#             presult.next = ListNode(None)
#             presult = presult.next
#             l1 = l1.next
#             l2 = l2.next
            
            
#         if remain == 1:
#             presult.next = ListNode(remain)
            
#         return result
            
