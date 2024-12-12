import random
from rich.console import Console
from rich.prompt import Prompt

console = Console()

class Entity:
    def __init__(self, name: str, description: str, level: int, xp: float, stats: dict, attack_list: list):
        self.name = name
        self.description = description
        self.level = level
        self.xp = xp
        self.stat = stats or {"health": 100, "attack": 10, "defense": 5}
        self.max_hp = self.stat["health"]
        self.attack_list = attack_list or []

    def attack(self, target):
        if not self.attack_list:
            console.print(f"{self.name} n'a aucune attaque disponible")
        attack_chosen = random.choice(self.attack_list) if isinstance(target, Monster) else self.choose_attack()
        damage = max(attack_chosen["damage"] + self.stat["attack"] - target.stat["defense"], 0)

        console.print(f"{self.name} attaque {target.name} avec {attack_chosen['name']} et inflige {damage} de dégâts.")
        target.change_stats(-damage, "health")

    def choose_attack(self):
        choices = "\n".join([f"{i} - {attack['name']}" for i, attack in enumerate(self.attack_list)])
        choice = int(Prompt.ask(f"Choisissez votre attaque :\n{choices}\n", choices=[str(i) for i in range(len(self.attack_list))]))
        return self.attack_list[choice]

    def change_stats(self, amount: int, damage_type: str):
        actual_damage = max(amount, 0)

        if damage_type == "health":
            self.stat["health"] += actual_damage
            self.stat["health"] = max(0, min(self.stat["health"], self.max_hp))
            console.print(f"La santé de {self.name} est maintenant à {self.stat['health']}")
            if self.stat["health"] <= 0:
                console.print(f"{self.name} est vaincu !")

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

class Player(Entity):
    def __init__(self, name: str, level: int, xp: float, stats: dict, attack_list: list, place):
        super().__init__(name, "", level, xp, stats, attack_list)
        self.inventory = []
        self.place = place

    def show_inventory(self):
        if not self.inventory:
            console.print(f"L'inventaire de {self.name} est vide")
        else:
            console.print(f"[bold]{self.name} - Inventaire :[/bold]")
            for index, item in enumerate(self.inventory, start=1):
                console.print(f"{index}. {item.name} - {item.description}")

    def use_item(self, item_index):
        try:
            item = self.inventory[item_index]
            console.print(f"{self.name} utilise {item.name}")
            item.use(self)
            self.inventory.pop(item_index)
        except IndexError:
            console.print("L'objet choisi n'existe pas dans l'inventaire.")

    def add_xp(self, amount: float):
        self.xp += amount
        while self.xp >= self.level_up_threshold():
            self.xp -= self.level_up_threshold()
            self.level_up()

    def level_up_threshold(self):
        base_xp = 100
        growth_rate = 1.5
        return base_xp * (growth_rate ** (self.level - 1))

    def level_up(self):
        self.level += 1
        console.print(f"[green]{self.name} monte au niveau {self.level}![/green]")

class Item:
    def __init__(self, name: str, description: str, effect: dict):
        self.name = name
        self.description = description
        self.effect = effect

    def use(self, target):
        for stat, value in self.effect.items():
            if stat in target.stat:
                target.stat[stat] = min(target.max_hp if stat == "health" else target.stat[stat] + value, target.max_hp)
        console.print(f"{self.name} a été utilisé avec succès !")

class Equipable(Item):
    def __init__(self, name: str, description: str, effect: dict):
        super().__init__(name, description, effect)
        self.equipped = False

    def equip(self, target):
        if not self.equipped:
            for stat, value in self.effect.items():
                target.stat[stat] += value
            self.equipped = True
            console.print(f"{self.name} est maintenant équipé !")
        else:
            console.print(f"{self.name} est déjà équipé.")

class Consumable(Item):
    def __init__(self, name: str, description: str, effect: dict, durability: int):
        super().__init__(name, description, effect)
        self.durability = durability

    def use(self, target):
        if self.durability > 0:
            super().use(target)
            self.durability -= 1
            if self.durability == 0:
                console.print(f"{self.name} s'est cassé après utilisation.")
        else:
            console.print(f"{self.name} n'est plus utilisable.")

class Combat:
    def __init__(self, player: Player, opponent: Monster):
        self.turn_number = 1
        self.player = player
        self.opponent = opponent
        self.active_player = random.choice([0, 1])  # 0 = Player, 1 = Monster

    def start(self):
        console.print(f"[red]Un combat commence contre {self.opponent.name}![/red]")
        while self.player.stat["health"] > 0 and self.opponent.stat["health"] > 0:
            self.show_health()
            self.turn()
        self.end()

    def show_health(self):
        console.print(f"[bold]{self.player.name} : {self.player.stat['health']} HP[/bold]")
        console.print(f"[bold]{self.opponent.name} : {self.opponent.stat['health']} HP[/bold]")

    def turn(self):
        if self.active_player == 0:
            console.print(f"[cyan]Tour {self.turn_number}: {self.player.name}, à vous de jouer![/cyan]")
            self.player_turn()
        else:
            console.print(f"[magenta]Tour {self.turn_number}: {self.opponent.name} attaque![/magenta]")
            self.opponent_turn()

        self.active_player = 1 - self.active_player
        self.turn_number += 1

    def player_turn(self):
        action = Prompt.ask("Choisissez une action :", choices=["1", "2", "3"], default="1")
        if action == "1":
            self.player.attack(self.opponent)
        elif action == "2":
            self.player.show_inventory()
            item_index = int(Prompt.ask("Choisissez un objet à utiliser (index) ou -1 pour annuler:", default="-1"))
            if item_index != -1:
                self.player.use_item(item_index - 1)
        elif action == "3":
            console.print("[yellow]Vous tentez de fuir...[/yellow]")
            if random.randint(0, 1):
                console.print("[green]Vous avez réussi à fuir![/green]")
                return self.end("escape")
            else:
                console.print("[red]Vous n'avez pas réussi à fuir![/red]")

    def opponent_turn(self):
        self.opponent.attack(self.player)

    def end(self, result="victory"):
        if result == "victory" and self.opponent.stat["health"] <= 0:
            console.print(f"[green]
