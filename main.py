from manager import Manager

OPT_RENTAL, OPT_RETURN, OPT_DVD_INV, OPT_CUST_MNG, OPT_DVD_AVA = 1, 2, 3, 4, 5  # Main Menu

OPT_DVD_TITLE, OPT_DVD_DETAIL, OPT_MOV_ADD, OPT_DVD_ALL, OPT_DVD_ADD = 1, 2, 3, 4, 5  # DVD Menu

OPT_CUST_ALL, OPT_CUST_DETAIL, OPT_CUST_ADD, = 1, 2, 3  # Customer Menu

OPT_QUIT, OPT_BACK = 0, 0  # Quit, Back

FORMAT_ERROR_MSG = "\nPlease enter correct format!"
THANKS_MSG = "\n\U0001F60A~~~Thanks for using~~~~\U0001F609"

#f"\t{OPT_DVD_RENTED}. Check rented DVD\n" \

def menu_input():
    menu_opt = f"\nWelcome to DVD Store\n" \
               f"\t{OPT_RENTAL}. DVD rental\n" \
               f"\t{OPT_RETURN}. DVD return\n" \
               f"\t{OPT_DVD_INV}. DVD inventory management\n" \
               f"\t{OPT_CUST_MNG}. Customer database management\n" \
               f"\t{OPT_DVD_AVA}. Check DVD availability\n" \
               f"\t{OPT_QUIT}. Quit\n" \
               "Choose Option: "

    return int(input(menu_opt))


def dvd_menu_input():
    dvd_opt = f"\nDVD Inventory Management\n" \
              f"\t{OPT_DVD_TITLE}. Show Movies List\n" \
              f"\t{OPT_DVD_DETAIL}. Show Movie details\n" \
              f"\t{OPT_MOV_ADD}. Add Movie\n" \
              f"\t{OPT_DVD_ALL}. Show all DVDs\n" \
              f"\t{OPT_DVD_ADD}. Add DVD\n" \
              f"\t{OPT_BACK}. Back to main menu\n" \
              "Choose Option: "

    return int(input(dvd_opt))


def cust_menu_input():
    cust_opt = f"\nCustomer Database Management\n" \
               f"\t{OPT_CUST_ALL}. Show all customers\n" \
               f"\t{OPT_CUST_DETAIL}. Show customer's detail\n" \
               f"\t{OPT_CUST_ADD}. Add customer\n" \
               f"\t{OPT_BACK}. Back to main menu\n" \
               f"Choose Option: "
    return int(input(cust_opt))


def dvd_func(mng):
    # dvd_dict = {OPT_DVD_TITLE: "dvd title list", OPT_DVD_DETAIL: "dvd detail", OPT_DVD_ALL: "dvd all",
    #           OPT_DVD_AVA: "dvd_ava", OPT_DVD_ADD: "dvd_add"}
    while True:
        dvd_opt_val = dvd_menu_input()
        if dvd_opt_val == OPT_DVD_TITLE:
            mng.show_all_movie()
            continue
        elif dvd_opt_val == OPT_DVD_DETAIL:
            mng.get_movie_detail()
            continue
        elif dvd_opt_val == OPT_MOV_ADD:
            mng.add_movie()
            continue
        elif dvd_opt_val == OPT_DVD_ALL:
            mng.show_all_dvd()
            continue
        elif dvd_opt_val == OPT_DVD_ADD:
            mng.add_dvd()
            continue
        elif dvd_opt_val == OPT_BACK:
            break
        else:
            print(FORMAT_ERROR_MSG)
            continue


def cust_func(mng):
    while True:
        cust_opt_val = cust_menu_input()
        if cust_opt_val == OPT_CUST_ALL:
            mng.show_all_cust()
            continue
        elif cust_opt_val == OPT_CUST_DETAIL:
            mng.get_cust_detail()
            continue
        elif cust_opt_val == OPT_CUST_ADD:
            mng.add_customer()
            continue
        elif cust_opt_val == OPT_BACK:
            break
        else:
            print(FORMAT_ERROR_MSG)
            continue


def main():
    mng = Manager()
    try:
        while True:
            option = menu_input()
            if option == OPT_RENTAL:  # Rent
                mng.rent_dvd()
                continue
            elif option == OPT_RETURN:  # Return
                mng.return_dvd()
                continue
            elif option == OPT_DVD_INV:  # Dvd mng
                dvd_func(mng)
                continue
            elif option == OPT_CUST_MNG:  # cust mng
                cust_func(mng)
                continue
            elif option == OPT_DVD_AVA: # dvd_available
                mng.check_dvd()
                continue
            elif option == OPT_QUIT:  # Quit
                print(THANKS_MSG)
                break
            else:
                print(FORMAT_ERROR_MSG)
                continue
    except KeyboardInterrupt:
        quit("\n\nKeyboard interrupt received, exit." + THANKS_MSG)


if __name__ == '__main__':
    main()
