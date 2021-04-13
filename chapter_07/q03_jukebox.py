from enum import Enum

class Song:
    def __init__(self, artist, name) -> None:
        self.artist = artist
        self.name = name


class Jukebox:
    FARE = 0.25 # Per song

    SONGS = {
        'A1': Song('Pink Floyd', 'Money'),
        'B2': Song('The Beatles', 'Help'),
        'C9': Song('Megadeth', 'Symphony of Destruction'),
        'T0': Song('Metalica', 'Enter Sandman'),
    }

    class State(Enum):
        STANDING_BY = 1
        SELECT_SONG_LETTER = 2
        SELECT_SONG_NUMBER = 3
        PLAYING = 4

    def __init__(self) -> None:
        self.state = self.State.STANDING_BY
        self.credits = 0

    def deposit(self, amount):
        self.credits += amount
        print(f"Total credits: {self.credits}")
        self._charge()

    def _charge(self):
        if self.state == self.State.STANDING_BY:
            if self.credits >= self.FARE:
                self.credits -= self.FARE
                print(f"Charged {self.FARE} cents. Remaining credits: {self.credits}")
                print("Please press a letter and a number to select a song")
                self.state = self.State.SELECT_SONG_LETTER

    def press_letter(self, letter):
        if self.state != self.State.SELECT_SONG_LETTER:
            raise RuntimeError("Wrong usage")

        self.selection = letter
        self.state = self.State.SELECT_SONG_NUMBER

    def press_number(self, number):
        if self.state != self.State.SELECT_SONG_NUMBER:
            raise RuntimeError('Wrong usage')

        self.selection += str(number)
        print(f"Selection: {self.selection}")
        self._play_song()

    def _play_song(self):
        if self.selection not in self.SONGS:
            raise RuntimeError('Song not found')

        self.state = self.State.PLAYING
        song = self.SONGS[self.selection]
        print(f"Played {song.artist} - {song.name}")
        self.state = self.State.STANDING_BY
        self._charge()

jb = Jukebox()

jb.deposit(0.80)
jb.press_letter('C')
jb.press_number(9)

jb.press_letter('A')
jb.press_number(1)

jb.press_letter('B')
jb.press_number(2)

jb.press_letter('T')
jb.press_number(0)
