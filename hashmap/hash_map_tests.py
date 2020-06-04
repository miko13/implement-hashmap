import unittest
from hash_map import MyHashMap


class MyHashMapTests(unittest.TestCase):
    def setUp(self):
        self.hashmap = MyHashMap(5)

    def tearDown(self):
        self.hashmap = None

    def initialize_hashmap(self):
        empty_hashmap = MyHashMap(10)
        self.assertEqual(empty_hashmap, 10)

    def test_add(self):
        self.hashmap.add(key="miko", value=10)
        self.assertEqual(self.hashmap.size, 1)
        self.assertEqual(self.hashmap.num_buckets, 5)

        self.hashmap.add(key="GOOG", value=76)
        self.assertEqual(self.hashmap.size, 2)
        self.assertEqual(self.hashmap.num_buckets, 5)

        self.hashmap.add(key="AAPL", value=50)
        self.assertEqual(self.hashmap.size, 3)
        self.assertEqual(self.hashmap.num_buckets, 5)

        self.hashmap.add(key="AMZN", value=10)
        self.assertEqual(self.hashmap.size, 4)
        self.assertEqual(self.hashmap.num_buckets, 10)

    def test_get(self):
        self.hashmap.add(key="miko", value=10)
        self.hashmap.add(key="GOOG", value=76)
        self.hashmap.add(key="AAPL", value=50)
        self.hashmap.add(key="AMZN", value=10)

        gotten_val = self.hashmap.get(key="miko")
        self.assertEqual(gotten_val, 10)

        none_gotten_val = self.hashmap.get(key="nothing")
        self.assertIsNone(none_gotten_val)

    def test_remove(self):
        self.hashmap.add(key="miko", value=10)
        self.hashmap.add(key="GOOG", value=76)
        self.hashmap.add(key="AAPL", value=50)
        self.hashmap.add(key="AMZN", value=10)

        self.hashmap.remove(key="AMZN")
        self.assertIsNone(self.hashmap.get("AMZN"))
        self.assertEqual(self.hashmap.size, 3)

        self.hashmap.remove(key="GOOG")
        self.assertIsNone(self.hashmap.get("GOOG"))
        self.assertEqual(self.hashmap.size, 2)

        self.hashmap.remove(key="miko")
        self.assertIsNone(self.hashmap.get("miko"))
        self.assertEqual(self.hashmap.size, 1)

        self.hashmap.remove(key="AAPL")
        self.assertIsNone(self.hashmap.get("AAPL"))
        self.assertEqual(self.hashmap.size, 0)
        self.assertEqual()


if __name__ == "__main__":
    unittest.main()
