# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_node = TreeNode(preorder[0])

        inorder_index = inorder.index(preorder[0])
        
        root_node.left = self.buildTree(preorder[1:inorder_index + 1], inorder[:inorder_index])
        root_node.right = self.buildTree(preorder[inorder_index + 1:], inorder[inorder_index + 1:])

        return root_node
        