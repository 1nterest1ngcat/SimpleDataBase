import datetime


class Album:
    __name = str()
    __artist = str()

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
    def dateOfRelease(self):
        return self.__dateOfRelease

    @dateOfRelease.setter
    def dateOfRelease(self, dateOfRelease):
        try:
            dateOfRelease = datetime.datetime.strptime(dateOfRelease, "%Y-%m-%d %H:%M:%S")
            self.__dateOfRelease = dateOfRelease
        except ValueError:
            print("Invalid value")
            self.__dateOfRelease = None

    def __init__(self, name,artist,dateOfRelease):
        self.name = name
        self.artist = artist
        self.dateOfRelease = dateOfRelease


class EP(Album):
    pass

