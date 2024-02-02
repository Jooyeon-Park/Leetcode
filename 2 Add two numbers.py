# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode()
        carry = 0
        i = 0
        while l1 or l2:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            node.val = sum % 10  
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if l1 or l2:
                newNode = ListNode()
                node.next = newNode
                node = newNode 
        if carry == 1:
            node.next = ListNode(1)
        return head
            

        