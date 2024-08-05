# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


# When the fast pointer reaches the end of the list, the slow pointer will be at the middle node.

# length = 0
# node = head
# while node:
#     length += 1
#     node = node.next

# i = 0
# node = head
# while i < length // 2:
#     node = node.next
#     i += 1

# return node
