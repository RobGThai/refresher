from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    """
    https://leetcode.com/problems/n-ary-tree-preorder-traversal

    Preorder means reading all of the leaf on one side of the tree first. 
    This can be done using DFS.
    """
    def preorder(self, root: 'Node') -> List[int]:
        # Recursive variants
        # if not root:
        #     return []

        # def visit(node: 'Node') -> List[int]:
        #     result = []
        #     result.append(node.val)
        #     for c in node.children:
        #         result += visit(c)
        #     return result

        # return visit(root)

        # Queue variants. Cheaper memory since no nested callstack necessary.
        if not root:
            return []

        result = []

        queue = deque()
        queue.append(root)

        while queue:
            n = queue.popleft()
            result.append(n.val)
            # print(f"me({n.val}) children: {[c.val for c in n.children]}")
            # Internally extendleft append items individually in sequential order, hence the result will be reversed.
            queue.extendleft(reversed(n.children))

        return result
