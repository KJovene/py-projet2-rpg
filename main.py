from rich.console import Console
from rich.prompt import Prompt
from rich.prompt import Confirm
from random import randint

console = Console()

class Combat:
    def __init__(self, player: Player, opponent: Monster):
        self.turn_number = 0 
        self.player = player
        self.opponent = opponent
        self.active_player = 0 # 0 = Monster / 1 = Player
    
    def start(self):
        #Début du combat
        Console.print("[red]Vous vous apprêtez à vous battre contre {self.opponent}...\n QUE LE COMBAT COMMENCE[/red]")
        self.active_player = randint(0 , 1) # 0 = Player /  1 = Monster // Détermine celui qui commence en premier       
        while self.player.health != 0 and self.opponent.health != 0: #Boucle des tours
            self.turn()
        self.end()
        
    def turn(self):
        self.turn_number += 1
        if self.active_player and self.turn_number == 1: #Le Player commence le combat
            Console.print(f"[cyan]Tour 1 : Vous commencez en premier ![/cyan]")
            Console.print(f"[bold]Vous avez {self.player.health} PDV. \n {self.opponent.name} a {self.opponent.health} PDV.")
            self.player_turn()
        elif self.active_player == 0: #L'adverdsaire commence le combat
            Console.print(f"[cyan]Tour 1 : {self.opponent.name} commence en premier ![/cyan]")
            Console.print(f"[bold]Vous avez {self.player.health} PDV. \n {self.opponent.name} a {self.opponent.health} PDV.")
            self.opponent_turn()
            
        if self.active_player == 1:
            Console.print(f"[cyan]Tour {self.turn_number} : A votre tour de jouer ![/cyan]")
            Console.print(f"[bold]Vous avez {self.player.health} PDV. \n {self.opponent.name} a {self.opponent.health} PDV.")
            self.player_turn()
        else:
            Console.print(f"[cyan]Tour {self.turn_number} : Au tour de {self.opponent.name} de jouer ![/cyan]")
            Console.print(f"[bold]Vous avez {self.player.health} PDV. \n {self.opponent.name} a {self.opponent.health} PDV.")
            self.opponent_turn()    

        self.active_player = 1 - self.active_player #Inversion de active_player après chaque tour (alterne entre 0 et 1)


    def player_turn(self):
            player_interact = Prompt.ask(
                "Choisissez une action\n", 
                choices = [
                        "1", "Attaquer\n",
                        "2", "Inventaire\n",
                        "3","Fuir" ],C
                default= "1"
                )
            if player_interact == '1':
                
                attack_opponent = self.player.attack(self.opponent)                
                #opponent_damaged = self.opponent.take_damage(attack_opponent)
                Console.print(f"Vous infligez {attack_opponent} dégâts à {self.opponent.name} !")
                Console.print(f"Il reste {self.opponent.health} PDV à {self.opponent.name}.")
                
            elif player_interact == '2' :

                self.player.show_inventory() #Affiche l'inventaire

                Menu_choice = Prompt.ask(
                    choices = [
                        "1" , "Utiliser un objet\n",
                        "2" , "Revenir en arrière\n"
                    ], default= "1"
                )

                if Menu_choice == '1' :
                    self.player.show_inventory() #Ré-affiche l'inventaire
                    inventory_interact = Prompt.ask(
                        "Que souhaitez vous utiliser ?",
                        choices = [i for i in range(len(self.player.inventory))]
                    )             

                    if inventory_interact == "item.name" :

                        Confirm_use = Confirm.ask("Voulez vous vraiment utiliser cet objet ?", default=True)

                        if Confirm_use:
                            item_to_use = inventory_interact
                            self.player.use_item(item_to_use)
                        else:
                            Console.print("Action annulée !\n Retour en arrière.")

                elif Menu_choice == '2' :
                    Console.print("Retour en arrière.")

            elif player_interact == '3' :
                self.escape()
            
    def opponent_turn(self):
        
            attack_player = self.opponent.attack(self.player)
            #player_damaged = self.player.take_damage(attack_player)
            Console.print(f"{self.opponent.name} vous inflige {attack_player} de dégâts !")
            Console.print(f"Il vous reste {self.player.health} PDV.")

    def end(self):
        if self.opponent.health <= 0 :
            amount_xp = self.player.add_xp()
            drop_item = self.opponent.calculate_drops()
            Console.print("Le combat est terminé !")
            Console.print("[cyan]Vous avez vaincu {self.opponent.name} \n XP = +{amount_xp} \n Vous avez trouvé {drop_item}[/cyan]")
        
        if self.player.health <= 0 :
            Console.print("[red]Vous avez été vaincu comme un Looser que vous êtes ! Vous retournez au spawn bredouille ![/red]")          
            self.player.move('spawn')


    def escape(self):
        Console.print("[cyan]Vous arrivez à vous enfuir comme un lâche ![/cyan]")
        self.player.move('spawn')
        
