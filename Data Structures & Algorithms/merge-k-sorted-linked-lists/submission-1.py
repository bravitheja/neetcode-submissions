# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        
        def twoWayMerge(list1, list2):
            head = ListNode()
            current = head
            while list1 and list2:

                if list1.val < list2.val:
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next
                head = head.next
            
            if list1:
                 head.next = list1
            
            else:
                head.next = list2
            
            return current.next

        if not lists:
            return None
        l1 = lists[0]


        interval = 1

        while interval < len(lists):

            for i in range(0, len(lists)-interval, interval*2):
                lists[i] = twoWayMerge(lists[i], lists[i+interval])

            interval = interval*2

        return lists[0]