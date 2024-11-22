# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle of the list
        # reverse the second part of the list
        # merge the two sorted lists

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow points to the middle node now

        prev = None
        cur = slow  # now start of the list is slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # now the second part starts from prev

        first = head
        second = prev
        while second.next:  # end of the list
            first.next, first = second, first.next
            second.next, second = first, second.next
