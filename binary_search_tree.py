class BST:

    def __init__(self, class_data=None):
        self.class_data = class_data
        self.left = None
        self.right = None

    def append(self, class_data):

        if self.class_data is None:
            self.class_data = class_data
        elif class_data < self.class_data:
            if self.left:
                self.left.append(class_data)
            else:
                self.left = BST(class_data)
        elif self.class_data < class_data:
            if self.right:
                self.right.append(class_data)
            else:
                self.right = BST(class_data)

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.class_data)
        if self.right:
            self.right.in_order_traversal()

    def search(self, class_data):
        if class_data == self.class_data:
            return self.class_data
        elif class_data < self.class_data:
            return self.left.search_dvd(class_data)
        else:
            return self.right.search_dvd(class_data)


if __name__ == '__main__':
    test = BST()
    test.append(4)
    test.append(5)
    # test.append(Customer(4, "customer", "4", 4))
    # test.append(Customer(2, "customer", "2", 2))
    # test.append(Customer(1, "customer", "1", 1))
    # test.append(Customer(7, "customer", "7", 7))
    # test.append(Customer(5, "customer", "5", 5))
    # test.append(Customer(9, "customer", "9", 9))
    # test.append(Customer(11, "customer", "11", 11))
    # test.append(Customer(10, "customer", "10", 10))
    # test.append(Customer(8, "customer", "8", 8))
    # test.in_order_traversal()
    print(test.search(4), "result")
