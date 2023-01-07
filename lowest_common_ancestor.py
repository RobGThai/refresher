# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
    As we are finding common ancestor. We can just check if the value of the current root is out of bound (p, q) or not.
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_value = min(p.val, q.val)
        max_value = max(p.val, q.val)

        if root.val > max_value:
            # look left as the current root value is too high for max
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min_value:
            # look right as the current root value is too low for min
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # Current root is within the bound and must be the common ancestor
            return root