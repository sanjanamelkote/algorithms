"""
Linked List implementation - insert and delete functions

Design and definitions:
- A linked list consists of nodes which hold specific information of any type, linked by a next value
- A Node is the component of a Linked List.
 * The node will have a value and a next pointer
- The List will be initialized with a root (dummy) node and all insert operations will append the list.
- The first real node is root->next
"""


class Node:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.root = Node()

    def insert(self, value):
        """
        Append a node.
        Time Complexity: O(n) -> we have to traverse the whole LL thus far to add an element at the end
        Memory: O(1) -> only using pointers, no extra space
        """
        curr = self.root
        while curr.next:
            curr = curr.next
        curr.next = Node(value)
            
    
    def delete(self, value):
        """
        Delete a node with a specified value.
        Time Complexity: O(n) -> worst case we are deleting the last value or a value that isn't in the LL so we have to traverse the whole LL looking for it.
        Memory: O(1) -> only using pointers, no extra space
        """

        curr = self.root
        while curr:
            if curr.next and curr.next.val == value:
                curr.next = curr.next.next
                return
            curr = curr.next

