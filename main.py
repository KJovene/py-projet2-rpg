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
        self.active_player = randint(0 , 1) # 0 = Player /  1 = Monster // Détermine celui qui commence en premier 
    
    def start(self):
        #Début du combat
        Console.print("[red]Vous vous apprêtez à vous battre contre {self.opponent}...\n QUE LE COMBAT COMMENCE[/red]")    
        while self.player.health != 0 and self.opponent.health != 0: #Boucle des tours
            Console.print(f"[bold]Vous avez {self.player.health} PV. \n {self.opponent.name} a {self.opponent.health} PV.") #Affichage des PV à chaque début de tour
            self.turn()
        self.end()
        
    def turn(self):
        self.turn_number += 1
        if self.active_player and self.turn_number == 1: #Le Player commence le combat
            Console.print(f"[cyan]Tour 1 : Vous commencez en premier ![/cyan]")
            self.player_turn()
        elif self.active_player == 0: #L'adverdsaire commence le combat
            Console.print(f"[cyan]Tour 1 : {self.opponent.name} commence en premier ![/cyan]")
            self.opponent_turn()
            
        if self.active_player == 1:
            Console.print(f"[cyan]Tour {self.turn_number} : A votre tour de jouer ![/cyan]")
            self.player_turn()
        else:
            Console.print(f"[cyan]Tour {self.turn_number} : Au tour de {self.opponent.name} de jouer ![/cyan]")
            self.opponent_turn()    

        self.active_player = 1 - self.active_player #Inversion de active_player après chaque tour (alterne entre 0 et 1)


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
                
                self.player.attack(self.opponent)                
                Console.print(f"Il reste {self.opponent.health} PV à {self.opponent.name}.")
                
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
                    if self.player.inventory: #Si le joueur possède un inventaire
                        item_id = Prompt.ask("Entrez le nom de l'objet à utiliser :", choices = [i for i in range(len(self.player.inventory))])
                        self.player.use_item(item_id)
                    else:
                        console.print("[yellow]Votre inventaire est vide ![/yellow]")           

                elif Menu_choice == '2' :
                    Console.print("Retour en arrière.")
                    self.player_turn()

            elif player_interact == '3' :
                self.escape()
            
    def opponent_turn(self):
        
            self.opponent.attack(self.player)
            Console.print(f"Il vous reste {self.player.health} PV.")

    def end(self):
        if self.opponent.health <= 0 :
            amount_xp = 150 
            self.player.add_xp(amount_xp) #Ajoute l'xp au héro, 150 par défault
            drop_item = self.opponent.calculate_drops(dropable_items) #Drop du monstre, dropable_items = la liste des drops du monstre
            Console.print("Le combat est terminé !")
            Console.print("[cyan]Vous avez vaincu {self.opponent.name} \n vous avez gagne {amount_xp} xp, il vous manque ... xp pour augmenter de niveau \n Vous avez trouvé {drop_item}[/cyan]")
        
        if self.player.health <= 0 :
            Console.print("[red]Vous avez été vaincu comme un Looser que vous êtes ! Vous retournez au spawn bredouille ![/red]")          
            self.player.move('spawn')


    def escape(self):
        Console.print("[cyan]Vous arrivez à vous enfuir comme un lâche ![/cyan]")
        self.player.move('spawn')
