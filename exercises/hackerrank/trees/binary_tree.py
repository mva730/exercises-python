class Node:
    value = None
    left = None
    right = None

    def __repr__(self):
        return f"VAL: {self.value}, L: {self.left.value if self.left else 'None'}, R: {self.right.value if self.right else 'None'}"

    def __init__(self, value):
        self.value = value

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


class Tree:
    root = None

    def __init__(self, arr):
        for val in arr:
            self.insert(val)

    def get_min(self, node):
        current_node = node
        result = None
        while current_node is not None:
            result = current_node
            current_node = current_node.left

        return result

    def get_max(self, node):
        current_node = node
        result = None
        while current_node is not None:
            result = current_node
            current_node = current_node.right

        return result

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return

        current_node = self.root
        while True:
            if val < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = Node(val)
                    break

            elif val > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = Node(val)
                    break

            else:
                break

    def find_level(self, val):
        level = 0

        current_node = self.root

        while current_node:
            if val < current_node.value:
                current_node = current_node.left
                level += 1

            elif val > current_node.value:
                current_node = current_node.right
                level += 1

            else:
                return level

    def delete(self, val):
        found_node, parent = self.find_node(val)

        # 1. Удаляемый узел - листовый
        if self.is_leaf_node(found_node):
            if self.is_parent_left(parent, found_node):
                parent.left = None
            else:
                parent.right = None

            del found_node
            return

        # 2. У удаляемого узла только 1 потомок слева
        if found_node.left and not found_node.right:
            if self.is_parent_left(parent, found_node):
                parent.left = found_node.left
            else:
                parent.right = found_node.left

            del found_node
            return

        # 2. У удаляемого узла только 1 потомок справа
        if found_node.right and not found_node.left:
            if self.is_parent_left(parent, found_node):
                parent.left = found_node.right
            else:
                parent.right = found_node.right

            del found_node
            return

        # 3. Два потомка.
        right_minimum = self.get_min(found_node.right)

        # Если правая сторона НЕ дерево:
        if not self.is_tree_on_right_side(found_node):
            found_node.value = found_node.right.value
            del found_node.right

        # Если правая сторона дерево:
        else:
            _, minimum_parent = self.find_node(right_minimum.value)

            # 3.1 Если минимум правой стороны листовая нода
            if self.is_leaf_node(right_minimum):
                minimum_parent.left = None
            else:
                if minimum_parent.value == found_node.value:
                    found_node.right = right_minimum.right
                else:
                    minimum_parent.left = right_minimum.right

            found_node.value = right_minimum.value
            del right_minimum
            return

    def find_node(self, val):

        current_node = self.root
        parent = None
        while current_node:
            if val < current_node.value:
                parent = current_node
                current_node = current_node.left

            elif val > current_node.value:
                parent = current_node
                current_node = current_node.right

            else:
                return current_node, parent

    def is_leaf_node(self, node):
        return not node.left and not node.right

    def is_tree_on_right_side(self, node_for_deletion):
        return node_for_deletion.right \
               and (node_for_deletion.right.left or node_for_deletion.right.right)

    def is_parent_left(self, parent, node):
        if not parent.left:
            return False

        return parent.left.value == node.value

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.value, end=' ')
        self.show_tree(node.right)


# 0             6
#             /   \
# 1          5     10
#           /     / \
# 2        2     7   14
#         / \       /  \
# 3      1   3     11   15
#             \     \
# 4            4     12

t = Tree([6, 5, 10, 2, 1, 3, 4, 14, 11, 15])
t.insert(7)
t.insert(9)

t.delete(14)
t.show_tree(t.root)

print()
print(t.find_level(7))
print(t.get_max(t.root).value)
