# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        element = []
        element1 = []
        
        # 1. Dono lists se elements nikalna
        while l1:
            element.append(l1.val)
            l1 = l1.next
        while l2:
            element1.append(l2.val)
            l2 = l2.next
        
        # 2. Reverse karna taaki sahi number ban sake
        element.reverse()
        element1.reverse()
        
        sum1 = 0
        sum2 = 0
        for i in element:
            sum1 = i + sum1 * 10
        for i in element1:
            sum2 = i + sum2 * 10

        # 3. Dono ka sum nikalna
        x = sum1 + sum2
        
        # 4. Naya Linked List banana (Dummy node ka use karke)
        dummy = ListNode(0) # Ek temporary shuruati node
        temp = dummy
        
        # Agar x zero hai, toh loop chalane ke bajaye seedhe ek 0 ka node banna chahiye
        if x == 0:
            temp.next = ListNode(0)
        else:
            while x > 0:
                digit = x % 10
                temp.next = ListNode(digit) # Naya node banakar connect kiya
                temp = temp.next            # Temp ko aage badhaya
                x = x // 10
                
        return dummy.next # dummy ke baad se actual list shuru hoti hai