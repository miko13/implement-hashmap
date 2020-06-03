import unittest
from linked_list import LinkedList


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def tearDown(self):
        self.linked_list = None

    def test_initialize(self):
        new_linked_list = LinkedList()
        self.assertTrue(new_linked_list.is_empty())
        self.assertTrue(new_linked_list.size == 0)

    def test_put(self):
        self.assertTrue(self.linked_list.is_empty())

        # add a first node that will be both the head and the tail
        first_node = self.linked_list.put(key=10, value=45)

        self.assertFalse(self.linked_list.is_empty())
        self.assertTrue(self.linked_list.head.key == first_node.key)
        self.assertTrue(self.linked_list.head.value == first_node.value)
        self.assertIsNone(self.linked_list.head.next)

        # add a second node that will be the tail
        # its .prev will be the head
        second_node = self.linked_list.put(key=5, value=89)

        self.assertFalse(self.linked_list.is_empty())
        self.assertTrue(self.linked_list.tail.key == second_node.key)
        self.assertTrue(self.linked_list.tail.value == second_node.value)
        self.assertIsNone(self.linked_list.tail.next)
        self.assertTrue(self.linked_list.head.key == first_node.key)
        self.assertTrue(self.linked_list.head.value == first_node.value)
        self.assertEqual(self.linked_list.head.next, self.linked_list.tail)

        # add a third node that will be the tail
        # its .prev will be the second node
        third_node = self.linked_list.put(key=23, value=50)

        self.assertFalse(self.linked_list.is_empty())
        self.assertTrue(self.linked_list.tail.key == third_node.key)
        self.assertTrue(self.linked_list.tail.value == third_node.value)
        self.assertIsNone(self.linked_list.tail.next)
        self.assertEqual(self.linked_list.tail.prev, second_node)

    def test_get_key(self):
        first_node = self.linked_list.put(key=2, value=14)
        second_node = self.linked_list.put(key="nope", value=30)
        third_node = self.linked_list.put(key=3, value=21)

        no_matched_node = self.linked_list.get_key(key=6)
        self.assertIsNone(no_matched_node)

        searched_node = self.linked_list.get_key(key="nope")
        self.assertEqual(searched_node, second_node)

    def test_get_value(self):
        first_node = self.linked_list.put(key=2, value=14)
        second_node = self.linked_list.put(key="nope", value=30)
        third_node = self.linked_list.put(key=3, value=21)

        no_matched_node = self.linked_list.get_value(value="hello")
        self.assertIsNone(no_matched_node)

        searched_node = self.linked_list.get_value(value=30)
        self.assertEqual(searched_node, second_node)

    def test_update(self):
        first_node = self.linked_list.put(key=2, value=14)
        second_node = self.linked_list.put(key="lemonade", value=30)
        third_node = self.linked_list.put(key=3, value=21)

        updated_node = self.linked_list.update(key="lemonade", value=10)
        self.assertIsNotNone(updated_node)
        self.assertEqual(updated_node.value, 10)
        self.assertEqual(second_node, updated_node)

    def test_remove(self):
        first_node = self.linked_list.put(key="Wizard", value=14)
        second_node = self.linked_list.put(key="Leopard", value=30)
        third_node = self.linked_list.put(key="Harkonnen", value=21)
        self.assertEqual(self.linked_list.size, 3)

        self.linked_list.remove(key="Leopard")
        self.assertTrue(self.linked_list.head, second_node)
        self.assertFalse(self.linked_list.is_empty())
        self.assertEqual(self.linked_list.size, 2)

        self.linked_list.remove(key="Wizard")
        self.assertTrue(self.linked_list.head, third_node)
        self.assertFalse(self.linked_list.is_empty())
        self.assertEqual(self.linked_list.size, 1)

    def test_items(self):
        self.assertEqual(self.linked_list.items(), [])

        first_node = self.linked_list.put(key="Harkonnen", value=21)
        one_item = self.linked_list.items()
        self.assertEqual(one_item, [(first_node.key, first_node.value)])
        self.assertEqual(len(one_item), 1)

        second_node = self.linked_list.put(key="Leopard", value=30)
        two_items = self.linked_list.items()
        self.assertEqual(
            two_items,
            [(first_node.key, first_node.value), (second_node.key, second_node.value)],
        )
        self.assertEqual(len(two_items), 2)


if __name__ == "__main__":
    unittest.main()
