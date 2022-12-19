class Music():
    def __init__(self,perf,song,album,year):
        self.perf=perf
        self.song=song
        self.album=album
        self.year=year
    def __str__(self):
        return f'Performer: {self.perf}\nSong: {self.song}\nAlbum: {self.album}\nYear: {self.year}'
song1=Music('Harry Styles','As it was',"Harry\'s House",2021)

print(song1)