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



class Place:
    def __init__(self, name: str, description: str, monsters: Monster):
        self.name = name
        self.description = description
        self.monsters = monsters
        self.exploration = False

    def interact():
        pass

class Combat:
    def __init__(self, player: Player, target: Monster):
        self.turn = 0
        self.player = player
        self.target = target
        self.active = False #Combat ON/OFF

    def start(self):
        print(f"Le combat a commencé entre '{self.target}' et '{self.player}' !")
        self.active = True 
        self.turn()
        

    def turn(self):
        while self.active == True :
            self.turn += 1 #Compteur de tours
            print(f"Tour {self.turn}")
            player_interact = input("Choisir une action (attaquer/inventaire/fuir) : ").lower()
            if player_interact == "attaquer":
                self.player.attack()
                self.target.take_damage()
                if self.target.health <= 0 :
                    print(f"Vous avez vaincu {self.target} !")
                    self.end()
            elif player_interact == "inventaire" :
                self.player.show_inventory()
                self.player.use_item()
            elif player_interact == "fuir" :
                self.escape()
            else:
                print("Action incomprise, veuillez réessayer")
            
            if self.target.health > 0 :
                self.target.attack()
                self.player.take_damage()
                if self.player.health <= 0 :
                    print(f"Vous avez été vaincu par '{self.target}' !")
                    self.end()

    def end(self):
        print("Le combat est terminé !")
        if self.target.health <= 0 :
            self.player.add_xp()
            self.target.calculate_drops()
        else:
            self.active = False #Combat OFF
            self.player.move('spawn')
        
        

    def escape(self):
        print("Vous avez reussi à fuir !")
        self.end() #Appel de fonction pour arrêter le combat
        

class Entity:
    def __init__(self, name: str, description: str, level: int, xp: float, stats: array, attack_list: array):
        self.name = name
        self.description = description
        self.level = level
        self.xp = xp
        self.stats = stats
        self.attack_list = attack_list
        self.status = None

    def attack():
        pass

    def take_damage():
        pass

class Pnj(Entity):
    def __init__(self, dialog: array):
        self.dialog = dialog

    def interact():
        pass

class Player(Entity):
    def __init__(self, name: str, description: str, level: int, xp: float, stats: array, attack_list: array):
        super().__init__(name, description, level, xp, stats, attack_list)
        self.inventory = []
        self.coord = []

    def show_inventory():
        pass

    def use_item():
        pass

    def move():
        pass

    def add_xp():
        pass

class Monster(Entity):
    def __init__(self, name: str, description: str, level: int, stats: array, attack_list: array, dropable_items: array):
        super().__init__(name, description, level, 0, stats, attack_list)
        self.dropable_items = dropable_items

    def attack():
        pass

    def calculate_drops():
        pass

class Item:
    def __init__(self, name: str, description: str, effect: str):
        self.name = name
        self.descritpion = description
        self.effect = effect

class Equipable(Item):
    def __init__(self, name: str, description: str, effect: array):
        self.equiped = False

    def equip():
        pass

class Consomable(Item):
    def __init__(self, name: str, description: str, effect: array, durability: int):
        self.active = False
        self.durability = durability

    def use():
        pass

class Attack:
    def __init__(self, name: str, description: str, AHHHHHH: str, durability: int, effect: dict):
        self.name = name
        self.description = description
        self.AHHHHHH = AHHHHHH
        self.durability = durability
        self.effect = effect # {stat : dégats}
