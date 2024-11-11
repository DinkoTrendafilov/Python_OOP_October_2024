from typing import List

from project.song import Song


class Album:
    def __init__(self, name: str, *songs: Song) -> None:
        self.name = name
        self.songs: List[Song] = list(songs)
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."

        song_for_remove = next((s for s in self.songs if s.name == song_name), None)
        if not song_for_remove:
            return "Song is not in the album."
        else:
            self.songs.remove(song_for_remove)
            return f"Removed song {song_name} from album {self.name}."

    def publish(self) -> str:
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        else:
            return f"Album {self.name} is already published."

    def details(self) -> str:
        result = [f"Album {self.name}"]
        for song in self.songs:
            result.append(f"== {song.get_info()}")

        return "\n".join(result)
