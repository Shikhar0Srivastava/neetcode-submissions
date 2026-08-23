# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val

        left_sum = self.maxPathSum(root.left)
        right_sum = self.maxPathSum(root.right)

        ans_left = max(left_sum + root.val, left_sum)
        ans_right = max(right_sum + root.val, right_sum)
        ans_mid = max(ans_left, ans_right)
        return max(ans_mid, root.val + left_sum + right_sum)
        