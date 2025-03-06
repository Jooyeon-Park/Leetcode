class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # Skip the duplicate
                current.next = current.next.next
            else:
                # Move to next node only if no duplicate was found
                current = current.next
        
        return head