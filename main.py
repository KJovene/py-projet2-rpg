from rich.console import Console
from rich.prompt import Prompt
from rich.prompt import Confirm
from random import randint

console = Console()

class Combat:
    def __init__(self, player: Player, opponent: Monster):
        self.turn = 0
        self.player = player
        self.opponent = opponent
        self.active_player = 0 # 0 = Player / 1 = Monster
    
    def start(self):
        Console.print("[red]Vous vous apprêtez à vous battre contre {self.opponent}...\n QUE LE COMBAT COMMENCE[/red]")
        self.active_player = randint(0 , 1) # 0 = Player /  1 = Monster        
        while self.player.health != 0 and self.opponent.health != 0:
            self.turn()
        self.end()
        
    def turn(self):
        if self.active_player:
            Console.print("[cyan]Vous commencez en premier ![/cyan]")
            self.player_turn()
        else:
            Console.print(f"[cyan]{self.opponent} commence en premier ![/cyan]")
            self.opponent_turn()

    def player_turn(self):
            player_interact = Prompt.ask(
                "Choisissez une action\n", 
                choices = [
                        "1", "Attaquer\n",
                        "2", "Inventaire\n",
                        "3","Fuir" ], 
                default= "1"
                )
            if player_interact == '1':
                
                Console.print({self.show_attacks})
                pass #Â remplir une fois la liste d'attaques du héro OK
                self.player.attack(choosen_attack)
                self.opponent.take_damage(attack_damage)

            elif player_interact == '2' :

                self.player.show_inventory()

                Menu_choice = Prompt.ask(
                    choices = [
                        "1" , "Utiliser un objet\n",
                        "2" , "Revenir en arrière\n"
                    ], default= "1"
                )

                if Menu_choice == '1' :

                    inventory_interact = Prompt.ask(
                        "Que souhaitez vous utiliser ?",
                        choices = [i for i in range(len(self.player.inventory))]
                    )             

                    if inventory_interact == "item.name" :

                        Confirm_use = Confirm.ask("Voulez vous vraiment utiliser cet objet ?", default=True)

                        if Confirm_use:
                            self.player.use_item()
                        else:
                            Console.print("Action annulée !\n Retour en arrière.")
                            self.player.player_turn()

                elif Menu_choice == '2' :
                    Console.print("Retour en arrière.")
                    self.player.player_turn()

            elif player_interact == '3' :
                self.escape()
            
    def opponent_turn(self):
            self.opponent.attack()
            self.player.take_damage()

    def end(self):
        if self.opponent.health <= 0 :
            self.player.add_xp()
            self.opponent.calculate_drops()
            Console.print("Le combat est terminé !")
            Console.print("[cyan]Vous avez vaincu {self.opponent} \n XP = +{amount} \n Vous avez trouvé {drop_item}[/cyan]")
        
        if self.player.health <= 0 :
            Console.print("[red]Vous avez été vaincu comme un Looser que vous êtes ! Vous retournez au spawn bredouille ![/red]")          
            self.player.move('spawn')


    def escape(self):
        Console.print("[cyan]Vous arrivez à vous enfuir comme un lâche ![/cyan]")
        self.player.move('spawn')
        
