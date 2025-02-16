# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        occur = set()

        return self.helper(head, occur)
    def helper(self, head, occur) -> bool:
        # print(head.val)
        if head in occur:
            return True
        if head.next == None:
            return False
        occur.add(head)
        return self.helper(head.next, occur)