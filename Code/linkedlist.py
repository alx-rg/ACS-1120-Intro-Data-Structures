#!python


from lib2to3.pgen2.token import EQUAL
from platform import node
from typing import ItemsView
from venv import create
from zipapp import create_archive


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None
        
    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        node = self.head
        count = 0
        while node != None:
            count += 1
            node = self.next
        return count
        # node_count = 0
        # node = self.head
        # print(node)
        # while node is not self.tail:
        #     node = node.next
        #     node_count += 1
        # return node_count


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        created_node = Node(item)
        # check to see if we're at the head/begin of the linked list
        if self.is_empty():
            self.head = created_node
            self.tail = created_node
        else:
            self.tail.next = created_node
            self.tail = created_node
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        # TODO: Else append node after tail


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        created_node = Node(item)
        # TODO: Prepend node before head, if it exists
        # check to see if linked list exists 
        if self.length() == 0:
            # if there is no list, add node to head and tail
            self.head = created_node
            self.tail = created_node
        else:
            # linked list exists! only add to head
            created_node.next = self.head
            self.head = created_node

        

    def find(self, item):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        node = self.head
        while node != None:
            if (item == self.item):
                return True
            else:
                return False
        # TODO: Loop through all nodes to find item, if present return True otherwise False

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

if __name__ == "__main__":
    my_ll = LinkedList(["A", "B", "C"])
    print(my_ll)

    


