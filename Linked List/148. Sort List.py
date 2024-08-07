# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # Base case: if the list is empty or has only one element
            return head

        def middle(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        mid = middle(head)
        right = mid.next
        mid.next = None
        left = head

        # Recursively sort both halves
        left = self.sortList(left) #  self --> it's a method within the Solution class
        right = self.sortList(right)

        def merge(l1,l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val<l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2 
            return dummy.next
        
        return merge(left,right)
        # TC : O(nlogn)
        # SC: O(n)