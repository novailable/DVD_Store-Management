import db_manager
from customer import Customer
from binary_search_tree import BST


class CustomerManager:

    def __init__(self):
        self.customers = BST()
        self.new_cust_id = None
        self.new_acc_num = None
        self.load_customer()


    def load_customer(self):
        _cust_data = db_manager.select_tb(tb_name="customer")
        self.new_cust_id = max(_cust_data)[0]
        self.new_acc_num = max(_cust_data)[3]
        print(self.new_cust_id, self.new_acc_num)
        for customer in _cust_data:
            _c_id = customer[0]
            _f_name = customer[1]
            _l_name = customer[2]
            _acc_num = customer[3]
            _query = "select rental.rental_id, dvd.m_name, rental.rent_date, rental.return_date " \
                     f"from dvd join rental on dvd.dvd_id = rental.dvd_id " \
                     f"where rental.acc_num = {_acc_num}"

            self.customers.append(Customer(_c_id, _f_name, _l_name, _acc_num,
                                           rented_dvd_list=db_manager.select_tb(query=_query)))

    def show_all_cust(self):
        _line = "-" * 91
        _output_tuple = (("Customer ID", "^11"), ("Name", "^50"), ("Account Number", "^20"))
        output = f"\t{_line}\n\t|"
        for data, space in _output_tuple:
            output += f" {data:{space}} |"
        output += f"\n\t{_line}"
        print(output)
        self.customers.in_order_traversal()
        print("\t" + _line)

    def search(self, acc_num):
        node = self.customers
        while True:

            if acc_num == node.class_data.get_acc_num():
                # print(node.class_data, " == ")
                return node.class_data
            elif acc_num < node.class_data.get_acc_num():
                if node.left:
                    node = node.left
                    continue
                    # print(node.class_data, "left")
            elif acc_num > node.class_data.get_acc_num():
                if node.right:
                    node = node.right
                    continue
                    # print(node.class_data, "right")
            return False

    def add_customer(self, f_name, l_name):
        self.new_cust_id += 1
        self.new_acc_num += 1
        db_manager.insert_tb("customer", [self.new_cust_id, f_name, l_name, self.new_acc_num])
        self.customers.append(Customer(self.new_cust_id, f_name, l_name, self.new_acc_num))


if __name__ == '__main__':
    test = CustomerManager()
    test.load_customer()
    test.show_all_cust()
    print(test.search(1015))
