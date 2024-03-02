class DVD:

    def __init__(self, dvd_id, m_name, acc_num):
        self.__dvd_id = dvd_id
        self.__m_name = m_name
        self.__acc_num = acc_num

    def get_acc_num(self):
        return self.__acc_num

    def get_m_name(self):
        return self.__m_name

    def get_dvd_id(self):
        return self.__dvd_id

    def set_acc_num(self, acc_num):
        self.__acc_num = acc_num

    def __str__(self):
        _acc_num = self.__acc_num
        if _acc_num is None:
            _acc_num = "None"
        self.__output_tuple = ((self.__dvd_id, 9), (self.__m_name, 50), (_acc_num, 24))
        self.__output = "\t|"
        for data, space in self.__output_tuple:
            self.__output += f" {data:<{space}} |"
        return self.__output


if __name__ == '__main__':
    test = [(1, 'Avatar (2009)', 1001), (2, 'Titanic (1997)', 1002),
            (3, 'Star Wars: Episode VII - The Force Awakens (2015)', None)]
    for tests in test:
        test3 = tests[2]
        if tests[2] is None:
            test3 = ""
        print(tests)
        print(DVD(tests[0], tests[1], test3))
