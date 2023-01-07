from collections import deque
from typing import Optional, List
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    https://leetcode.com/problems/binary-tree-level-order-traversal
    BFS through the tree. The key is to deplete the queue before adding next batch.
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []

        q = deque()
        q.append(root)

        while q:
            size = len(q)
            level = []
            tmp_list = []

            for i in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    tmp_list.append(node.left)

                if node.right:
                    tmp_list.append(node.right)

            result.append(level)
            q.extend(tmp_list)
            level = []
            
        return result