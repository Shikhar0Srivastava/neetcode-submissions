# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        to_visit = collections.deque()
        to_visit.append(root)

        while to_visit:
            queue_length = len(to_visit)
            level = []
            for i in range(queue_length):
                curr = to_visit.popleft()
                if curr:
                    level.append(curr.val)
                    to_visit.append(curr.left)
                    to_visit.append(curr.right)
            if level:
                res.append(level)
        return res

        