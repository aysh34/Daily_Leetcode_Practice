# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummyNode = ListNode()
        tail = dummyNode
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            elif list2.val <= list1.val:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # if list1 is not None:
        #     tail.next = list1
        # if list2 is not None:
        #     tail.next = list2
        tail.next = list1 or list2
        return dummyNode.next
