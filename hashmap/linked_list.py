from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def put(self, key, value) -> None:
        new_node = Node(key, value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        return new_node

    def get_key(self, key):
        node = self.head
        while node:
            if node.key == key:
                return node
            node = node.next
        return

    def get_value(self, value):
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        return

    def update(self, key, value) -> None:
        node = self.get_key(key=key)
        if node:
            node.value = value
            return node

    def remove(self, key) -> None:
        curr = self.head
        if self.head.key == key:
            if self.head.next is not None:
                self.head.next.prev = None
            self.head = self.head.next
        if self.tail and self.tail.key == key:
            if self.tail.prev is not None:
                self.tail.prev.next = None
            self.tail = self.tail.prev

        while curr:
            if curr.key == key:
                curr.remove()
                self.size -= 1
                break
            curr = curr.next
        return

    def is_empty(self) -> bool:
        return self.size == 0 and self.head is None and self.tail is None

    def items(self) -> dict:
        items = []
        curr = self.head

        while curr:
            items.append((curr.key, curr.value))
            curr = curr.next
        return items
