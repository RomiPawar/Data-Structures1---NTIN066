#!/usr/bin/env python3

class Node:
    """Node in a binary tree `Tree`"""

    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

class Tree:
    """A simple binary search tree"""

    def __init__(self, root=None):
        self.root = root

    def insert(self, key, node=None):
        """Insert key into the tree.

        If the key is already present, do nothing.
        If the node is given, start searching a new position from that node.
        """
        if self.root is None:
            self.root = Node(key)
            return self.root

        if not node:
            node = self.root

        while node.key != key:
            if key < node.key:
                if node.left is None:
                    node.left = Node(key, parent=node)
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(key, parent=node)
                node = node.right

        return node

    def successor(self, node=None):
        """Return successor of the given node.

        The successor of a node is the node with the next greater key.
        Return None if there is no such node.
        If the argument is None, return the node with the smallest key.
        """
        # TODO: Implement
        #If no node provided, returning the leftmost node
        if node is None:
            node = self.root
            if node is None:
                return None
            while node.left:
                node = node.left
            return node
        #Node has a right subtree
        if node.right:
            succ = node.right
            while succ.left:
                succ = succ.left
            return succ
        
        #No right subtree, finding closest ancestor whose left child is ancestor of node
        while node.parent and node == node.parent.right:  
            node = node.parent
        return node.parent
        raise NotImplementedError
