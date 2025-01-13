from project.song import Song

class Album:

    def __init__(self, name: str, *args: tuple[Song])-> None:
        self.name = name
        self.songs: list[Song] = [el for el in args]
        self.published = False

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}, It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song} has been added to the album {self.name}"


    def remove_song(self, song_name: str) -> str:
        try:
            song = [el for el in self.songs if el.name == song_name][0]
            if self.published:
                return "Cannot add songs. Album is published."
            self.songs.remove(song)
            return f"Removed song {song.name} from album {self.name}."
        except IndexError:
            return "Song is in not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self) -> str:
        result = f"Album {self.name}\n"
        formatted_songs = [f"=={el.get_info()}" for el in self.songs]
        result += '\n'.join(formatted_songs) + "\n"
        return result




