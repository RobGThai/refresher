# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    https://leetcode.com/problems/validate-binary-search-tree
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # """
        # Inorder tree traversal helps resolve if the tree is valid.
        # """
        # stack = []
        # prev_val = float('-inf')

        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root = root.left
            
        #     root = stack.pop()
        #     if root.val <= prev_val:
        #         return False
        #     prev_val = root.val
        #     root = root.right 

        # return True

        """
        Recursive variants
        """
        def helper(node, left, right) -> bool:
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return helper(node.left, left, node.val) and helper(node.right, node.val, right) 
        return helper(root, -inf, inf)








