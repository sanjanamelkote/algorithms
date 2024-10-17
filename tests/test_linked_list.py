#tests/test_linked_list.py

import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from linked_list import *

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.llist = LinkedList()

    def test_insert(self):
        self.llist.insert(1)
        self.llist.insert(2)
        self.llist.insert(3)
        self.assertEqual(self.llist.root.next.val, 1)
        self.assertEqual(self.llist.root.next.next.val, 2)
        self.assertEqual(self.llist.root.next.next.next.val, 3)
        self.assertIsNone(self.llist.root.next.next.next.next)


    def test_delete(self):
        self.llist.insert(1)
        self.llist.insert(2)
        self.llist.insert(3)
        self.llist.delete(2)
        self.assertEqual(self.llist.root.next.next.val, 3)
        self.llist.delete(1)
        self.assertEqual(self.llist.root.next.val, 3)
        self.llist.delete(3)
        self.assertIsNone(self.llist.root.next)


    def test_delete_non_existent(self):
        self.llist.insert(1)
        self.llist.insert(2)
        self.llist.delete(3)  # Deleting a non-existent value
        self.assertEqual(self.llist.root.next.val, 1)
        self.assertEqual(self.llist.root.next.next.val, 2)
        self.assertIsNone(self.llist.root.next.next.next)

if __name__ == "__main__":
    unittest.main()
