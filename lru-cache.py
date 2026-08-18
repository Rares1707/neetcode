class Node:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value


class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.head = Node(
            -1, -1
        )  # self.head.next will contain the least recently used node; self.head is just a dummy
        self.tail = self.head  # self.tail will contain the most recently used node
        self.capacity = capacity
        self.length = 0

    def move_node_to_tail(self, node):
        if node == self.tail:
            return
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        self.tail.next, node.prev = node, self.tail
        self.tail = node

    def pop_head(self):
        # pop the head, not the dummy head
        self.hashmap.pop(self.head.next.key, None)
        self.head.next = self.head.next.next
        if self.head.next:
            self.head.next.prev = self.head
        self.length -= 1

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.move_node_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap and self.length == self.capacity:
            self.pop_head()

        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.move_node_to_tail(node)
        else:
            node = Node(key, value)
            self.hashmap[key] = node
            self.tail.next, node.prev = node, self.tail
            self.tail = node
            self.length += 1
