from project.album import Album

class Band:

    def __init__(self, name: str) -> None:
        self.name = name
        self.albums: list[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)  # Add the album to the band's collection
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        try:
            album_n = [el for el in self.albums if el.name == album_name][0]
            if album_n.published:
                return f"Album has been published. It cannot be removed."
            self.albums.remove(album_n)  # Remove the album before returning
            return f"Album {album_name} has been removed."
        except IndexError:
            return f"Album {album_name} is not found."

    def details(self) -> str:
        result = f"Band {self.name}\n"
        result += "\n".join([el.details() for el in self.albums])
        return result
