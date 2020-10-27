import datetime


if __name__ == "__main__":
    print("\t**********************************************")
    print("\t***  Simple Database Ver.0.0.32i-snapshot  ***")
    print("\t**********************************************\n")

    print("Select an action:")
    print("\t1 - show all albumes")
    print("\t2 - add new alnum")
    print("\t3 - change some album content")
    print("\t4 - delete some album")

    choice = input()
    if choice == "1":
        pass

    if choice == "2":
        pass

    if choice == "3":
        pass

    if choice == "4":
        pass


class Album:
    __name = str()
    __artist = str()
    __bpm = float()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        name = str(name)
        self.__name = name

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, artist):
        artist = str(artist)
        self.__artist = artist

    @property
    def bpm(self):
        return self.__bpm

    @bpm.setter
    def bpm(self, bpm):
        try:
            bpm = float(bpm)
            if bpm > 0:
                self.__bpm = bpm
            else:
                raise ValueError
        except ValueError:
            print("Invalid value")
            self.__bpm = None

    @property
    def dateOfRelease(self):
        return self.__dateOfRelease

    @dateOfRelease.setter
    def dateOfRelease(self, dateOfRelease):
        try:
            dateOfRelease = datetime.datetime.strptime(
                dateOfRelease, "%Y-%m-%d %H:%M:%S")
            self.__dateOfRelease = dateOfRelease
        except ValueError:
            print("Invalid value")
            self.__dateOfRelease = None

    def __init__(self, name, artist, dateOfRelease, bpm):
        self.name = name
        self.artist = artist
        self.dateOfRelease = dateOfRelease
        self.bpm = bpm


class EP(Album):
    pass
