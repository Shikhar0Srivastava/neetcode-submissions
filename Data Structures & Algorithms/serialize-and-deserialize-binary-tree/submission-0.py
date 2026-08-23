# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        return f"{root.val}, {self.serialize(root.left)}, {self.serialize(root.right)}"

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        node_vals = data.split(", ")
        i = 0
        
        def dfs():
            nonlocal i
            if node_vals[i] == "N":
                i += 1
                return None
            node = TreeNode(int(node_vals[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
