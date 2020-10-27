
class Song:
    __name = str()
    __bpm = float()
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

    def __init__(self, name,artist,bpm):
        self.name = name
        self.artist = artist
        self.bpm = bpm
