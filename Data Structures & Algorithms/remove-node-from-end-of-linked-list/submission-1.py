# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = 0
        current = head
        while current:
            current = current.next
            c +=1
        
        x = c - n - 1
        current = head
        while x > 0:
            current = current.next
            x -=1

        if x == -1:
            head = head.next
        
        if x == 0:
            prev = current
            current = current.next
            prev.next = current.next
            del current


        return head