import datetime

class Album:
    __name = str()
    __artist = str()
    __bpm = float()
    __dateOfRelease = datetime.datetime()
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, artist):
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
        self.__dateOfRelease = dateOfRelease

    def __init__(self, name,str,dateOfRelease, bpm):
        self.name = name
        self.str = str
        self.dateOfRelease = dateOfRelease
        self.bpm = bpm
