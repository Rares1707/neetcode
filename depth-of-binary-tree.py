# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """My BFS"""
        if root is None:
            return 0

        queue = deque([(root, 1)])
        max_depth = 0
        while queue:
            node, depth = queue.popleft()
            max_depth = max(depth, max_depth)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return max_depth

        """Neetcode's BFS"""
        # if root is None:
        #     return 0

        # queue = deque([root])
        # depth = 0
        # while queue:
        #     depth += 1
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)

        # return depth

        """My DFS"""
        # if root is None:
        #     return 0
        # left_depth = self.maxDepth(root.left)
        # right_depth = self.maxDepth(root.right)
        # return max(left_depth, right_depth) + 1

        """My iterative DFS (needed help)"""
        # if root is None:
        #     return 0

        # stack = [(root, 1)]
        # max_depth = 1
        # while stack:
        #     node, depth = stack.pop()
        #     max_depth = max(max_depth, depth)
        #     if node.left:
        #         stack.append((node.left, depth + 1))
        #     if node.right:
        #         stack.append((node.right, depth + 1))
        # return max_depth
