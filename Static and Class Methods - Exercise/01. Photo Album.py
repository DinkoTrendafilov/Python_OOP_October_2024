from math import ceil
from typing import List


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    DASHES_COUNT = 11
    SYMBOL_FOR_LINE: str = "-"

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE))

    def add_photo(self, label: str) -> str:
        for i, page in enumerate(self.photos, start=1):
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {i} slot {len(page)}"

        return "No more free slots"

    def display(self):
        result = [self.DASHES_COUNT * self.SYMBOL_FOR_LINE]

        for page in self.photos:
            result.append(("[] " * len(page)).strip())
            result.append(self.DASHES_COUNT * self.SYMBOL_FOR_LINE)

        return "\n".join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
