class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def show_all(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def show_all_reverse(self):
        self._show_all_reverse(self.head)

    def _show_all_reverse(self, node):
        if node is None:
            return
        self._show_all_reverse(node.next)
        print(node.data)


    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

