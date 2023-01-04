# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    https://leetcode.com/problems/middle-of-the-linked-list/
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Using two pointers moving one at double the speed (fast).
        Once the fast one reach the end, the slow one will be in the middle.
        """
        slow_ptr = fast_ptr = head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr