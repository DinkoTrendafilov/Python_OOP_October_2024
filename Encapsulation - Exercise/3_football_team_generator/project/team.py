from typing import List

from project.player import Player


class Team:
    def __init__(self, name: str, rating: int) -> None:
        self.__name = name
        self.__rating = rating
        self.__players: list[Player] = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> str:
        player_to_remove = next((player for player in self.__players if player.name == player_name), None)
        if player_to_remove is None:
            return f"Player {player_name} not found"
        self.__players.remove(player_to_remove)
        return player_to_remove



