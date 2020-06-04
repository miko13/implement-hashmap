from linked_list import LinkedList


class MyHashMap(object):
    def __init__(self, buckets=10):
        self.size = 0
        self.num_buckets = buckets
        self.linked_lists = [LinkedList() for i in range(buckets)]

    def _get_bucket_index(self, key):
        hash_code = hash(key)
        index = hash_code % self.num_buckets
        return index

    def is_empty(self):
        return self.size == 0

    def add(self, key, value) -> None:
        bucket_index = self._get_bucket_index(key)
        node = self.linked_lists[bucket_index].put(key, value)
        self.size += 1

        if (1.0 * self.size) / self.num_buckets >= 0.7:
            self.resize(grow=True)

    def get(self, key):
        bucket_index = self._get_bucket_index(key)
        node = self.linked_lists[bucket_index].get_key(key)
        return node.value if node else None

    def remove(self, key) -> None:
        bucket_index = self._get_bucket_index(key)
        self.linked_lists[bucket_index].remove(key)
        self.size -= 1

    def update(self, key, value) -> None:
        bucket_index = self._get_bucket_index(key)
        node = self.linked_lists[bucket_index].get_key(key)
        if node:
            node.value = value

    def resize(self, grow=True):
        self.num_buckets = self.num_buckets * 2 if grow else self.num_buckets / 2

        old_lists = self.linked_lists
        self.linked_lists = [LinkedList() for i in range(self.num_buckets)]
        self.size = 0

        for llist in old_lists:
            item = llist.head

            while item:
                self.add(item.key, item.value)
                item = item.next
