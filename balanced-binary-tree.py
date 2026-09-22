# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Recursive DFS"""
        # if root is None:
        #     return True

        # is_height_balanced = True

        # def dfs(node):
        #     nonlocal is_height_balanced

        #     if node is None or not is_height_balanced:
        #         return 0

        #     left_height = dfs(node.left)
        #     right_height = dfs(node.right)

        #     if abs(left_height - right_height) > 1:
        #         is_height_balanced = False

        #     return max(left_height, right_height) + 1

        # dfs(root)

        # return is_height_balanced

        """Iterative DFS"""
        if root is None:
            return True

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
                left_height = height[node.left]
                right_height = height[node.right]
                if abs(left_height - right_height) > 1:
                    return False

                height[node] = max(left_height, right_height) + 1

        return True
