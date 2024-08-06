# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = dummy
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
                
        return dummy.next


        # dummy = ListNode()
        # dummy.next = head
        # tail = dummy
        # cur = head
        # while cur:
        #     if cur.val != val:
        #         tail.next = cur
        #         tail = tail.next
        #         cur = cur.next
        #     else:
        #         cur = cur.next
        # tail.next = None
        # return dummy.next


