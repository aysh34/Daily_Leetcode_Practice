class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A, B = headA, headB
        while A != B:
            A = headB if A is None else A.next
            B = headA if B is None else B.next
        return B # or return A 

 # when A == B it means intersection node(same memory address)
# The intersection occurs when two lists share the exact same node (same memory address), not just the same value.
# By redirecting the pointers to the opposite list’s head after reaching the end, we ensure both pointers traverse the same total distance.