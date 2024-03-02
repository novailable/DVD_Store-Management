import db_manager
from dvd import DVD
from linked_list import LinkedList
from movie import Movie
from difflib import SequenceMatcher


def check_similar(txt1, txt2):
    s = SequenceMatcher(None, txt1, txt2)
    similarity = s.ratio()
    if similarity > 0.7:
        return True
    return False


class DVDManager:

    def __init__(self):
        self._new_movie_id = None
        self._new_dvd_id = None
        self._dvds_l_list = LinkedList()
        self._movies_l_list = LinkedList()
        self.load_dvd()
        self.load_movie()

    def load_dvd(self):
        _dvds_data_list = db_manager.select_tb(tb_name="dvd")
        self._new_dvd_id = max(_dvds_data_list)[0]
        for dvd_data in _dvds_data_list:
            _dvd_id = dvd_data[0]
            dvd_name = dvd_data[1]
            acc_num = dvd_data[2]
            self._dvds_l_list.append(DVD(_dvd_id, dvd_name, acc_num))

    def load_movie(self):
        _movies_data_list = db_manager.select_tb(tb_name="movie")
        self._new_movie_id = max(_movies_data_list)[0]
        for movie_data in _movies_data_list:
            m_id = movie_data[0]
            m_name = movie_data[1]
            genre = movie_data[2]
            directors = movie_data[3]
            producers = movie_data[4]
            m_stars = movie_data[5]
            copies = movie_data[6]
            self._movies_l_list.append(Movie(m_id, m_name, genre, directors, producers, m_stars, copies))

    def search_dvd(self, dvd_id):
        _curr = self._dvds_l_list.head
        while _curr:
            if dvd_id == _curr.data.get_dvd_id():
                return _curr.data
            _curr = _curr.next
        return False

    def search_movie(self, movie_name):
        _curr = self._movies_l_list.head
        while _curr:
            if check_similar(movie_name, _curr.data.get_m_name()):
                return _curr.data
            _curr = _curr.next
        return False

    def show_all_dvd(self):
        _output_tuple = (("DVD ID", "^9"), ("Movie Name", "^50"), ("Rented by Account Number", "^24"))
        _line = "\t" + "-" * 93
        _output = _line + "\n\t|"
        for data, space in _output_tuple:
            _output += f" {data:{space}} |"
        _output += "\n" + _line
        print(_output)
        self._dvds_l_list.show_all_reverse()
        print(_line)

    def show_all_movie(self):
        _output_tuple = (("Movie ID", "^8"), ("Movie Name", "^80"), ("Genre", "^40"))
        _line = "\t" + "-" * 138
        _output = _line + "\n\t|"
        for data, space in _output_tuple:
            _output += f" {data:{space}} |"
        _output += "\n" + _line
        print(_output)
        self._movies_l_list.show_all_reverse()
        print(_line)

    def add_movie(self, m_name, genre, directors, producers, m_stars, copies):
        self._new_movie_id += 1
        db_manager.insert_tb("movie", [self._new_movie_id, m_name, genre, directors, producers, m_stars, copies])
        self._movies_l_list.append(Movie(self._new_movie_id, m_name, genre, directors, producers, m_stars, copies))
        for count in range(copies):
            self.add_dvd(m_name)

    def add_dvd(self, dvd_name):
        self._new_dvd_id += 1
        db_manager.insert_tb("dvd", [self._new_dvd_id, dvd_name, None])
        self._dvds_l_list.append(DVD(self._new_dvd_id, dvd_name, None))

    def update_acc_num(self, acc_num, dvd_id):
        db_manager.update_tb("dvd", "acc_num", acc_num, f"where dvd_id = {dvd_id}")

    def update_copies(self, copies, m_id):
        db_manager.update_tb("movie", "copies", copies, f"where m_id = {m_id} ")

    def get_head(self):
        print(self._new_dvd_id)


if __name__ == '__main__':
    DVDManager().get_head()
