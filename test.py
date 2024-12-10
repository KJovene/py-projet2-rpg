class Combat:
    def __init__(self, player: Player, opponent: Monster):
      # CHANGEMENT DU NOM DU TURN
        self.turn_number = 0
        self.player = player
<<<<<<< feature/combat
        self.opponent = opponent
        self.active_player = 0 # 0 = Player / 1 = Monster
    
    def start(self):
        Console.print("[red]Vous vous apprêtez à vous battre contre {self.opponent}...\n QUE LE COMBAT COMMENCE[/red]")
        self.active_player = randint(0 , 1) # 0 = Player /  1 = Monster        
        while self.player.health != 0 and self.opponent.health != 0:
            self.turn()
        self.end()
        
    def turn(self):
      # AJOUT DU TURN 1 ET DES FUTURS TOURS
        self.turn_number += 1
        if self.turn_number == 1 and self.active_player:
          Console.print("[cyan]Tour 1 : Vous commencez en premier ![/cyan]")
          self.player_turn()
        elif self.turn_number == 1:
          Console.print(f"[cyan]Tour 1 : {self.opponent} commence en premier ![/cyan]"
          self.opponent_turn()
        
        if self.active_player:
            Console.print(f"[cyan]Tour {self.turn_number} : A votre tour de jouer ![/cyan]")
            self.player_turn()
        else:
            Console.print(f"[cyan]Tour {self.turn_number} : Au tour de {self.opponent} de jouer ![/cyan]")
            self.opponent_turn()

    def player_turn(self):
             # EUH... JE CROIS QU'IL Y A UN SOUCIS AVEC CETTE FONCTION, DANS ME MENU CHOICE NOTAMENT, TU MET RETOUR EN ARRIERE MAIS IL SE PASSE QUOI APRÈS ÇA ???? + TU AS PAS CHANGÉ L'ACTIVE PLAYER
            player_interact = Prompt.ask(
                "Choisissez une action\n", 
                choices = [
                        "1", "Attaquer\n",
                        "2", "Inventaire\n",
                        "3","Fuir" ], 
                default= "1"
                )
            if player_interact == '1':
                # ??? Il se passe quoi ici ???
                Console.print({self.show_attacks})
                pass #Â remplir une fois la liste d'attaques du héro OK
                self.player.attack(choosen_attack)
                damage = self.player.attack
                self.opponent.take_damage(damage)

            elif player_interact == '2' :

                self.player.show_inventory()

                Menu_choice = Prompt.ask(
                    choices = [
                        "1" , "Utiliser un objet\n",
                        "2" , "Revenir en arrière\n"
                    ], default= "1"
                )

                if Menu_choice == '1' :
                    # PEUT ÊTRE RE AFFICHER LES ITEMS ??
                    inventory_interact = Prompt.ask(
                        "Que souhaitez vous utiliser ?",
                        choices = [i for i in range(len(self.player.inventory))]
                    )             

                    if inventory_interact == "item.name" :

                        Confirm_use = Confirm.ask("Voulez vous vraiment utiliser cet objet ?", default=True)

                        if Confirm_use:
                        #FRR TON ITEM_TO_USE IL EXISTE PAS, JE VAIS T'ENCULER
                            self.player.use_item(item_to_use)
                        else:
                            Console.print("Action annulée !\n Retour en arrière.")

                elif Menu_choice == '2' :
                    Console.print("Retour en arrière.")

            elif player_interact == '3' :
                self.escape()
            
    def opponent_turn(self):
            # WTF TU L'APPELLE DEUX FOIS ????
            self.opponent.attack()
            damage = self.opponent.attack()
            self.player.take_damage(damage)
            # FAUT CHANGER L'ACTIV PLAYER

    def end(self):
        if self.opponent.health <= 0 :
             # MANQUE LE CLC D'XP MAIS ON VOIS ÇA APRÈS
            self.player.add_xp()
            self.opponent.calculate_drops()
            Console.print("Le combat est terminé !")
            # JE VAIS T'ENCULER ICIC AUSSI, TU MET SELF.OPPONENT MAIS TU MET PAS SON NOM, TU MET AMOUNT MAIS TU L'AS PSA DÉFINI ET DROP ITEMS NON PLUS... LAURENTTTTT
            Console.print("[cyan]Vous avez vaincu {self.opponent} \n XP = +{amount} \n Vous avez trouvé {drop_item}[/cyan]")
        
        if self.player.health <= 0 :
            Console.print("[red]Vous avez été vaincu, Looser que vous êtes ! Vous retournez au spawn bredouille ![/red]")          
            self.player.move('spawn')


    def escape(self):
        Console.print("[cyan]Vous vous enfuyez tel un lâche ![/cyan]")
        # LE SPAWN S'APPELLE PAS "SPAWN" MAIS ON CHANGERA ÇA
        self.player.move('spawn')
