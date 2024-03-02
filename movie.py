class Movie:

    def __init__(self, m_id, m_name, genre, directors, producers, m_stars, copies):
        self.__m_id = m_id
        self.__m_name = m_name
        self.__genre = genre
        self.__directors = directors
        self.__producers = producers
        self.__m_stars = m_stars
        self.__copies = copies

    def get_m_id(self):
        return self.__m_id

    def get_copies(self):
        return self.__copies

    def set_copies(self, copies):
        self.__copies = copies

    def get_m_name(self):
        return self.__m_name

    def get_detail(self):
        _output = f"Movie ID - {self.__m_id}\n" \
                 f"\tMovie Name - {self.__m_name}\n" \
                 f"\tGenre - {self.__genre}\n" \
                 f"\tDirectors - {self.__directors}\n" \
                 f"\tProducers - {self.__producers}\n" \
                 f"\tStars - {self.__m_stars}\n" \
                 f"\tNumber of Copies - {self.__copies}"

        return _output

    
    def __str__(self):
        self.__output_tuple = ((self.__m_id, 8), (self.__m_name, 80), (self.__genre, 40))
        self.__output = "\t|"
        for data, space in self.__output_tuple:
            self.__output += f" {data:<{space}} |"
        return self.__output




if __name__ == '__main__':
    dvd1 = Movie("13124", "RTEtsdascufhqpwofhal", "Sldasd, aldfjask, asdasdf", "wqefadf,a sfasdfasf,adsfasd,aasfa",
                 "asdfasdf, asdfasd", "asdfasdfasfas,asdfasfasadfscd", "34")
    print(dvd1.get_dvd_detail())
    print(dvd1)