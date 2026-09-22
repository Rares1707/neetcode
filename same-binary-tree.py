# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """BFS"""
        # from collections import deque

        # queue = deque([(p, q)])
        # while queue:
        #     p, q = queue.popleft()

        #     if not p and not q:
        #         continue
        #     if p and not q:
        #         return False
        #     if q and not p:
        #         return False
        #     if p.val != q.val:
        #         return False

        #     queue.append((p.left, q.left))
        #     queue.append((p.right, q.right))

        # return True

        """Iterative DFS"""
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()

            if not p and not q:
                continue
            if p and not q:
                return False
            if q and not p:
                return False
            if p.val != q.val:
                return False

            stack.append((p.left, q.left))
            stack.append((p.right, q.right))

        return True
