# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # If the list has fewer than 3 nodes, there can't be any critical points
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_crit = -1
        prev_crit = -1
        min_dist = float('inf')

        prev = head
        curr = head.next
        nxt = curr.next
        
        pos = 1  # Using 0-based indexing where head is 0, curr is 1

        while nxt:
            # Check if the current node is a local maxima or minima
            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):
                
                if first_crit == -1:
                    first_crit = pos
                else:
                    # Update minimum distance with the adjacent critical point
                    min_dist = min(min_dist, pos - prev_crit)
                
                prev_crit = pos
            
            # Move pointers forward
            prev = curr
            curr = nxt
            nxt = nxt.next
            pos += 1
        
        # If we found fewer than 2 critical points, min_dist remains infinity
        if min_dist == float('inf'):
            return [-1, -1]
        
        # The maximum distance will always be between the first and the last critical point
        max_dist = prev_crit - first_crit
        
        return [min_dist, max_dist]