class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        prev=None
        slow=fast=head
        
        while (fast and fast.next !=None):
            prev=slow
            slow =slow.next
            fast =fast.next.next
        prev.next=slow.next
        return head
