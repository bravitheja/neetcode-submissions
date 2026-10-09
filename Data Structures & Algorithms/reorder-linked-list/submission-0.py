# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        1. Identify middle node
        2. reverse the second half
        3. merge two halfs now
        """

        # 1. Identify middle node
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # 2. reverse the list from 

        current = slow
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # 3. merge now
        list2 = prev
        list1 = head

        new_list = ListNode()

        c = 0
        while list1 and list2:
            if c%2==0:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next
            c+=1
        return new_list.next