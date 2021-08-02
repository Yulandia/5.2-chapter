class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

lyrics = Songs(["Happy birthday to you, ",
                "Happy birthday to you, ",
                "Happy birthday dear Sveta,",
                "Happy birthday to you!"])

lyrics.sing_me_a_song()
