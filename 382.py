class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        odd = head
        even = head.next
        even_head = head.next
        
        while even != None and even.next != None:
            odd.next=odd.next.next
            odd=odd.next

            even.next=even.next.next
            even=even.next
        odd.next=even_head
        return head