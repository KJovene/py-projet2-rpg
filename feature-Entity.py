class Entity:
    def __init__(self, name: str, description: str, level: int, xp: float, stat: dict, attack_list: list):
        self.name = name
        self.description = description
        self.level = level
        self.xp = xp
        self.stat = stat or {}
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

    def calculate_drops(self):
        pass

class Map :
    def __init__ (self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [["empty" for _ in range(width)] for _ in range(height)]
    
    def show_map(self):
        console.print("Game map:")
        for row in self.grid:
            console.print("".join(row))

game_map = Map(10,10)

class Place:
    def __init__(self, name: str, description: str, monsters: list, interaction, places_around=None):
        self.name = name
        self.description = description
        self.places_around = places_around or {}
        self.monsters = monsters
        self.exploration = False
        self.interaction = interaction

    def interact(self):
        self.interaction(self)

class Player(Entity):
    def __init__(self, name: str, level: int, xp: float, stats: dict, attack_list: list, place: Place ):
        super().__init__(name, "", level, xp, stats, attack_list)
        self.inventory = []
        self.place = place

    def show_inventory(self):
        if not self.inventory :
            console.print(f"\L'inventaire de {self.name} est vide")
        else : 
            console.print(f"\ L'inventaire de {self.name}")
            for index, item in enumerate(self.inventory, start=1):
                item_details = f"{index}. {item.name} - {item.description}" if hasattr(item,"description") else f"{index}.{item.name}"
                console.print(item_details)
                console.print(f"Nombre d'item : {len(self.inventory)}")

    def use_item(self):
        if not self.inventory:
            console.print(f"Votre inventaire est vide. Vous n'avez rien à utiliser")
            return
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                console.print(f"{self.name} utilise {item.name}")
                if hasattr(item, "use") and callable(item.use):
                    item.use(self)
                    self.inventory.remove(item)
                    console.print(f"Vous venez d'utiliser {item.name}")
                else:
                    console.print(f"(Vous ne pouvez pas utiliser {item.name} sur vous)")
                return
        console.print(f"{item.name} n'est pas dans votre inventaire")

    def move(self, place):
        directions = {
            "nord":(1,0),
            "sud":(-1,0),
            "ouest":(0,-1),
            "est":(0,1)
        }
        if direction not in directions:
            console.print(f" Direction non valide, veuillez choisir : nord, sud, ouest ou est")
            return

        delta_row, delta_col = directions[direction]
        new_row = self.place.row + delta_row
        new_col = self.place.col = delta_col
        if not (0 <= new_row < len(game_map) and 0 <= new_col < len(game_map[0])):
            console.print(f"Vous ne pouvez pas vous déplacer vers {direction}. Vous êtes à la limite de la carte")
        
        console.print(f"Vous vous déplacer vers {direction}, vous êtes en ({new_row},{new_col})")
        self.place.row, self.place.col = new_row, new_col

    def add_xp(self, amount : float):
        if amount <= 0 :
            console.print("L'expérience ne peut pas être négative")
        console.print(f"Vous venez de gagner {amount} XP !")
        self.xp += amount
        required_xp = self.level_up_threshold()

        while self.xp >= required_xp:
            self.xp -= required_xp
            self.level_up()
            required_xp = self.level_up_threshold()
    
    def level_up_threshold(self):
        base_xp = 100
        growth_rate = 1.5
        return base_xp * (growth_rate ** (self.level - 1))

    def level_up(self):
        self.level += 1
        print(f"Vous venez de passer au niveau {self.level}")

        for stat, value in self.stats.items():
            increase = int(value*0.1)
            self.stats[stat] += increase
            console.print(f"vos statistiques sont augmentées de {increase} pour {self.stats[stat]} !")
        