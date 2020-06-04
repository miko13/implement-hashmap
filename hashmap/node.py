class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def remove(self):
        if self.prev is not None and self.next is not None:
            self.prev.next, self.next.prev = self.next, self.prev
            self.prev, self.next = None, None
        if self.prev is not None:
            self.prev.next = None
        if self.next is not None:
            self.next.prev = None
        return

    def __repr__(self):
        return f"({self.key}, {self.value})"
