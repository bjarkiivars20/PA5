class Node:
    def __init__(self, data = None):
        self.data = data

test_node = Node("Testing123")
print(test_node.data)
test_node = None
print(test_node)
