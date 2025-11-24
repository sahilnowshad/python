# implementation of binary search tree 
#bst have atmost 2 childerns left child and right child the value of left child is less then the value of 
# the right child and parent node This property helps us search, insert, or delete elements quickly 
# (in O(log n) time for balanced trees).
# Binary Search Tree Implementation in Python

class Node:
    def __init__(self, data):
        self.data = data      # Node value
        self.left = None      # Left child
        self.right = None     # Right child

class BST:
    def __init__(self):
        self.root = None

    # Insert new data into BST
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(current.right, data)
        else:
            print(f"{data} already exists in the tree!")

    # Search for a value in BST
    def search(self, data):
        return self._search(self.root, data)

    def _search(self, current, data):
        if current is None:
            return False
        if current.data == data:
            return True
        elif data < current.data:
            return self._search(current.left, data)
        else:
            return self._search(current.right, data)

    # Inorder Traversal (Left → Root → Right)
    def inorder(self):
        print("Inorder Traversal:", end=" ")
        self._inorder(self.root)
        print()

    def _inorder(self, current):
        if current:
            self._inorder(current.left)
            print(current.data, end=" ")
            self._inorder(current.right)

# ----------------------------
# Example Usage
# ----------------------------
bst = BST()
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    bst.insert(v)

bst.inorder()  # Output: 20 30 40 50 60 70 80

print("Search 60:", bst.search(60))  # True
print("Search 25:", bst.search(25))  # False
