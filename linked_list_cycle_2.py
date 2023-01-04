# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    https://leetcode.com/problems/linked-list-cycle-ii
    """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return None
        """
        Use Floyd's cycle detection system
        """
        slow = fast = head
        while fast:
            slow = slow.next
            fast = fast.next

            if fast:
                fast = fast.next
            else:
                return None

            if fast == slow:
                break
        
        if not fast:
            return None

        while slow != head and slow.next:
            slow = slow.next
            head = head.next
        
        print(f"slow: {slow}")
        return slow