class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict[str: int] = {}
        self.guild = Player.DEFAULT_GUILD

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        skills = "\n".join(f'==={s} - {v}' for s, v in self.skills.items())

        return f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n{skills}"
