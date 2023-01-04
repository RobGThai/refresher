# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    https://leetcode.com/problems/reverse-linked-list
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = None

        while head:
            n = head.next
            head.next = root
            root = head
            head = n

        return root