# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current_node = head
        d = set()
        
        while current_node:
            if current_node in d:
                return True
            d.add(current_node)
            current_node = current_node.next
        return False




