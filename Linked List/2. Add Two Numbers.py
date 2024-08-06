# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        p1 = l1  # p1 points to head of l1
        p2 = l2
        while p1 or p2 or carry:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            sumValues = v1 + v2 + carry
            digit = sumValues % 10
            carry = sumValues // 10
            newNode = ListNode(
                digit
            )  # creating new node and pointing tail.next to that new node
            tail.next = newNode
            tail = tail.next  # move tail pointer to newly added node
            p1 = p1.next if p1 else None  # move p1 to next node of l1 if p1 exists
            p2 = p2.next if p2 else None
        return dummy.next
