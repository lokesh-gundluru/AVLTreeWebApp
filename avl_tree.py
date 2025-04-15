class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Balance the node
        balance_factor = self.get_balance(root)

        # Left heavy case
        if balance_factor > 1:
            if key < root.left.value:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        # Right heavy case
        if balance_factor < -1:
            if key > root.right.value:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Rotate
        y.left = z
        z.right = T2

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Rotate
        y.right = z
        z.left = T3

        return y

    def get_balance(self, root):
        if not root:
            return 0
        return self.height(root.left) - self.height(root.right)

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def delete(self, root, key):
        if not root:
            return root

        if key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                temp = self.get_min_value_node(root.right)
                root.value = temp.value
                root.right = self.delete(root.right, temp.value)

        balance_factor = self.get_balance(root)

        if balance_factor > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def get_preorder(self, root):
        result = []
        if root:
            result.append(root.value)
            result.extend(self.get_preorder(root.left))
            result.extend(self.get_preorder(root.right))
        return result
