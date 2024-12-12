import random

class Entity:
    def __init__(self, name: str, description: str, level: int, xp: float, stat: dict, attack_list: list):
        self.name = name
        self.description = description
        self.level = level
        self.xp = xp
        self.stat = stat or {"health" : 100, "attack": 10, "defense": 5}
        self.attack_list = attack_list or []
        self.status = []

    def attack(self, target) -> None:
        if len(self.attack_list) <= 0:
                console.print(f"{self.name} n'a aucune attaque disponible")
        
        attack_chosen = None
        if type(target) is Monster :
            attack_chosen = self.attack_list[random.randint(0, len(self.attack_list) - 1)]
        elif type(target) is Player :
            choice = int(prompt.ask(f"{self.name}, choississez votre attaque parmis celle-ci :\n{"\n".join([f"{i} - {attack.name}" for i, attack in enumerate(self.attack_list)])}\n", choices=[i for i in range(len(self.attack_list))]))
            attack_chosen = self.attack_list[choice]
            
        damage = attack_chosen["damage"] + self.stat["attack"]
        console.print(f"{self.name} attaque {target.name} avec {attack_chosen['name']} et inflige {damage}.")

        target.take_damage(damage, "attack")

    def take_damage(self, amount: int, damage_type: str) -> None:
        defense = self.stat["defense"]
        actual_damage = max(amount - defense, 0)

        if damage_type == "health" :
            self.stat["health"] -= actual_damage
            self.stat["health"] = max(self.stat["health"], 0)

            console.print(f"{self.name} reçoit {actual_damage}. Santé restante : {self.stat['health']}")
            if self.stat["health"] <= 0:
                console.print(f"{self.name} est vaincu")
        elif damage_type == "attack" :
            self.stat["attack"] -= actual_damage
            self.stat["attack"] = max(self.stat["attack"], 0)

            console.print(f"L'attaque de {self.name} déscend de {actual_damage} points. Points d'attaque restante : {self.stat['attack']}")
        elif damage_type == "defense" :
            self.stat["defense"] -= actual_damage
            self.stat["defense"] = max(self.stat["defense"], 0)

            console.print(f"La défense de {self.name} déscend de {actual_damage} points. Points de défense restant : {self.stat['defense']}")

class Monster(Entity):
    def __init__(self, name: str, description: str, level: int, stats: dict, attack_list: list, dropable_items: list):
        super().__init__(name, description, level, 0, stats, attack_list)
        self.dropable_items = dropable_items

    def calculate_drops(self):
        dropped_items = []
        for item, drop_chance in self.dropable_items:
            if random.randint(0, 100) <= drop_chance:
                dropped_items.append(item)
        return dropped_items
        
        # if __name__ == "__main__":
        #     Amelie = Monster(
        #         name = "Amelie",
        #         level = 2,
        #         stats = {"health" : 20, "attack" : 3, "defense" : 2},
        #         attack_list=[],
        #         dropable_items=[
        #             ("Potion de soin", 50)
        #         ]
        #     )
        

class Player(Entity):
    def __init__(self, name: str, level: int, xp: float, stats: dict, attack_list: list, place: Place ):
        super().__init__(name, "", level, xp, stats, attack_list)
        self.inventory = []
        self.place = place

    def show_inventory(self):
        if len(self.inventory) <= 0:
            return console.print(f"\L'inventaire de {self.name} est vide")
        else : 
            console.print(f"\ L'inventaire de {self.name}")
            for index, item in enumerate(self.inventory, start=1):
                item_details = f"{index}. {item.name} - {item.description}" if hasattr(item,"description") else f"{index}.{item.name}"
                console.print(item_details)
                console.print(f"Nombre d'item : {len(self.inventory)}")

    def use_item(self, item_index):
        if len(self.inventory) <= 0:
            return console.print(f"Votre inventaire est vide. Vous n'avez rien à utiliser")
        for index, item in enumerate(self.inventory):
            if index == item_index:
                console.print(f"{self.name} utilise {item.name}")
                if hasattr(item, "use"):
                    item.use(self)
                    self.inventory.remove(item)
                    console.print(f"Vous venez d'utiliser {item.name}")
                else:
                    console.print(f"(Vous ne pouvez pas utiliser {item.name} sur vous)")
                return
        console.print(f"{item.name} n'est pas dans votre inventaire")

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
        
        #On débloque des nouvelles attaques ?
