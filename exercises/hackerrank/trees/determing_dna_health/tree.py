class Node:
    value = None
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


class Tree:
    root = None

    def __init__(self, arr):
        if not self.root:
            self.root = Node(arr[0])

        for val in arr:
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

    def get_min(self):
        current_node = self.root
        result = None
        while current_node is not None:
            result = current_node.value
            current_node = current_node.left

        return result

    def get_max(self):
        current_node = self.root
        result = None
        while current_node is not None:
            result = current_node.value
            current_node = current_node.right

        return result


t = Tree([6, 5, 8, 1, 2, 3, 4])
print(t.get_max())
