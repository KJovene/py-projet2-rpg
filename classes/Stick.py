import random
from rich.prompt import Prompt

class Stick:
    def __init__(self, opponent, player):
        self.nb_batons = 21
        self.active_player = random.randint(0, 1) # 0 = opponent, 1 = player
        self.opponent = opponent
        self.player = player
        self.turn_number = 0
    
    def stick_start(self):
        print(f"Que le Jeu du Baton Sacré commence !! Tu ne vas jamais rencontrer mon maître je te le garantis !")
        while self.nb_batons > 0:
            print(f"Le nombre de bâtons restant est de {self.nb_batons}")
            self.active_player = 1 - self.active_player
            self.turn()
            self.leo_chakra()
        return self.end()
    
    def leo_chakra(self):
            if self.nb_batons == 5:
                print(f"{self.opponent}: Je sens que la pression monte !! je concentre tout mon chakra !!!")
            elif self.nb_batons == 1 and self.active_player == 1:
                print(f"{self.opponent}: Quoi ???!!! C'est impossible !!! Je ne peux pas perdre !!!")
    
    def turn(self):
        if self.active_player == 0:
            self.opponent_turn()
        else:
            self.turn_number += 1
            print(f"Tour {self.turn_number}") 
            self.player_turn()
       
    def remove(self, batons_retires):
        if self.nb_batons < batons_retires:
            print("Il n'y a pas assez de bâtons pour retirer autant")
            return False
        self.nb_batons -= batons_retires
        return True
        
    def opponent_turn(self):
        while True:
            batons_retires = random.randint(1, 3)
            if self.remove(batons_retires):
                print(f"{self.opponent} a retiré {batons_retires} bâtons")
                break

    def player_turn(self):
        while True:
            batons_retires = int(Prompt.ask("Combien de bâtons voulez-vous retirer ?", choices=["1", "2", "3"]))
            if self.remove(batons_retires):
                print(f"{self.player.name} a retiré {batons_retires} bâtons")
                break
        
    def end(self):
        if self.active_player == 1:
            print(f"Vous avez perdu... {self.opponent} a gagné le jeu des battons !")
            return False
        else: 
            print(f"La partie est terminée, {self.player.name} a gagné !")
            return True