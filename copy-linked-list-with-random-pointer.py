"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def __init__(self):
        self.original_to_copy = {}

    def copy_node(self, node: Optional[Node]):
        if not node:
            return None

        new_node = Node(node.val, None, None)
        self.original_to_copy[node] = new_node

        new_node.next = self.copy_node(node.next)
        new_node.random = self.original_to_copy.get(node.random)

        return new_node

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        return self.copy_node(head)
