from rich.console import Console
from rich.prompt import Prompt

console = Console()

class Game:
    def __init__(self, name: str):
        self.name = name
        self.main_player = None
        self.places = {
            "Spawn": Place(
                name="Spawn",
                description="Le point de départ du joueur",
                places_around={
                    "east": self.places["Souflis Forest"]
                },
                monsters=[]
            ),
            "Souflis Forest": Place(
                name="Souflis Forest",
                description="Un endroit où vous pouvez trouver des ressources",
                places_around={
                    "west": self.places["Spawn"],
                    "north": self.places["Ici tout le monde perd"],
                    "north-east": self.places["Domaine des Souflis"],
                    "east": self.places["Hetic"],
                    "south-east": self.places["Le casino du cartier des plaisirs"],
                    "south": self.places["Le temple des 1 000 moines"]
                },
                monsters=[]
            ),
            "Ici tout le monde perd": Place(
                name="Ici tout le monde perd",
                description="Un endroit où vous pouvez trouver des ressources",
                places_around={
                    "south": self.places["Souflis Forest"],
                },
                monsters=[]
            ),
            "Domaine des Souflis": Place(
                name="Domaine des Souflis",
                description="Un endroit où vous pouvez trouver des ressources",
                places_around={
                    "south-west": self.places["Souflis Forest"],
                },
                  monsters=[]),
            "Le casino du cartier des plaisirs": Place(
                name="Le casino du cartier des plaisirs",
                description="Un endroit où vous pouvez trouver des ressources",
                places_around={
                    "west": self.places["Souflis Forest"],
                },
                monsters=[]
            ),
            "Le temple des 1 000 moines": Place(
                name="Le temple des 1 000 moines",
                description="Un endroit où vous pouvez trouver des ressources",
                places_around={
                    "north-west": self.places["Souflis Forest"],
                },
                monsters=[]
            ),
            "Hetic": Place(
                name="Hetic",
                description="Un endroit où vous pouvez trouver des ressources",
                places_around={
                    "west": self.places["Souflis Forest"],
                },
                monsters=[]
            )
        }

        self.attacks = {
            "Bois de boulogne": Attack(name="Bois de boulogne", description="", battle_cry="", durability=100, effect={"damage": 10} ),
            "Course rapide": Attack(name="Course rapide", description="", battle_cry="", durability=100, effect={"damage": 10} ),
            "Souplesse du judoka": Attack(name="Souplesse du judoka", description="", battle_cry="Go muscu", durability=100, effect={"damage": 10} ),
            "Poing de feu": Attack(name="Poing de feu", description="", battle_cry="Brule en enfer", durability=100, effect={"damage": 10} ),
            "Coup de tonerre": Attack(name="Coup de tonerre", description="", battle_cry="Ça va piquer", durability=100, effect={"damage": 10} ),
            "Grattage du délégué": Attack(name="Grattage du délégué", description="", battle_cry="Donne moi tes hp", durability=100, effect={"damage": 10} ),
            "Lancé de talon": Attack(name="Lancé de talon", description="", battle_cry="Prend toi mon talon", durability=100, effect={"damage": 10} ),
            "Griffure": Attack(name="Griffure", description="", battle_cry="Roarrrr", durability=100, effect={"damage": 10} ),
            "Explosion": Attack(name="Explosion", description="", battle_cry="Araaaaa", durability=100, effect={"damage": 10} ),
            "Vol rapide": Attack(name="Vol rapide", description="", battle_cry="Bismilah", durability=100, effect={"damage": 10} ),
            "Charme": Attack(name="Charme", description="", battle_cry="Mouah 💋", durability=100, effect={"damage": 10} ),
            "Chant brutal": Attack(name="Chant brutal", description="", battle_cry="Dès que je chanterais tu deviendras sourd.", durability=100, effect={"damage": 10} ),
            "Kamehameha": Attack(name="Kamehameha", description="", battle_cry="Redonne mon couscous", durability=100, effect={"damage": 10} ),
            "Malaka": Attack(name="Malaka", description="", battle_cry="Mange mon grec", durability=100, effect={"damage": 10} ),
            "Control Mental": Attack(name="Control Mental", description="", battle_cry="Au hazard", durability=100, effect={"damage": 10} ),
            "Gear 5": Attack(name="Gear 5", description="", battle_cry="Youhouu", durability=100, effect={"damage": 10} ),
            "Fara 1": Attack(name="Fara 1", description="", battle_cry="", durability=100, effect={"damage": 10} ),
            "Fara 2": Attack(name="Fara 2", description="", battle_cry="", durability=100, effect={"damage": 10} ),
            "Amel 1": Attack(name="Amel 1", description="", battle_cry="", durability=100, effect={"damage": 10} ),
            "Amel 2": Attack(name="Amel 2", description="", battle_cry="", durability=100, effect={"damage": 10} )
        }

        self.items = {
            "Clé du casino" : Item(name="Clé du casino", description="Cette clé t'aidera a acceder au boss final !", effect={}),
            "Clé de la fête foraine" : Item(name="Clé de la fête foraine", description="Cette clé t'aidera a acceder au boss final !", effect={}),
            "Clé du temple" : Item(name="Clé du temple", description="Cette clé t'aidera a acceder au boss final !", effect={}),
            "Clé des sou(flis)" : Item(name="Clé du casino", description="Cette clé t'aidera a acceder au boss final !", effect={}),
            "Petite potion rouge": Consomable(name="Petite potion rouge", description="Potion donné par la déesse Gaïa (soigne)", effect={"hp": 5}, durability=1)
        }

        self.artefact = {
            "Ecran du mac": Equipable(name="Ecran du Mac", description="Utilisé comme bouclier, c'est le fameu écran du Mac de Mathieu", effect={"defense": 10}),
            "Maxi Phô Boeuf": Equipable(name="Maxi Phô Boeuf", description="", effect={"damage": 10}),
            "Jeu de cartes": Equipable(name="Jeu de cartes", description="", effect={})
        }

        self.monsters = {
            "Fara": Monster(name="Fara", description="", level=2, stats={}, attack_list=[], dropable_items=[]),
            "Imen": Monster(name="Imen", description="", level=2, stats={}, attack_list=[], dropable_items=[]),
            "Nazim": Monster(name="Nazim", description="", level=2, stats={}, attack_list=[], dropable_items=[]),
            "Nana la renarde": Monster(name="Nana la renarde", description="", level=2, stats={}, attack_list=[], dropable_items=[]),
            "Youva": Monster(name="Youva", description="", level=2, stats={}, attack_list=[], dropable_items=[]),
            "Carglass": Monster(name="Carglass", description="", level=2, stats={}, attack_list=[], dropable_items=[]),
            "Cherif": Monster(name="Cherif", description="", level=2, stats={}, attack_list=[], dropable_items=[]),
            "Noa": Monster(name="Noa", description="", level=2, stats={}, attack_list=[], dropable_items=[]),
            "Hamid": Monster(name="Hamid", description="", level=2, stats={}, attack_list=[], dropable_items=[]),
        }
    def start(self):
        console.print(f"[bold blue]Bienvenue dans {self.name}[/bold blue]")
    def save(self):
        pass
    def load(self):
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
