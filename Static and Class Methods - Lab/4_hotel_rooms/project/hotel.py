from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = next((r for r in self.rooms if r.number == room_number), None)

        if room:
            return room.take_room(people)

    def free_room(self, room_number: int):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room:
            return room.free_room()

    def status(self):
        free_rooms = [r.number for r in self.rooms if not r.is_taken]
        taken_rooms = [r.number for r in self.rooms if r.is_taken]
        total_guests = sum([g.guests for g in self.rooms])

        result = ""
        result += f"Hotel {self.name} has {total_guests} total guests\n"
        result += f"Free rooms: {', '.join(map(str, free_rooms))}\n"
        result += f"Taken rooms: {', '.join(map(str, taken_rooms))}"
        return result.strip()
