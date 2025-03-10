# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(0)
        output = start
        carry = 0

        temp_l1 = l1
        temp_l2 = l2

        while temp_l1 or temp_l2:
            if not temp_l1.next and temp_l2.next:
                temp_l1.next = ListNode(0)
            if not temp_l2.next and temp_l1.next:
                temp_l2.next = ListNode(0)
            temp_l1 = temp_l1.next
            temp_l2 = temp_l2.next
        # print("l1: ", l1)
        # print("l2: ", l2)

            

        while l1 and l2:
            # print(l1.val)
            #zip <- Research
            if l1.val + l2.val + carry >= 10:
                output.next = ListNode(l1.val + l2.val - 10 + carry)
                carry = 1
            else:
                output.next = ListNode(l1.val + l2.val + carry)
                carry = 0
            l1 = l1.next
            l2 = l2.next
            output = output.next
        if carry != 0:
            output.next = ListNode(carry)
        return start.next
