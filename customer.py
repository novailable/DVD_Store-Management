
class Customer:
    __line = "-" * 94

    def __init__(self, c_id, f_name, l_name, acc_no, rented_dvd_list=None):
        """c_data_list: c_id, f_name, l_name, rented_dvd_list: Movie Name, Rent Date, Return Date"""
        if rented_dvd_list is None:
            rented_dvd_list = []
        self.__c_id = c_id
        self.__f_name = f_name
        self.__l_name = l_name
        self.__acc_no = acc_no
        self.__dvd_list = rented_dvd_list

    def get_name(self):
        return f"{self.__f_name} {self.__l_name}"

    def get_acc_num(self):
        return self.__acc_no

    def get_detail(self):
        _output_tuple = (("Rental ID", "^8"), ("Movie Name", "^50"), ("Rent Date", "^11"), ("Return Date", "^11"))
        _output_detail = f"\nCustomer Detail of ID: {self.__c_id}\n" \
                               f"\tName - {self.get_name()}\n" \
                               f"\tAccount Number - {self.__acc_no}\n\t" \
                               f"\n\tRented DVD history of customer\n\t\t" +\
                               self.__line + "\n\t\t|"
        for data, space in _output_tuple:
            _output_detail += f" {data:{space}} |"

        _output_detail += f"\n\t\t{self.__line}\n"

        if len(self.__dvd_list):
            for dvds in self.__dvd_list:
                _return_date = dvds[3]
                if _return_date is None:
                    _return_date = "None"
                _output_detail += f"\t\t| {dvds[0]:<9} | {dvds[1]:<50} | {dvds[2]:^11} | {_return_date:^11} |\n"
        else:
            data = "None"
            _output_detail += f"\t\t| {data:^9} | {data:^50} | {data:^11} | {data:^11} |\n"

        _output_detail += "\t\t" + self.__line

        return _output_detail

    def __str__(self):
        self.__output_tuple = ((self.__c_id, 11), (self.get_name(), 50), (self.__acc_no, 20))
        self.__output = "\t|"
        for data, space in self.__output_tuple:
            self.__output += f" {data:<{space}} |"
        return self.__output

    def __lt__(self, other):
        return self.__acc_no < other.__acc_no
