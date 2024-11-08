from typing import List


class Shop:
    def __init__(self, name: str, items: List[str]):
        self.name = name
        self.items = items

    def get_items_count(self) -> int:
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
shop1 = Shop("My Shop1", ["Apples", "Bananas", "Cucumbers", "Massive", "Red"])
print(shop.get_items_count())
print(shop1.get_items_count())
