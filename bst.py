# bst.py

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class ContactBST:
    def __init__(self):
        self.root = None

    def insert(self, name):
        """Insert a contact into the BST."""
        if not self.root:
            self.root = TreeNode(name)
        else:
            self._insert(self.root, name)

    def _insert(self, current_node, name):
        if name < current_node.name:
            if current_node.left is None:
                current_node.left = TreeNode(name)
            else:
                self._insert(current_node.left, name)
        elif name > current_node.name:
            if current_node.right is None:
                current_node.right = TreeNode(name)
            else:
                self._insert(current_node.right, name)

    def search(self, name):
        """Search for a contact in the BST."""
        return self._search(self.root, name)

    def _search(self, current_node, name):
        if not current_node:
            return False
        if name == current_node.name:
            return True
        elif name < current_node.name:
            return self._search(current_node.left, name)
        else:
            return self._search(current_node.right, name)

    def delete(self, name):
        """Delete a contact from the BST."""
        self.root = self._delete(self.root, name)

    def _delete(self, current_node, name):
        if not current_node:
            return current_node
        if name < current_node.name:
            current_node.left = self._delete(current_node.left, name)
        elif name > current_node.name:
            current_node.right = self._delete(current_node.right, name)
        else:
            if not current_node.left:
                return current_node.right
            elif not current_node.right:
                return current_node.left
            temp = self._find_min(current_node.right)
            current_node.name = temp.name
            current_node.right = self._delete(current_node.right, temp.name)
        return current_node

    def _find_min(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node

    def display_contacts(self):
        """Return contacts in alphabetical order as a list."""
        contacts = []
        self._in_order_traversal(self.root, contacts)
        return contacts

    def _in_order_traversal(self, current_node, contacts):
        if current_node:
            self._in_order_traversal(current_node.left, contacts)
            contacts.append(current_node.name)
            self._in_order_traversal(current_node.right, contacts)
