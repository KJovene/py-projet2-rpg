class Game:
    def __init__(self, name: str, main_player: Player):
        self.name = name,
        self.main_player = main_player

    def start():
        pass

    def save():
        pass

    def load():
        pass


class Entity:
    def __init__(self, name: str, description: str, level: int, xp: float, stats: dict, attack_list: list):
        self.name = name
        self.description = description
        self.level = level
        self.xp = xp
        self.stats = stats or {}
        self.attack_list = attack_list or []
        self.status = []

    def attack(self, target: 'Entity') -> None:
        """Effectue une attaque sur la cible"""
        pass

    def take_damage(self, amount: int, damage_type: str) -> None:
        """Reçoit des dégâts d'un certain type"""
        pass

class Pnj(Entity):
    def __init__(self, dialog: list):
        self.dialog = dialog

    def interact(self):
        pass

class Monster(Entity):
    def __init__(self, name: str, description: str, level: int, stats: dict, attack_list: list, dropable_items: list):
        super().__init__(name, description, level, 0, stats, attack_list)
        self.dropable_items = dropable_items

    def attack():
        pass

    def calculate_drops():
        pass

class Place:
    def __init__(self, name: str, description: str, places_around: dict, monsters: list):
        self.name = name
        self.description = description
        self.places_around = places_around
        self.monsters = monsters
        self.exploration = False

    def interact():
        pass

class Player(Entity):
    def __init__(self, name: str, level: int, xp: float, stats: dict, attack_list: list, place: Place ):
        super().__init__(name, "", level, xp, stats, attack_list)
        self.inventory = []
        self.place = place

    def show_inventory(self):
        pass

    def use_item(self):
        pass

    def move(self):
        pass

    def add_xp(self):
        pass

class Combat:
    def __init__(self, player: Player, target: Monster):
        self.turn = 1
        self.player = player
        self.target = target
        self.is_active = True

    def start(self) -> None:
        """Démarre le combat"""
        console.print(f"[red]Combat contre {self.target.name} commencé ![/red]")

    def process_turn(self) -> None:
        """Gère un tour de combat"""
        pass

    def end():
        pass

    def escape():
        pass

class Item:
    def __init__(self, name: str, description: str, effect: dict):
        self.name = name
        self.descritpion = description
        self.effect = effect

class Equipable(Item):
    def __init__(self, name: str, description: str, effect: dict):
        super().__init__(name, description, effect)
        self.equiped = False

    def equip(self):
        pass

class Consomable(Item):
    def __init__(self, name: str, description: str, effect: dict, durability: int):
        super().__init__(name, description, effect)
        self.active = False
        self.durability = durability

    def use(self):
        pass

class Attack:
    def __init__(self, name: str, description: str, damage_type: str, durability: int, effect: dict):
        self.name = name
        self.description = description
        self.damage_type = damage_type
        self.durability = durability
        self.effect = effect


if __name__ == "__main__":
    game = Game("Mon RPG")
    game.start()
