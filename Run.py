import datetime
import Song

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
    __songs = list()

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

    @property
    def ___songs(self):
        return self.__songs

    @___songs.setter
    def ___songs(self,songs):
        try:
            songs = list(songs)
            for s in songs:
                if not isinstance(s,Song.Song):
                    raise ValueError
            self.__songs = songs
        except ValueError:
            print(print("Invalid value"))
            self.__songs = None

    @dateOfRelease.setter
    def dateOfRelease(self, dateOfRelease):
        try:
            if isinstance(dateOfRelease, str):
                dateOfRelease = datetime.datetime.strptime(dateOfRelease, "%Y-%m-%d %H:%M:%S")
            self.__dateOfRelease = dateOfRelease
        except ValueError:
            print("Invalid value")
            self.__dateOfRelease = None

    def __init__(self, name,artist,dateOfRelease,songs):
        self.name = name
        self.artist = artist
        self.dateOfRelease = dateOfRelease
        self.__songs = songs

    def __init__(self, name,artist,dateOfRelease):
        self.name = name
        self.artist = artist
        self.dateOfRelease = dateOfRelease

    def __getitem__(self, item):
        try:
            return self.___songs[item]
        except IndexError:
            print("Invalid index")

    def __setitem__(self, key, value):
        try:
            if(not isinstance(value,Song.Song)):
                raise ValueError
            self.___songs[key] = value
        except IndexError:
            print("Invalid index")
        except ValueError:
            print("Invalid value")


    def AddSong(self, song):
        try:
            if (not isinstance(song, Song.Song)):
                raise ValueError
            self.___songs.append(song)
        except ValueError:
            print("Invalid value")

    def RemoveSong(self, song):
        try:
            index = self.___songs.index(song)
            return self.___songs.pop(index)
        except ValueError:
            print("Song isn't in list")
            return None

    def RemoveSongAt(self,index):
        try:
            return self.___songs.pop(index)
        except ValueError:
            print("InvalidIndex")

class EP(Album):
    pass

