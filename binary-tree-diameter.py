# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Recursive DFS"""
        # max_diameter = 0

        # def dfs(node: Optional[TreeNode]) -> int:
        #     nonlocal max_diameter

        #     if node is None:
        #         return 0

        #     left_depth = dfs(node.left)
        #     right_depth = dfs(node.right)

        #     max_diameter = max(max_diameter, left_depth + right_depth)
        #     return max(left_depth, right_depth) + 1

        # dfs(root)
        # return max_diameter

        """Iterative DFS"""
        max_diameter = 0
        height = defaultdict(int)

        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()

            if node is None:
                continue

            if not visited:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
            else:
                left_height = height[node.right]
                right_height = height[node.left]

                height[node] = max(left_height, right_height) + 1
                max_diameter = max(max_diameter, left_height + right_height)

        return max_diameter
