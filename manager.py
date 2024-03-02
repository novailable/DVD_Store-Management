from pprint import pprint

import db_manager
from datetime import datetime
from cust_mng import CustomerManager
from dvd_mng import DVDManager


class Manager:

    def __init__(self):
        self._cust_data = CustomerManager()
        self._dvds_data = DVDManager()
        self._rental_data = db_manager.select_tb(tb_name="rental")
        self._new_rent_id = max(self._rental_data)[0]

    def show_all_movie(self):
        print("\nMovies List")
        self._dvds_data.show_all_movie()

    def show_all_dvd(self):
        print("\nDVDs List")
        self._dvds_data.show_all_dvd()

    def show_all_cust(self):
        print("\nCustomer")
        self._cust_data.show_all_cust()

    def get_movie_detail(self):
        _dvd_name = None
        while True:
            try:
                _dvd_name = input("\tMovie Name: ")
                print(self._dvds_data.search_movie(_dvd_name).get_detail())
                break
            except AttributeError:
                print(f"Can't find the movie named: {_dvd_name}")
                continue

    def get_cust_detail(self):
        _acc_num = 0
        while True:
            try:
                _acc_num = int(input("\tAccount Number: "))
            except ValueError:
                print("Please enter number!")
                continue
            _cust_info = self._cust_data.search(_acc_num)
            if _cust_info:
                print(_cust_info.get_detail())
                break
            else:
                print(f"Can't find customer's account number: {_acc_num}")
                continue

    def add_movie(self):
        _m_name = input("\tMovie Name: ")
        _genre = input("\tGenre: ")
        _directors = input("\tDirectors: ")
        _producers = input("\tProducers: ")
        _m_stars = input("\tMovie Stars: ")
        _copies = None
        while True:
            try:
                _copies = int(input("\tNumber of Copies: "))
                break
            except ValueError:
                print("Please enter number!")
                continue
        print("Loading...")
        self._dvds_data.add_movie(_m_name, _genre, _directors, _producers, _m_stars, _copies)
        print(f"Movie Name - {_m_name} with {_copies} copies is added!")

    def add_dvd(self):
        _m_data = None
        _copies = None
        while True:
            _m_name = input("\tMovie Name: ")
            _m_data = self._dvds_data.search_movie(_m_name)
            if _m_data is False:
                print("Invalid movie name!")
                continue
            try:
                _copies = int(input("\tNumbers of DVD: "))
                break
            except ValueError:
                print("Please enter number!")
                continue

        _m_name = _m_data.get_m_name()
        print("Loading...")
        for count in range(_copies):
            self._dvds_data.add_dvd(_m_name)
        _m_id = _m_data.get_m_id()
        _m_copies = _m_data.get_copies() + _copies
        self._dvds_data.update_copies(_m_copies, _m_id)
        _m_data.set_copies(_m_copies)
        print(f"{_copies} copies of {_m_name} is added!")

    def add_customer(self):
        f_name = input("\tFirst Name: ")
        l_name = input("\tLast Name: ")
        self._cust_data.add_customer(f_name, l_name)

    def check_dvd(self):
        _dvd_id = None
        while True:
            try:
                _dvd_id = int(input("\tDVD ID: "))
            except ValueError:
                print("Please enter number!")
                continue
            _result = self._dvds_data.search_dvd(_dvd_id)
            if _result:
                _m_name = _result.get_m_name()
                _acc_num = _result.get_acc_num()
                if _acc_num is None:
                    print(f"DVD ID: {_dvd_id}\nName - {_m_name} is currently available.")
                else:
                    print(f"DVD ID: {_dvd_id}\nName - {_m_name} is rented by customer's account number - {_acc_num}")
                break
            else:
                print(f"DVD ID: {_dvd_id} is invalid!")
                continue

    def rent_dvd(self):
        _rent_acc_num = None
        print("\nRent DVD")
        while True:
            try:
                _rent_acc_num = int(input("\tAccount Number: "))
            except ValueError:
                print("Please enter number!")
                continue
            _customer = self._cust_data.search(_rent_acc_num)
            if _customer is False:
                print("Invalid Customer ID!")
                continue
            break
        while True:
            try:
                _dvd_id = int(input("\tDVD ID: "))
            except ValueError:
                print("Please enter number!")
                continue
            _result = self._dvds_data.search_dvd(_dvd_id)
            if _result:
                _m_name = _result.get_m_name()
                _dvd_acc_num = _result.get_acc_num()
                if _dvd_acc_num is None:
                    _rent_date = datetime.now().date()
                    self._new_rent_id += 1
                    db_manager.insert_tb("rental",
                                         [self._new_rent_id, _dvd_id, _rent_acc_num, _rent_date.__str__(), None])
                    self._dvds_data.update_acc_num(_rent_acc_num, _dvd_id)
                    self._rental_data.append((self._new_rent_id, _dvd_id, _rent_acc_num, _rent_date.__str__(), None))
                    _result.set_acc_num(_rent_acc_num)
                    print(f"Rental ID: {self._new_rent_id}\n"
                          f"\tDVD ID - {_dvd_id}, {_m_name} is rented by account number: {_rent_acc_num}!")
                else:
                    print(f"DVD ID: {_dvd_id}, {_m_name} is currently unavailable!")
                break
            else:
                print(f"Invalid DVD ID!")
                continue

    def return_dvd(self):
        _result_rental = None
        _return_date = None
        _index = None
        _dvd_id = None
        print("\nReturn DVD")
        while True:
            try:
                _rental_id = int(input("\tRental ID: "))
            except ValueError:
                print("PLease enter number!")
                continue
            for index, rental in enumerate(self._rental_data):
                if _rental_id == rental[0]:
                    _result_rental = rental
                    _index = index
            if _result_rental:
                _return_date = _result_rental[4]
                if _return_date is None or _return_date == "":
                    _return_date = datetime.now().date()

                    _dvd_id = _result_rental[1]
            else:
                print("Invalid Rental ID")
                continue

            self._dvds_data.update_acc_num("NULL", _dvd_id)
            _result_dvd = self._dvds_data.search_dvd(_dvd_id)
            _result_dvd.set_acc_num(None)
            db_manager.update_tb("rental", "return_date", f"'{_return_date}'", f"where rental_id = {_rental_id}")
            _acc_num = _result_rental[2]
            _rent_date = _result_rental[3]
            self._rental_data[_index] = (_rental_id,_dvd_id,_acc_num,_rent_date,_return_date)
            print(f"Rent ID - {_rental_id}\n"
                  f"\tAccount ID: {_acc_num} returned the item DVD's ID: {_dvd_id}")
            break

if __name__ == '__main__':
    manager = Manager()
    # manager.add_dvd()
    #manager.show_all_dvd()
    manager.return_dvd()
    #manager.show_all_dvd()
    # manager.add_movie()
