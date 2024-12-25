"""
GROUPE : KEVIN, LAURENT, ANJARA, MATHIEU

Nous sommes désolé de ne pas avoir découpé le code mais nous avons ajouté beaucoup de commentaires pour vous faciliter la vie.
Vous pouvez appuyer longtemps sur entrer pour passer les dialogues plus rapidement.
"""

from rich.console import Console
from rich.prompt import Prompt
from classes.Stick import Stick
import random
from os import system

console = Console()

# Classe représentant le jeu entier
class Game:
    """
    Représente le jeu entier.
    """
    def __init__(self, name: str):
        """
        Initialise le jeu avec un nom et configure le joueur principal et les lieux.
        
        Args:
            name (str): Le nom du jeu.
        """
        self.name = name
        self.main_player = Player("SAPAL", 0, 0, [], None)



        # Le joueur spawn dans le Tutoriel du jeu
        def spawn_interaction(place):
            naration = [
                ("-", "Vous vous réveillez lentement, déboussolé, vous entendez des bruits peu reconnaissables…"),
                ("-", "Vos yeux s'ouvrent lentement..."),
                ("Vous dans vos pensées", "Où suis-je…? Quels sont ces bruits...?"),
                ("...", f"... ? ... !? {self.main_player.name} !!!?"),
                ("Vous, déboussolé", "Où... Où suis-je..? Et qui êtes-vous..?"),
                ("...", "Ah ! J'ai bien cru que vous étiez mort !"),
                ("Vous, lentement", "Mais qui..."),
                ("...", "Chut ! Laissez-moi me présenter, je me nomme Loic et je serai ton guide tout au long de cette aventure !"),
                ("Vous, encore confus", "Une aventure ? Mais de quoi parlez-vous ?"),
                ("Loic, avec un sourire énigmatique", f"Ah, {self.main_player.name} ! Vous avez tant à découvrir. Vous vous trouvez dans un monde extraordinaire, rempli de magie et de mystères."),
                ("Vous, en vous redressant lentement", "Je ne comprends pas... Comment suis-je arrivé ici ?"),
                ("Loic", "C'est une excellente question, mais malheureusement, je n'ai pas la réponse. Ce que je sais, c'est que vous avez un rôle crucial à jouer dans ce monde."),
                ("Vous, en regardant autour de vous", "Et quel est ce rôle exactement ?"),
                ("Loic", f"Cela, {self.main_player.name}, c'est à vous de le découvrir. Mais ne vous inquiétez pas, je serai là pour vous guider à chaque étape."),
                ("-", "Soudain, un bruit étrange résonne au loin. Loic se tourne brusquement."),
                ("Loic, d'un ton urgent", "Nous devons partir. Ce monde peut être dangereux pour ceux qui ne le connaissent pas. Suivez-moi !"),
                ("-", "Vous hésitez un instant, puis décidez de suivre Loic. Après tout, il semble être votre seul allié dans ce monde étrange."),
                ("-", "Alors que vous vous mettez en route, vous ne pouvez vous empêcher de vous demander ce qui vous attend dans cette mystérieuse aventure...")
            ]

            dialog.dialog(naration)

            # Faux Déplacement dans une zone fictive pour le tutoriel
            dialog.place_changement(self.places["Souflis Forest"].name)
            naration = [
                ["-", "La lumière filtre à travers les arbres d'une forêt dense. L'air est rempli de murmures, comme si les feuilles elles-mêmes chuchotaient des secrets oubliés. Loic marche devant vous, vif et attentif, se retournant de temps en temps pour s'assurer que vous le suivez."],
                ["Loic", f"Bienvenue, {self.main_player.name}, dans la Forêt des Souflis. Cet endroit est unique... et dangereux. Mais c'est aussi ici que commence votre apprentissage."],
                ["-", "Vous regardez autour de vous, observant les racines imposantes et les étranges champignons luminescents qui poussent dans l'obscurité. Vous sentez une présence, comme si la forêt elle-même vous scrutait."],
                ["Vous", "Apprentissage ? Que suis-je censé apprendre ici ?"],
                ["Loic", "Les bases. Comment vous défendre, comment survivre, et comment devenir suffisamment fort pour affronter ce qui vous attend. La quête que vous portez ne sera pas facile. Mais avec chaque épreuve, vous deviendrez plus puissant."],
                ["-", "Soudain, un mouvement furtif attire votre attention. Une petite créature, mi-lapin, mi-reptile, bondit hors d'un buisson. Elle vous fixe avec des yeux curieux."],
                ["Loic", f"Regardez, {self.main_player.name}. La nature vous offre déjà votre premier défi. Ces créatures, les 'Écho-lapins', sont faibles, mais rapides. Attrapez-en un pour commencer. Vous devez vous familiariser avec le maniement de vos compétences."],
                ["Vous", "Mais… je ne sais même pas comment faire ça."],
                ["Loic (riant doucement)", "C'est pourquoi je suis là. Regardez dans votre sac. Vous y trouverez une arme rudimentaire - un bâton, mais suffisant pour débuter. Maintenant, concentrez-vous."],
                ["-", "Vous ouvrez un petit sac en toile suspendu à votre ceinture. Un bâton, usé mais solide, repose à l'intérieur. Vous le saisissez avec hésitation."],
                ["Loic", "Bien. Maintenant, tenez-vous prêt. Ces créatures sont petites, mais elles peuvent mordre si vous n'êtes pas rapide. Concentrez votre énergie sur leur mouvement… et frappez !"],
                ["-", "Un tutoriel interactif commence. Vous apprenez à utiliser les commandes de base pour attaquer."],
            ]
            dialog.dialog(naration)

            #Tutoriel de combat
            tutorielCombat = Combat(self.main_player, Monster(name="Écho-lapin", description="Tutorial Mob", level=1, dropable_items=[Consomable(**self.items["Petite potion rouge"], drop_rate=100)], attack_list=[Attack(name="Cris du fauve", description="Le cris d'un lapin", battle_cry="Miaou 🥺", durability=100, damage=5)]))
            tutorielCombat.start()

            #Présentation de l'objectif principal, drop et xp
            naration = [
                ["Vous", "Je l'ai eu !"],
                ["Loic", f"Très bien, {self.main_player.name}. Chaque créature ici vous offre une leçon. Continuez ainsi, et bientôt, vous serez prêt à affronter bien plus que des lapins."],
                ["-", "Alors que vous continuez votre exploration, Loic vous explique les mécaniques du jeu."],
                ["Loic", "Dans cette forêt, vous allez apprendre les fondamentaux. Voici ce que vous devez savoir pour progresser :\n1 - Expérience et Niveaux : Chaque créature vaincue vous rapporte de l'expérience. Plus vous en accumulez, plus vous montez en niveau, débloquant de nouvelles compétences et renforçant vos capacités."],
                ["Loic", "Dans cette forêt, vous allez apprendre les fondamentaux. Voici ce que vous devez savoir pour progresser :\n2 - Équipement : Vous trouverez des matériaux dans les environs. Utilisez-les pour améliorer votre arme ou vous soigner."],
                ["Loic", "Dans cette forêt, vous allez apprendre les fondamentaux. Voici ce que vous devez savoir pour progresser :\n3 - Quête principale : Vous devrez récupérer 4 clés avant de pouvoir vous confronter au boss final se trouvant a HETIC."],
            ]
            dialog.dialog(naration)

            #Téléportation dans la zone de farm
            self.places["Souflis Forest"].interact(self.main_player)
            self.main_player.move(self.places["Souflis Forest"])

        #Zone Forêt des Souflis, zone de farm
        def souflis_forest_interaction(place):

            #Menu de navigation
            choice = Prompt.ask("Choices :\n1 - Interact with the curent zone\n2 - Open the inventory\n3 - Go to the north (La Foire aux Illusions Perdues)\n4 - Go to the north-east (Domaine des Souflis)\n5 - Go to the east (HETIC)\n6 - Go to the south-east (Le Casino Zoologique)\n7 - Go to the south (Le temple des 1 000 moines)\n", choices=["1","2","3","4","5","6","7"])
            match choice:

                #Le joueur reste dans la Forêt des Souflis
                case "1":

                    #Le monstre que va rencontrer le joueur sera de niveau plus ou moins équivalent à ce dernier
                    player_level = self.main_player.level
                    monster_possibility = [monster_data for monster_data in self.monsters.values() if player_level - 2 <= monster_data["level"] <= player_level + 2 and monster_data["boss"] == False]

                    #Rencontre d'un monstre choisi aléatoirement parmis la liste monster_possibility
                    if monster_possibility :
                        monster_fight = random.choice(monster_possibility)

                        #Appel de la méthode self.start de la Class Combat
                        combat = Combat(self.main_player, Monster(**monster_fight))
                        combat.start()
                    else:
                        combat = Combat(self.main_player, Monster(**self.monsters["Hamid"]))
                        combat.start()
                    place.interact(self.main_player)

                #Le joueur ouvre son inventaire et choisi d'utiliser un objet ou non
                case "2":                  
                    self.main_player.interact_with_inventory()
                    place.interact(self.main_player)
                #Le joueur se déplace au Nord vers le Sanctuaire de Kévin
                case "3":
                    self.main_player.move(self.places["La Foire aux Illusions Perdues"])
                #Le joueur se déplace au Nord-est vers le Sanctuaire de Mathieu
                case "4":
                    self.main_player.move(self.places["Domaine des Souflis"])
                #Le Joueur se déplace à l'Est vers le donjon final HETIC
                case "5":
                    required_keys = ["Clé du casino", "Clé de la fête foraine", "Clé du temple", "Clé du Domaine"]
                    missing_keys = []
                    for key_name in required_keys:
                        if not key_name in [item.name for item in self.main_player.inventory]:
                            missing_keys.append(key_name)
                    if len(missing_keys) == 0:
                        dialog.naration("Vous utilisez vos clefs pour entrer dans Hetic")
                        self.main_player.move(self.places["Hetic"])
                    else:
                        dialog.naration("Vous n'avez pas les clefs nécessaires pour entrer à Hetic")
                        place.interact(self.main_player)
                case "6":
                    self.main_player.move(self.places["Le Casino Zoologique"])
                #Le joueur se déplace au Sud vers le Sanctuaire de Laurent
                case "7":
                    self.main_player.move(self.places["Le temple des 1 000 moines"])
                case _:
                    pass

        #Le joueur arrive devant la Foire aux Illusions perdues
        def la_foire_aux_illusions_perdues_interaction(place):
            #Menu de navigation de la Foire aux Illusions Perdues
            choice = Prompt.ask("Choices :\n1 - Interact with the current zone\n2 - Open the inventory\n3 - Go to the south (Souflis Forest)\n", choices=["1", "2", "3"])
            match choice:
                case "1":
                    naration = [
                        ("-", "Après avoir quitté la dense et mystérieuse Forêt des Souflis, vous arrivez sur un sentier escarpé."),
                        ("-", "En contrebas, un étrange spectacle attire votre attention : un lieu qui ressemble à une fête foraine, bruyant et lumineux, plein de mouvement. Intrigué, vous descendez le sentier sinueux, curieux d'explorer cet endroit qui semble détonner dans cette nature sauvage."),
                        ("-", "Mais plus vous approchez, plus les détails vous troublent : la 'fête foraine' semble minuscule comparée à ce que vous aviez vu de loin. Quelques tentes délabrées, des attractions à moitié effondrées, et une ambiance bien plus lugubre qu'invitante. Vous ressentez un frisson désagréable."),
                        ("-", "Soudain, une vieille femme surgit de l'ombre et vous agrippe le bras avec une poigne étonnamment ferme pour son âge."),
                        ("Vieille Femme", "Alors, jeune âme téméraire… que fais-tu ici, perdu au milieu de nulle part ?"),
                        ("Vous", "Je me suis égaré après avoir quitté la Forêt des Souflis."),
                        ("Vieille Femme", "Oh, comme c'est mignon. Mais tu as de la chance d'être tombé sur moi, car je peux t'aider. Cependant, tout a un prix ici... Je vais te proposer des objets et tu devras en choisir un."),
                        ("Vieille Femme", "Chacun de ces objets a des avantages uniques pour la suite de ton aventure. Mais choisis bien, car tu ne pourras jamais revenir en arrière.")
                    ]

                    dialog.dialog(naration)
                    #La voyante demande au joueur de choisir son malus
                    choice = Prompt.ask("Choisissez un objet :\n1 - Les boucles d'oreilles de la mère de Mathieu\n2 - Le bonnet légendaire de Laurent\n3 - Un orbe magique scintillant\n", choices=["1","2","3"])
                    monster = Monster(**self.monsters["Kevin"])
                    match choice:
                        #Le boss vole 20 PV au joueur
                        case "1":
                            monster.stat["health"] += 20
                            monster.max_hp += 20
                            self.main_player.stat["health"] -= 20
                        #Le boss vole 20 d'attaque au joueur
                        case "2":
                            monster.stat["defense"] += 20
                            self.main_player.stat["attack"] -= 20
                        #Le boss vole 20 de défense au joueur
                        case "3":
                            monster.stat["defense"] += 20
                            self.main_player.stat["defense"] -= 20
                        case _:
                            pass

                    naration = [
                        ("-", "Vous hésitez, mais finissez par faire un choix. La vieille femme esquisse un sourire énigmatique avant de disparaître dans un nuage de fumée."),
                        ("-", "Une fois la femme disparue, vous ressentez un étrange frisson. En fouillant votre inventaire, vous réalisez que l'objet choisi n'est pas là. Pire encore, vous sentez une partie de votre force vous quitter. Les statistiques que vous venez de perdre semblent avoir été volatilisées dans l'air… ou transférées à quelqu'un d'autre."),
                        ("-", "Malgré cette expérience troublante, vous continuez votre chemin et entrez dans ce qui reste de la fête foraine. Mais l'ambiance y est complètement différente de ce que vous aviez perçu de loin : tout est inerte, silencieux. Plus un bruit, plus un mouvement. Les lumières des attractions vacillent, les ombres dansent, et un sentiment d'abandon vous envahit. Vous frissonnez à nouveau."),
                        ("-", "Une lumière vive attire votre attention. Vous vous retournez et découvrez une grande structure, effrayante et imposante : le Palais des Glaces. Le bâtiment semble presque vivant, et une énergie sinistre s'en dégage. Vous comprenez que c'est votre seule option pour avancer. Résolu, vous pénétrez dans ce lieu étrange, vos pas résonnant dans un silence oppressant."),
                        ("-", "L'intérieur est encore plus déroutant : des miroirs déformants renvoient des images grotesques et inquiétantes de vous-même. Chaque reflet semble amplifié, chaque pas résonne comme un coup de tonnerre. Alors que vous progressez dans ce labyrinthe brillant et oppressant, un rire lointain résonne soudain. Il est à la fois malveillant et amusé, semblant venir de partout à la fois."),
                        ("???", "Bienvenue dans MON domaine, intrus."),
                        ("-", "Vous tournez frénétiquement la tête, cherchant l'origine de cette voix, mais tout ce que vous voyez, ce sont des ombres mouvantes et des éclats de lumière. Soudain, une silhouette bondit devant vous. Un homme masqué, vêtu comme un clown sinistre, avec un immense marteau posé nonchalamment sur son épaule."),
                        ("Kévin", "Tu crois pouvoir défier le Souverain des Rires Perdus ? HAHAHA ! Prépare-toi à souffrir, petit joueur. Ce lieu est mon royaume, et ici, je fixe les règles."),
                        ("-", "Kévin brandit son marteau et se jette sur vous. Vous esquivez de justesse et comprenez que vous n'avez pas d'autre choix que de vous battre.")
                    ]

                    dialog.dialog(naration)

                    #Lancement du Combat contre Kévin, le Boss du donjon
                    combat = Combat(self.main_player, monster)
                    

                    #Si le combat est gagné, le joueur drop l'artefact (Petit canard +20PV max)
                    if combat.start():
                        naration = [ 
                            ("-", "Kévin s'écroule au sol, haletant, son masque tombant pour révéler un visage fatigué mais amusé."),
                            ("Kevin", "Hahaha… ça faisait longtemps que je n'avais pas perdu… Bien joué, étranger. Tu as prouvé ta valeur. Prends ce trésor, il pourrait t'être utile."),
                            ("-", "Vous découvrez un coffre à moitié ouvert au fond de la pièce. À l'intérieur, un canard en plastique jaune semble vous attendre. Sous le canard, un numéro mystérieux est gravé.")
                        ]
                        dialog.dialog(naration)
                    else:
                        match choice:
                            #Le boss vole 20 PV au joueur
                            case "1":
                                pass
                            #Le boss vole 20 d'attaque au joueur
                            case "2":
                                self.main_player.stat["attack"] += 20
                            #Le boss vole 20 de défense au joueur
                            case "3":
                                self.main_player.stat["defense"] += 20
                            case _:
                                pass
                        return place.interact(self.main_player)

                    #Retour à l'entrée de la Foire // Ouvre le menu d'intéraction
                    place.interact(self.main_player)
                case "2":
                    self.main_player.interact_with_inventory()
                    place.interact(self.main_player)
                case "3":
                    self.main_player.move(self.places["Souflis Forest"])
                case _:
                    pass

        #Le joueur arrive devant le Domaine des Souflis
        def domaine_des_souflis_interaction(place):
            #Menu de navigation du Domaine des Souflis
            choice = Prompt.ask("Choices :\n1 - Interact with the curent zone\n2 - Open the inventory\n3 - Go to the south-west (Domaine des Souflis)\n", choices=["1","2","3"])
            match choice:
                case "1": # Lancement du donjon
                    naration = [
                        ("-", "Vous franchissez les portes massives du Domaine des Souflis. Le lieu est à la fois majestueux et intimidant, avec des sculptures imposantes et des fresques murales racontant des légendes anciennes. Au centre, une immense salle trône sous un ciel artificiel éclairé par des cristaux lumineux. Vous ressentez une étrange tension dans l'air, comme si chaque pierre murmurait des avertissements."),
                        ("Loic", f"Nous sommes arrivés, {self.main_player.name}. Voici le Domaine des Souflis. Mais restez sur vos gardes… Nous ne sommes pas seuls."),
                        ("-", "Soudain, un bruit sourd résonne. Une silhouette imposante s'avance, sortant de l'ombre. C'est Anjalou, le fils du maître du Casino Zoologique, Anjara, et actuel protecteur de Mathieu Souflis."),
                        ("-", f"{self.main_player.name} entre dans la maison et glisse légèrement sur le sol bien poli. Anjalou apparaît soudainement, vêtu d'un costume élégant, son crâne parfaitement lustré. Il lève les yeux et ajuste son chapeau avec un air supérieur."),
                        ("Anjalou", "Ah, mon cher, vous avez enfin décidé de faire acte de présence. Mais faites attention, ce sol n'est pas là pour être sali !"),
                        ("-", f"Anjalou jette un coup d'œil à {self.main_player.name}, inspecte son propre reflet dans un miroir et se recoiffe en attendant sa réponse."),
                        ("Anjalou (S'approchant)", "Je suis Anjalou, le garde du corps du Seigneur Souflis. Si vous avez l'intention de vous aventurer plus loin, je conseille vivement de respecter le code de la mode et de l'élégance... ainsi que de vous préparer à affronter le véritable luxe.")
                    ]
                    dialog.dialog(naration)
                    #Lancement du combat intermédiaire contre Anjalou
                    combat = Combat(self.main_player, Monster(**self.monsters["Anjalou"]))
                    

                    if combat.start():
                        return place.interact(self.main_player)

                    naration = [
                        ("-", f"Anjalou, en plein combat, esquive avec grâce avant de s'arrêter un instant pour polir son crâne. Puis, d'un coup, {self.main_player.name} réussit à le déstabiliser avec un coup décisif. Anjalou tombe à genoux, un dernier éclat de lumière se reflétant sur son crâne brillant."),
                        ("Anjalou", "Même la perfection doit un jour céder... Mais... mon crâne... il était encore si... éclatant..."),
                        ("-", "Il s'effondre doucement, lissant encore une fois son crâne avant de sombrer dans l'obscurité."),
                        ("-", "Vous entrez dans une pièce richement décorée. Au fond, un homme se tient là, entouré de tableaux et de meubles luxueux. Il porte des habits amples et une attitude décontractée, mais quelque chose semble étrange, comme s'il dissimulait une puissance inouïe derrière cette apparence tranquille."),
                        ("Mathieu", "Ah, un nouveau venu... Vous devez vous demander pourquoi un homme tel que moi se trouve ici, non ? Ne vous inquiétez pas, ce n'est pas la richesse qui vous intéressera ici. Vous vous apprêtez à rencontrer la véritable force."),
                    ]
                    dialog.dialog(naration)

                    #Lancement du combat contre le boss du donjon Mathieu
                    combat = Combat(self.main_player, Monster(**self.monsters["Mathieu"]))

                    if combat.start():
                        return place.interact(self.main_player)

                    naration = [
                        ("-", f"Après une bataille intense, Mathieu se tient encore debout, son corps gravement blessé, mais une lueur de défi dans ses yeux. Il soulève son bras et regarde {self.main_player.name} avec une expression résolue."),
                        ("Mathieu", "Vous pensiez que la richesse était ma véritable arme ? Vous vous êtes trompé. J'ai plus que ça sous cette couche de confort."),
                        ("-", "Il lève son poing, prêt à frapper une dernière fois, mais vous lui donnez un coup fatal avant qu'il ne puisse attaquer. Son corps s'effondre lentement sur le sol, son sourire s'effaçant doucement, mais une lueur de respect dans ses yeux."),
                        ("Mathieu", "La... puissance... est... tout..."),
                    ]
                    dialog.dialog(naration)

                    #Retour devant le Domaine des Souflis
                    place.interact(self.main_player)
                case "2":
                    self.main_player.interact_with_inventory()
                    place.interact(self.main_player)
                case "3":
                    self.main_player.move(self.places["Souflis Forest"])
                case _:
                    pass

        def le_casino_zoologique_interaction(place): #Toujours changer le nom de cette zone
            choice = Prompt.ask("Choices :\n1 - Interact with the curent zone\n2 - Open the inventory\n3 - Go to the North (La Foret des Souflis)\n", choices=["1","2","3"])
            match choice:
                case "1": # Lancement d'un combat + re envoi de l'interface a la fin du combat'
                    naration = [
                        ("-", "Après avoir traversé la jungle dense et sauvage, vous découvrez enfin une clairière dissimulée par une végétation luxuriante. Une lumière vacillante brille à travers les feuillages : c'est l'entrée du mystérieux Casino Zoologique. Une arche massive faite de lianes et de bois sculpté marque le passage vers ce lieu de vice et de hasard."),
                        ('-', "Deux imposants gorilles en costards, bras croisés, montent la garde devant une porte dorée ornée de pierres précieuses. Leur allure imposante et leur regard perçant suffisent à dissuader quiconque de s'approcher imprudemment."),
                        ("Garde Gorille 1 (ton grave et méfiant)", "Hé toi, petit humain. Bienvenue au Casino Zoologique, le repaire des âmes audacieuses."),
                        ("Garde Gorille 2 (d'un ton moqueur) ", "Connaîtras-tu la lumière de la gloire ou te perdras-tu dans l'obscurité ? Héhéhé…"),
                        ('-', "Vous semblez hésitant face à ces deux colosses, mais vous affichez votre détermination."),
                        ("Garde Gorille 1 (impressionné, mais narquois)", "Tu viens pour défier le Roi ? Tu as du cran, mais ne crois pas que ce sera aussi simple."),
                        ("Garde Gorille 2", "On pourrait juste te casser en deux, mais… les règles du casino sont claires. Ici, seule la chance décide de ton sort."),
                        ("Garde Gorille 1", "Voici notre test : ce dé pipé. Tout ce que tu as à faire, c'est obtenir un 12. Simple, non ?"),
                        ("Garde Gorille 2", "Bonne chance, humain… ou devrais-je dire, bonne patience. Tant que tu n'y arrives pas, tu restes là. Mwahaha !")
                    ]
                    dialog.dialog(naration)

                    number = 0

                    while number != 12:
                        choice = int(Prompt.ask("Choisissez une action :\n1 - Lancer un dé\n2 - Abandonner", choices=["1","2"]))
                        if choice == 1:
                            number = random.randint(0, 12)
                            dialog.talk("-", f"Vous lancez un dé et tombez sur le numéro {number}")
                            if number != 12:
                                dialog.talk("Garde Gorille 1", "Hahaha, tu as raté ! Ré essaie si tu l'oses...")
                        else: # Choice == 2
                            dialog.talk("Garde Gorille 1", "Pff, comme prévu. Aucun humain ne peut rivaliser avec la jungle. Rentre chez toi, gamin.")
                            return place.interact(self.main_player)

                    naration = [
                        ("Garde Gorille 1 (étonné)", "Quoi ?! Tu as obtenu un 12 ? Eh bien, il semble que tu sois béni par la chance aujourd'hui."),
                        ("Garde Gorille 2", "Bonne chance avec le Roi. Il n'est pas aussi gentil que nous… Hé hé."),
                        ("-", "Une fois à l'intérieur, un monde flamboyant s'offre à vous : des chandeliers dorés suspendus au plafond, des tables de jeu illuminées par des néons verts et rouges, et une foule de primates en effervescence. Les chimpanzés, habillés comme des croupiers, font tourner les tables, tandis que des lémuriens occupés comptent des piles de jetons dans un coin sombre."),
                        ("-", "Au centre de la salle, sur un trône taillé dans un tronc d'arbre massif et recouvert de fourrure, trône le Roi Anjara. C'est un gorille massif au pelage d'un noir brillant, vêtu d'une cape en velours rouge. Un cigare pend mollement à sa lèvre, et une pile de cartes est posée à ses côtés."),
                        ("Roi Anjara (voix rauque et dominante)", "Qui ose troubler la paix de mon royaume ?"),
                        ("-", "Il vous dévisage avec intensité, puis se redresse lentement, écrasant son cigare dans une coupe dorée."),
                        ("Roi Anjara", "Ah, un humain… Tu veux te mesurer à moi ? Sache que je ne joue pas seulement avec les cartes, mais avec les destins. Prépare-toi, car ici, la triche est une vertu et la chance, un art.")
                    ]

                    dialog.dialog(naration)

                    combat = Combat(self.main_player, Monster(**self.monsters["Le Roi Singe"]))

                    if combat.start():
                        return place.interact(self.main_player)

                    place.interact(self.main_player)
                case "2":
                    self.main_player.interact_with_inventory()
                    place.interact(self.main_player)
                case "3":
                    self.main_player.move(self.places["Souflis Forest"])
                case _:
                    pass

        def le_temple_des_1000_moines_interaction(place):
            choice = Prompt.ask("Choices :\n1 - Interact with the curent zone\n2 - Open the inventory\n3 - Go to the North (La Foret des Souflis)\n", choices=["1","2","3"])
            match choice:
                case "1": # Lancement d'un combat + re envoi de l'interface a la fin du combat'
                    naration = [
                        ("-", "Vous arrivez au pied de la montagne qui abrite le légendaire Temple des 1000 Moines. Une double porte imposante en bois rouge écarlate se dresse devant vous, marquant l'entrée de ce sanctuaire ancien. Alors que vous vous approchez, les portes s'ouvrent lentement dans un grincement solennel. Une silhouette élancée se détache dans l'ombre du seuil."),
                        ('Leo', "Mes respects, jeune héros. Je suis Leo, humble serviteur de ce temple sacré. Bienvenue au sanctuaire du Temple des 1000 Moines."),
                        ("Leo (s'inclinant légèrement)", "Mon maître, Lao Ren, vous attendait avec impatience. Il dit que vous êtes l'Élu destiné à libérer la Forêt des Souflis de l'emprise de la guilde HETIC. Cependant…"),
                        ("Leo (serrant fortement un petit baton)", "…je dois m'assurer que vous êtes digne de rencontrer mon maître. Préparez-vous, jeune scarabée, car seul un esprit affûté peut franchir cette porte !"),
                    ]
                    dialog.dialog(naration)
                    # Jeu du baton contre pour entrer dans le temple
                    stick_game = Stick("Disciple Léo", self.main_player)
                    if not stick_game.stick_start():
                        return place.interact(self.main_player)
                    naration = [
                        ("-", "Vous avez réussi à battre Léo dans un jeu de bâton. Il vous adresse un sourire chaleureux et vous invite à entrer dans le temple."),
                        ("-", "Vous gravissez péniblement l'escalier interminable. À chaque marche, la végétation luxuriante de la forêt des Souflis s'éloigne, offrant une vue à couper le souffle sur le paysage environnant. Enfin, au sommet, le temple se dévoile, majestueux. Les trois pavillons principaux scintillent sous le soleil, leurs toits dorés étincelant comme des joyaux. Les murs extérieurs racontent, à travers des fresques, l'histoire des 1000 moines qui atteignirent l'illumination en ces lieux.\nAlors que vous avancez, une voix grave et profonde résonne dans le vent, semblant provenir de toutes les directions à la fois."),
                        ("-", "Vous entendez une voix omniprésente. \"Vous avez donc réussi le défi de mon disciple… Suivez ma voix, héros, et venez à ma rencontre.\""),
                        ("-", "Vous atteignez la cour centrale, où le vent se fait plus vif. Soudain, un nuage de fumée s'élève devant vous. De cette brume émerge Lao Ren, le Gardien du Temple des 1000 Moines. Grand et imposant, vêtu d'un habit de soie orné de motifs dorés, il tient un bâton gravé de symboles mystiques."),
                        ("Maître Lao Ren", "Sacheburidana, héros-sama. Je sais pourquoi vous êtes là."),
                        ("-", "Le maître, vous salue lentement, puis plante son bâton au sol avec force."),
                        ("Maître Lao ren", "Mais avant d'accepter de vous remettre la relique sacrée, il est de mon devoir de tester votre force et votre volonté. Ne perdons pas de temps... Affrontez-moi !")
                    ]
                
                    dialog.dialog(naration)
                    combat = Combat(self.main_player, Monster(**self.monsters["Lao-ren"]))

                    if combat.start():
                        return place.interact(self.main_player)
                    place.interact(self.main_player)
                    
                case "2":
                    self.main_player.interact_with_inventory()
                    place.interact(self.main_player)
                case "3":
                    self.main_player.move(self.places["Souflis Forest"])
                case _:
                    pass

        def hetic_interaction(place):
          choice = Prompt.ask("Choices :\n1 - Interact with the curent zone\n2 - Open the inventory\n3 - Go to the North (La Foret des Souflis)\n", choices=["1","2","3"])

          match choice:
            case "1": # Lancement d'un combat + re envoi de l'interface a la fin du combat'
                #Arrivée à Hetic
                naration = [
                    ("-", "Vous arrivez au bout du long chemin vous menant à la sombre façade d'un batiment."),
                    ("-", "Vous observez un grand portail, puis prenant votre courage à deux mains, vous utilisez vos forces pour ouvir cette porte. Vous avancez dans une grande cour rempli de brouillard et apercevez un silouhette."),
                    ("Alexandre","Eh bien...on dirait que les singes et les moines ne sont plus aussi féroce qu'avant"),
                    ("-", "Cet entrepreneur vous analyse entièrement, et semble se préparer à agir"),
                    ("Alexandre", "Allez, finis de jouer. Tu vas payer pour toutes les conférences que tu as ratées, y'avait pas un monde où tu n'y étais pas.")
                ]
                dialog.dialog(naration)
                combat = Combat(self.main_player, Monster(**self.monsters["Alexandre"]))
                if not combat.start():
                    place.interact(self.main_player)
                naration = [
                    ("Alexandre", "Mais...coment un mortel peut détenir autant de puissance? Tu as donc réuni tous les outils pour trouver une alternance?"),
                    ("-", "Votre combat bat son plein contre le grand chef heticien. Soudain une brume épaisse apparaît, et une silouhette encore plus grande apparait. Vous sentez une nouvelle présence dans la cour..."),
                    ("-", "Alexandre disparait peu à peu, et vous apercevez un homme vêtu d'un superbe costume bleu."),
                    ("Nabil", "Sacrilège, je ne peux donc plus compter sur ce bon vieux Alexandre. EH OUI ! C'est bien moi Nabil Lmrabet, celui qui tire les ficelles derrière tout ce qui se passe dans ce monde. Aller humain, montre moi tout ce que ton voyage t'as appris, ou péris dans les entrailles de mon école.")
                ]
                dialog.dialog(naration)
                combat = Combat(self.main_player, Monster(**self.monsters["Nabil"]))
                if not combat.start():
                    place.interact(self.main_player)
                
                if combat:
                    naration = [
                        ("Nabil", "Impossible... Comment as-tu pu me vaincre ?!"),
                        ("-", "Vous regardez autour de vous, le silence règne. Vous avez réussi. Vous avez vaincu tous les obstacles et triomphé de tous les ennemis."),
                        ("-", "Vous ressentez un mélange de soulagement et de fierté. Vous avez accompli votre quête."),
                        ("-", "Alors que vous vous apprêtez à quitter les lieux, une lumière éclatante vous entoure. Vous êtes téléporté dans un endroit familier."),
                        ("Loic", "Félicitations, {self.main_player.name}. Vous avez réussi là où tant d'autres ont échoué. Vous êtes un véritable héros."),
                        ("-", "Vous souriez, sachant que votre aventure est terminée, mais que de nouvelles quêtes vous attendent peut-être à l'avenir."),
                    ]
                    dialog.dialog(naration)
                    return self.end()
                else:
                    return place.interact(self.main_player)
                
            case "2":
                self.main_player.interact_with_inventory()
                place.interact(self.main_player)
            case "3":
                self.main_player.move(self.places["Souflis Forest"])
            case _:
                pass


        # Initialisation des places sans les connexions
        spawn = Place(name="Spawn", description="Le point de départ du joueur", monsters=[], interaction=spawn_interaction)
        souflis_forest = Place(name="Souflis Forest", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=souflis_forest_interaction)
        la_foire_aux_illusions_perdues = Place(name="La Foire aux Illusions Perdues", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=la_foire_aux_illusions_perdues_interaction)
        domaine_des_souflis = Place(name="Le domaine des Souflis", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=domaine_des_souflis_interaction)
        casino = Place(name="Le Casino Zoologique", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=le_casino_zoologique_interaction)
        temple = Place(name="Le temple des 1 000 moines", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=le_temple_des_1000_moines_interaction)
        hetic = Place(name="Hetic", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=hetic_interaction)
        # Connexions entre les places
        spawn.places_around = {"east": souflis_forest}
        souflis_forest.places_around = {
            "west": spawn,
            "north": la_foire_aux_illusions_perdues,
            "north-east": domaine_des_souflis,
            "east": hetic,
            "south-east": casino,
            "south": temple,
        }
        la_foire_aux_illusions_perdues.places_around = {"south": souflis_forest}
        domaine_des_souflis.places_around = {"south-west": souflis_forest}
        casino.places_around = {"west": souflis_forest}
        temple.places_around = {"north-west": souflis_forest}
        hetic.places_around = {"west": souflis_forest}

        spawn.interaction = spawn_interaction
        souflis_forest.interaction = souflis_forest_interaction
        la_foire_aux_illusions_perdues.interaction = la_foire_aux_illusions_perdues_interaction
        domaine_des_souflis.interaction = domaine_des_souflis_interaction
        casino.interaction = le_casino_zoologique_interaction
        temple.interaction = le_temple_des_1000_moines_interaction
        hetic.interaction = hetic_interaction

        # Stockage des places
        self.places = {
            "Spawn": spawn,
            "Souflis Forest": souflis_forest,
            "La Foire aux Illusions Perdues": la_foire_aux_illusions_perdues,
            "Domaine des Souflis": domaine_des_souflis,
            "Le Casino Zoologique": casino,
            "Le temple des 1 000 moines": temple,
            "Hetic": hetic,
        }

        self.attacks = {
            "Bois de boulogne": {"name": "Bois de boulogne", "description": "Je me souvient de ma forêt natale..", "battle_cry": "YAAAAAAH", "durability": -1, "damage": 65},
            "Course rapide": {"name": "Course rapide", "description": "Je cours très très vite !!!", "battle_cry": "HYPER VITESSE !!!!", "durability": -1, "damage": 60},
            "Souplesse du judoka": {"name": "Souplesse du judoka", "description": "Avec la fluidité et la puissance d'un Teddy Riner prime, projette l'adversaire au sol avec une grâce impeccable", "battle_cry": "Go muscu", "durability": -1, "damage": 60},
            "Poing de feu": {"name": "Poing de feu", "description": "Poing littéralement enflammé", "battle_cry": "Brule en enfer", "durability": -1, "damage": 55},
            "Coup de tonerre": {"name": "Coup de tonerre", "description": "Appelle la foudre de façon mystique", "battle_cry": "Ça va piquer", "durability": -1, "damage": 55},
            "Grattage du délégué": {"name": "Grattage du délégué", "description": "Faut bien s'entourer...", "battle_cry": "Donne moi tes hp", "durability": -1, "damage": 50},
            "Lancé de talon": {"name": "Lancé de talon", "description": "Lance un talon mais ce n'est pas une chaussure..", "battle_cry": "Prend toi mon talon", "durability": -1, "damage": 45},
            "Griffure": {"name": "Griffure", "description": "Des ongles t'as peur", "battle_cry": "Roarrrr", "durability": -1, "damage": 40},
            "Explosion": {"name": "Explosion", "description": "Boom", "battle_cry": "Araaaaa", "durability": -1, "damage": 40},
            "Vol rapide": {"name": "Vol rapide", "description": "UN HUMAIN QUI VOLE", "battle_cry": "Bismilah", "durability": -1, "damage": 35},
            "Charme": {"name": "Charme", "description": "L'amour est plus fort que tout", "battle_cry": "Mouah 💋", "durability": -1, "damage": 35},
            "Chant brutal": {"name": "Chant brutal", "description": "Pas mal d'Octaves dans la voix", "battle_cry": "Dès que je chanterais tu deviendras sourd.", "durability": -1, "damage": 30},
            "Kamehameha": {"name": "Kamehameha", "description": "Pouvoir totalement originaire d'ici", "battle_cry": "Redonne mon couscous", "durability": -1, "damage": 30},
            "Malaka": {"name": "Malaka", "description": "Il fait chaud là bas", "battle_cry": "Mange mon grec", "durability": -1, "damage": 25},
            "Control Mental": {"name": "Control Mental", "description": "Contrôle seulement le petit doigt de l'adversaire", "battle_cry": "Au hazard", "durability": -1, "damage": 25},
            "Gear 5": {"name": "Gear 5", "description": "Pouvoir totalement créer dans la forêt des souflis", "battle_cry": "Youhouu", "durability": -1, "damage": 20},
            "Ultra tarte": {"name": "Ultra tarte", "description": "Une énormé baffe", "battle_cry": "ET BIIIIIM", "durability": -1, "damage": 20},
            "Balayette laser": {"name": "Balayette laser", "description": "La gravité reste la force la plus faible des 4 que compose l'univers..", "battle_cry": "Tête AU SOL", "durability": -1, "damage": 15},
            "Force de mouche": {"name": "Force de mouche", "description": "P'tit coup de pression", "battle_cry": "Attention ça va faire mal !!!", "durability": -1, "damage": 15},
            "Contre-argument": {"name": "Contre-argument", "description": "La violence ne résoud rien..", "battle_cry": "La violence verbale est la plus grande des violence..", "durability": -1, "damage": 10},
            "Marteau du Forain": {"name": "Marteau du Forain", "description": "Un marteau venant d'une des plus grandes forges roumaine de l'humanité", "battle_cry": "Kévin abat son marteau avec fracas, déclenchant une onde de choc qui fait vibrer les miroirs autour de vous.", "durability": -1, "damage": 30},
            "Billes de Loterie Explosives": {"name": "Billes de Loterie Explosives", "description": "Des billes de fabrication chinoise..peut être ?", "battle_cry": "Il lance une poignée de billes colorées qui explosent en gerbes de lumière aveuglante.", "durability": -1, "damage": 28},
            "Claque de la Poigne Gigantesque": {"name": "Claque de la Poigne Gigantesque", "description": "Une main qui mériterait d'être un panneau stop", "battle_cry": "Il prépare une claque chargée, des veines lumineuses pulsent sur la main, et un bruit sourd de tension monte dans l'air. L'impact crée une onde de choc qui soulève poussière et débris tout autour.", "durability": 1, "damage": 40},
            "Le Lasso de Soie": {"name": "Le Lasso de Soie", "description": "Anjalou utilise un lasso en soie fine, qu'il fait briller comme une étoile. Il l'envoie avec élégance pour attraper ses ennemis et les ramener vers lui avec un mouvement fluide et gracieux.", "battle_cry": "TU M'ES ACCROCHÉ… ET J'AI UN CRÂNE À PRÉSERVER !", "durability": -1, "damage": 30},
            "La Roulade du Gentleman": {"name": "La Roulade du Gentleman", "description": "Anjalou effectue une roulade parfaitement chorégraphiée, évitant les attaques ennemies tout en décochant un coup de pied agile, comme un maître de danse.", "battle_cry": "UNE DANSE AU RYTHME DU STYLE !", "durability": -1, "damage": 35},
            "Le Vent du Chapeau": {"name": "Le Vent du Chapeau", "description": "Anjalou effectue un mouvement rapide, et son chapeau élégant se transforme en un projecteur de lumière qui éblouit temporairement les ennemis autour de lui.", "battle_cry": "MON STYLE, MA PUISSANCE !", "durability": -1, "damage": 40},
            "Le Crâne de Lumière": {"name": "Le Crâne de Lumière", "description": "Anjalou se tient droit, prend une pause pour s'assurer que son crâne est parfaitement poli, puis libère une lumière aveuglante depuis son crâne chauve, envoyant une onde d'énergie brillante dans toute la zone. L'onde déstabilise ses ennemis, tout en rétablissant l'éclat de son apparence avec une touche de perfection.", "battle_cry": "VOUS NE POUVEZ PAS FAIRE CONCURRENCE AVEC LE CRÂNE DU MAÎTRE !", "durability": 1, "damage": 55},
            "Le Marteau de la Banque": {"name": "Le Marteau de la Banque", "description": "Mathieu fait apparaître un énorme marteau doré en forme de lingot et le balance violemment sur le sol, créant une onde de choc étincelante.", "battle_cry": "TA BOURSE NE VA PAS AIMER ÇA !", "durability": -1, "damage": 70},
            "Le Lancer de Pièce Fétiche": {"name": "Le Lancer de Pièce Fétiche", "description": "Il saisit une pièce dorée et la propulse à une vitesse fulgurante, frappant l'ennemi directement entre les yeux.", "battle_cry": "C'EST À MOI QUE TU LA DOIS, LA MONNAIE !", "durability": -1, "damage": 60},
            "Le Coup du Pantalon Traître": {"name": "Le Coup du Pantalon Traître", "description": "Mathieu arrache un pan de ses vêtements et le fait tournoyer, créant un vent si puissant qu'il emporte ses adversaires.", "battle_cry": "CES FRINGUES NE SONT PAS JUSTE POUR LE STYLE !", "durability": -1, "damage": 50},
            "L'Écran Noir de la Dette": {"name": "L'Écran Noir de la Dette", "description": "Mathieu tend les bras, et un immense écran translucide apparaît au-dessus de l'arène, projetant une lumière éblouissante. Sur cet écran, une facture gigantesque s'affiche avec des chiffres astronomiques qui clignotent, plongeant ses ennemis dans une terreur indescriptible.", "battle_cry": "ET SI TU PAYAIS TES IMPÔTS ?!", "durability": 1, "damage": 100},
            "Low Kick du Kangourou": {"name": "Low Kick du Kangourou", "description": "Le tibia est une partie du corps très dure mais très sensible..", "battle_cry": "AYAAAH", "durability": -1, "damage": 100},
            "Bouclier du lémurien": {"name": "Bouclier du lémurien", "description": "Un bouclier venant tout droit du WAKANDA", "battle_cry": "WAKANDA POUR TOUJOURSSS!!!", "durability": -1, "damage": 120},
            "Déferlante de la jungle": {"name": "Déferlante de la jungle", "description": "Une bonne tempête tropicale comme on les aime..", "battle_cry": "Un brin d'air !", "durability": 1, "damage": 150},
            "Coup du Lotus Brisé": {"name": "Coup du Lotus Brisé", "description": "Un coup puissant et ciblé, imitant l'éclosion brutale d'un lotus.", "battle_cry": "Repose en paix...", "durability": -1, "damage": 350},
            "Sillage d'Encens": {"name": "Sillage d'Encens", "description": "Une série de mouvements fluides libérant une fumée toxique qui entrave les adversaires.", "battle_cry": "Fumer tue.", "durability": -1, "damage": 250},
            "Colère des 1000 Âmes": {"name": "Colère des 1000 Âmes", "description": "Le boss invoque les esprits des moines qui l'entourent pour déchaîner une tempête spirituelle dévastatrice.", "battle_cry": "TOUS TES MORTS SONT CONTRE TOI !", "durability": 1, "damage": 500},
            "Attaque légère" : {"name" : "Attaque légère", "description": "Attaque de base rapide et préçise", "battle_cry": "Ah c'est légeeeeeeer", "durability": -1, "damage": 10},
            "Attaque lourde" : {"name": "Attaque lourde", "description": "Attaque de base lourde", "battle_cry": "Ah c'est Louuuuuuurd", "durability": 2, "damage": 20},
            "Le cheat de Loic" : {"name": "Le cheat de Loic", "description": "/kill, pas le temps, faut corriger...", "battle_cry": "FAUT QUE JE CORRIGE VITE... HETIFICATION !!", "durability": -1, "damage": 486486486486}
        }

        self.items = {
            "Clé du casino": {"name": "Clé du casino", "description": "Cette clé t'aidera à accéder au boss final !", "effect": {}},
            "Clé de la fête foraine": {"name": "Clé de la fête foraine", "description": "Cette clé t'aidera à accéder au boss final !", "effect": {}},
            "Clé du temple": {"name": "Clé du temple", "description": "Cette clé t'aidera à accéder au boss final !", "effect": {}},
            "Clé du Domaine": {"name": "Clé du Domaine", "description": "Cette clé t'aidera à accéder au boss final !", "effect": {}},
            "Petite potion rouge": {"name": "Petite potion rouge", "description": "Potion donnée par la déesse Gaïa (soigne 20 PV)", "effect": {"health": 20}},
            "Grande potion rouge": {"name": "Grande potion rouge", "description": "Potion donnée par la déesse Gaïa (soigne 50 PV)", "effect": {"health": 50}},
            "Potion de vie": {"name": "Potion de vie", "description": "Une potion qui soigne 100 PV", "effect": {"health": 100}},
            "Potion de régénération": {"name": "Potion de régénération", "description": "Une potion qui soigne 200 PV", "effect": {"health": 200}},
            "Potion divine": {"name": "Potion divine", "description": "Une potion qui soigne complètement les PV", "effect": {"health": 9999}}
        }

        self.artefact = {
            "Petit canard": {"name": "Petit canard", "description": "Augmente l'HP. Parce que rien ne vaut un bon bain avec un canard en plastique.", "effect": {"health": 50, "attack": 0, "defense": 0}},
            "Écran du Mac": {"name": "Écran du Mac", "description": "Utilisé comme bouclier, c'est le fameux écran du Mac de Mathieu. Attention aux pixels morts !", "effect": {"health": 0, "attack": 0, "defense": 20}},
            "Maxi Phô Boeuf": {"name": "Maxi Phô Boeuf", "description": "Une soupe de nouille dont la recette est restée secrète depuis hier. Un vrai coup de boost pour les guerriers affamés.", "effect": {"health": 0, "attack": 200, "defense": 0}},
            "Jeu de cartes": {"name": "Jeu de cartes", "description": "Jeu de carte truqué. Parfait pour les soirées poker entre amis... ou pour tricher en combat.", "effect": {"health": 0, "attack": 0, "defense": 100}}
        }

        self.monsters = {
            "Amelie": {
            "name": "Amelie",
            "description": "Une créature mystérieuse avec une aura envoûtante.",
            "level": 2,
            "attack_list": [
                Attack(**self.attacks["Force de mouche"], drop_rate=5),
                Attack(**self.attacks["Contre-argument"], drop_rate=5)
            ],
            "dropable_items": [
                Consomable(**self.items["Petite potion rouge"], drop_rate=25),
                Consomable(**self.items["Grande potion rouge"], drop_rate=20),
                Consomable(**self.items["Potion de vie"], drop_rate=3),
                Consomable(**self.items["Potion de régénération"], drop_rate=2),
                Consomable(**self.items["Potion divine"], drop_rate=1)
            ],
            "boss": False
            },
            "Fara": {
            "name": "Fara",
            "description": "Un guerrier redoutable avec une force brute.",
            "level": 4,
            "attack_list": [
                Attack(**self.attacks["Ultra tarte"], drop_rate=5),
                Attack(**self.attacks["Balayette laser"], drop_rate=5)
            ],
            "dropable_items": [
                Consomable(**self.items["Petite potion rouge"], drop_rate=25),
                Consomable(**self.items["Grande potion rouge"], drop_rate=20),
                Consomable(**self.items["Potion de vie"], drop_rate=3),
                Consomable(**self.items["Potion de régénération"], drop_rate=2),
                Consomable(**self.items["Potion divine"], drop_rate=1)
            ],
            "boss": False
            },
            "Imen": {
            "name": "Imen",
            "description": "Un mage puissant maîtrisant les arts mystiques.",
            "level": 6,
            "attack_list": [
                Attack(**self.attacks["Control Mental"], drop_rate=4),
                Attack(**self.attacks["Gear 5"], drop_rate=4)
            ],
            "dropable_items": [
                Consomable(**self.items["Petite potion rouge"], drop_rate=25),
                Consomable(**self.items["Grande potion rouge"], drop_rate=20),
                Consomable(**self.items["Potion de vie"], drop_rate=6),
                Consomable(**self.items["Potion de régénération"], drop_rate=2),
                Consomable(**self.items["Potion divine"], drop_rate=1)
            ],
            "boss": False
            },
            "Nazim": {
            "name": "Nazim",
            "description": "Un combattant agile et rapide comme l'éclair.",
            "level": 8,
            "attack_list": [
                Attack(**self.attacks["Kamehameha"], drop_rate=3),
                Attack(**self.attacks["Malaka"], drop_rate=3)
            ],
            "dropable_items": [
                Consomable(**self.items["Petite potion rouge"], drop_rate=15),
                Consomable(**self.items["Grande potion rouge"], drop_rate=25),
                Consomable(**self.items["Potion de vie"], drop_rate=10),
                Consomable(**self.items["Potion de régénération"], drop_rate=5),
                Consomable(**self.items["Potion divine"], drop_rate=2)
                ],
            "boss": False
            },
            "Nana la renarde": {
            "name": "Nana la renarde",
            "description": "Une renarde rusée avec des charmes envoûtants.",
            "level": 10,
            "attack_list": [
                Attack(**self.attacks["Charme"], drop_rate=3),
                Attack(**self.attacks["Chant brutal"], drop_rate=3)
            ],
            "dropable_items": [
                Consomable(**self.items["Petite potion rouge"], drop_rate=15),
                Consomable(**self.items["Grande potion rouge"], drop_rate=35),
                Consomable(**self.items["Potion de vie"], drop_rate=13),
                Consomable(**self.items["Potion de régénération"], drop_rate=8),
                Consomable(**self.items["Potion divine"], drop_rate=3)
            ],
            "boss": False
            },
            "Youva": {
            "name": "Youva",
            "description": "Un guerrier explosif avec une vitesse fulgurante.",
            "level": 12,
            "attack_list": [
                Attack(**self.attacks["Explosion"], drop_rate=2),
                Attack(**self.attacks["Vol rapide"], drop_rate=2)
            ],
            "dropable_items": [
                Consomable(**self.items["Petite potion rouge"], drop_rate=15),
                Consomable(**self.items["Grande potion rouge"], drop_rate=35),
                Consomable(**self.items["Potion de vie"], drop_rate=13),
                Consomable(**self.items["Potion de régénération"], drop_rate=8),
                Consomable(**self.items["Potion divine"], drop_rate=3)
            ],
            "boss": False
            },
            "Carglass": {
            "name": "Carglass",
            "description": "Un monstre robuste avec des griffes acérées.",
            "level": 14,
            "attack_list": [
                Attack(**self.attacks["Lancé de talon"], drop_rate=2),
                Attack(**self.attacks["Griffure"], drop_rate=2)
            ],
            "dropable_items": [
                Consomable(**self.items["Petite potion rouge"], drop_rate=15),
                Consomable(**self.items["Grande potion rouge"], drop_rate=25),
                Consomable(**self.items["Potion de vie"], drop_rate=15),
                Consomable(**self.items["Potion de régénération"], drop_rate=8),
                Consomable(**self.items["Potion divine"], drop_rate=3)
            ],
            "boss": False
            },
            "Cherif": {
            "name": "Cherif",
            "description": "Un guerrier redoutable avec des attaques électriques.",
            "level": 16,
            "attack_list": [
                Attack(**self.attacks["Coup de tonerre"], drop_rate=2),
                Attack(**self.attacks["Grattage du délégué"], drop_rate=2)
            ],
            "dropable_items": [
                Consomable(**self.items["Petite potion rouge"], drop_rate=15),
                Consomable(**self.items["Grande potion rouge"], drop_rate=25),
                Consomable(**self.items["Potion de vie"], drop_rate=20),
                Consomable(**self.items["Potion de régénération"], drop_rate=8),
                Consomable(**self.items["Potion divine"], drop_rate=3)
            ],
            "boss": False
            },
            "Noa": {
            "name": "Noa",
            "description": "Un judoka puissant avec des poings enflammés.",
            "level": 18,
            "attack_list": [
                Attack(**self.attacks["Souplesse du judoka"], drop_rate=2),
                Attack(**self.attacks["Poing de feu"], drop_rate=2)
            ],
            "dropable_items": [                   
                Consomable(**self.items["Petite potion rouge"], drop_rate=15),
                Consomable(**self.items["Grande potion rouge"], drop_rate=15),
                Consomable(**self.items["Potion de vie"], drop_rate=10),
                Consomable(**self.items["Potion de régénération"], drop_rate=15),
                Consomable(**self.items["Potion divine"], drop_rate=5)
            ],
            "boss": False
            },
            "Hamid": {
            "name": "Hamid",
            "description": "Un guerrier forestier avec une vitesse incroyable.",
            "level": 20,
            "attack_list": [
                Attack(**self.attacks["Bois de boulogne"], drop_rate=2),
                Attack(**self.attacks["Course rapide"], drop_rate=2)
            ],
            "dropable_items": [
                
                Consomable(**self.items["Petite potion rouge"], drop_rate=15),
                Consomable(**self.items["Grande potion rouge"], drop_rate=15),
                Consomable(**self.items["Potion de vie"], drop_rate=10),
                Consomable(**self.items["Potion de régénération"], drop_rate=20),
                Consomable(**self.items["Potion divine"], drop_rate=10)
            ],
            "boss": False
            },
            "Kevin": {
            "name": "Kevin",
            "description": "Souverain des rires perdus, maître des illusions.",
            "level": 5,
            "attack_list": [
                Attack(**self.attacks["Marteau du Forain"], drop_rate=10),
                Attack(**self.attacks["Billes de Loterie Explosives"], drop_rate=10),
                Attack(**self.attacks["Claque de la Poigne Gigantesque"], drop_rate=10)
            ],
            "dropable_items": [(Item(**self.items["Clé de la fête foraine"], drop_rate=100)),Equipable(**self.artefact["Petit canard"])],
            "boss": True
            },
            "Anjalou": {
            "name": "Anjalou",
            "description": "Fils du Roi Singe, élégant et redoutable.",
            "level": 10,
            "attack_list": [
                Attack(**self.attacks["Le Lasso de Soie"], drop_rate=10),
                Attack(**self.attacks["La Roulade du Gentleman"], drop_rate=10),
                Attack(**self.attacks["Le Vent du Chapeau"], drop_rate=10),
                Attack(**self.attacks["Le Crâne de Lumière"], drop_rate=10)
            ],
            "dropable_items": [],
            "boss": True
            },
            "Mathieu": {
            "name": "Mathieu",
            "description": "Riche investisseur avec des attaques dévastatrices.",
            "level": 15,
            "attack_list": [
                Attack(**self.attacks["Le Marteau de la Banque"], drop_rate=10),
                Attack(**self.attacks["Le Lancer de Pièce Fétiche"], drop_rate=10),
                Attack(**self.attacks["Le Coup du Pantalon Traître"], drop_rate=10),
                Attack(**self.attacks["L'Écran Noir de la Dette"], drop_rate=10)
            ],
            "dropable_items": [(Item(**self.items["Clé du Domaine"], drop_rate=100)), Equipable(**self.artefact["Écran du Mac"])],
            "boss": True
            },
            "Le Roi Singe": {
            "name": "Le Roi Singe",
            "description": "Dirigeant de la confrérie singeresque, puissant et sage.",
            "level": 20,
            "attack_list": [
                Attack(**self.attacks["Low Kick du Kangourou"], drop_rate=10),
                Attack(**self.attacks["Bouclier du lémurien"], drop_rate=10),
                Attack(**self.attacks["Déferlante de la jungle"], drop_rate=10)
            ],
            "dropable_items": [(Item(**self.items["Clé du casino"], drop_rate=100)), Equipable(**self.artefact["Jeu de cartes"])],
            "boss": True
            },
            "Lao-ren": {
            "name": "Lao-ren",
            "description": "Maître Shaolin, gardien du temple sacré.",
            "level": 25,
            "attack_list": [
                Attack(**self.attacks["Coup du Lotus Brisé"], drop_rate=10),
                Attack(**self.attacks["Sillage d'Encens"], drop_rate=10),
                Attack(**self.attacks["Colère des 1000 Âmes"], drop_rate=10)
            ],
            "dropable_items": [(Item(**self.items["Clé du temple"], drop_rate=100)), Equipable(**self.artefact["Maxi Phô Boeuf"])],
            "boss": True
            },
          "Alexandre": {
              "name": "Alexandre",
              "description": "Directeur d'HETIC, stratège redoutable.",
              "level": 30,
              "attack_list": [
              Attack(**self.attacks["Coup du Lotus Brisé"], drop_rate=10),
              Attack(**self.attacks["Sillage d'Encens"], drop_rate=10),
              Attack(**self.attacks["Colère des 1000 Âmes"], drop_rate=10)
              ],
            "dropable_items": [],
            "boss": True
          },
          "Nabil": {
              "name": "Nabil",
              "description": "Le porte-parole, manipulateur et puissant.",
              "level": 35,
              "attack_list": [
              Attack(**self.attacks["Coup du Lotus Brisé"], drop_rate=10),
              Attack(**self.attacks["Sillage d'Encens"], drop_rate=10),
              Attack(**self.attacks["Colère des 1000 Âmes"], drop_rate=10)
              ],
            "dropable_items": [],
            "boss": True
          }
        }




    def start(self):
        """
        Démarre le jeu en créant le joueur principal et en initiant la première interaction.
        """
        console.print("[green]Création du personnage...[/green]")
        player_name = Prompt.ask("Quel nom souhaitez-vous donner à votre personnage ? (si vous êtes Loic, veuillez écrire \"Loic\")", default="Joueur")
        system("clear")
        if player_name == "Loic":
            self.main_player = Player(
                name=player_name,
                level=10,
                xp=0,
                attack_list=[Attack(**self.attacks["Attaque légère"]), Attack(**self.attacks["Colère des 1000 Âmes"]),Attack(**self.attacks["Le cheat de Loic"])],
                place= self.places["Spawn"],
                inventory=[Item(**self.items["Clé du casino"]), Item(**self.items["Clé de la fête foraine"]), Item(**self.items["Clé du temple"]), Item(**self.items["Clé du Domaine"])],
            )
        else:
            self.main_player = Player(
                name=player_name,
                level=1,
                xp=0,
                attack_list=[Attack(**self.attacks["Attaque légère"]), Attack(**self.attacks["Attaque lourde"])],
                place= self.places["Spawn"],
                inventory=[],
            )
        console.print(f"[bold blue]Bienvenue dans {self.name}[/bold blue]")
        self.main_player.place.interact(self.main_player)

    def end(self):
        """
        Termine le jeu en affichant un message de fin.
        """
        console.print("[bold green]Merci d'avoir joué ![/bold green]")

class Entity:
    """
    Représente une entité générique dans le jeu.
    """
    def __init__(self, name: str, description: str, level: int, xp: float, stats: dict, attack_list: list) :
        """
        Initialise une entité avec des attributs de base.
        
        Args:
            name (str): Le nom de l'entité.
            description (str): Une description de l'entité.
            level (int): Le niveau de l'entité.
            xp (float): Les points d'expérience de l'entité.
            stats (dict): Les statistiques de l'entité.
            attack_list (list): La liste des attaques que l'entité peut effectuer.
        """
        self.name = name
        self.description = description
        self.level = level
        self.xp = xp
        self.stat = stats or {"health" : 100, "attack": 10, "defense": 5}
        self.max_hp = self.stat["health"]
        self.attack_list = attack_list or []

    def attack(self, target) -> str:
        """
        Effectue une attaque sur la cible.
        
        Args:
            target (Entity): L'entité cible à attaquer.
        
        Returns:
            str: Le résultat de l'attaque.
        """
        if not self.attack_list:
            return f"{self.name} n'a aucune attaque disponible"

        attack_chosen = None
        if type(target) is Player:
            attack_chosen = random.choice(self.attack_list)
        elif type(target) is Monster:
            choices = "\n".join([f"{i} - {attack.name} : {attack.damage + self.stat["attack"]}" for i, attack in enumerate(self.attack_list)])
            attack_chosen = self.attack_list[int(Prompt.ask(f"Choisissez votre attaque :\n{choices}\n", choices=[str(i) for i in range(len(self.attack_list))]))]

        if attack_chosen.durability > 0 or attack_chosen.max_durability == -1:
            dialog.naration(f"{self.name} utilise {attack_chosen.name}. \"{attack_chosen.battle_cry}\"")
            damage = max(attack_chosen.damage + self.stat["attack"] - target.stat["defense"], 0)
            target.change_stats(-damage, "health")
            if attack_chosen.max_durability != -1:
                attack_chosen.durability -= 1
        else:
            dialog.naration(f"{self.name} n'a plus de durabilité pour {attack_chosen.name}")
            return self.attack(target)

    def change_stats(self, amount: int, damage_type: str) -> None:
        """
        Modifie les statistiques de l'entité.
        
        Args:
            amount (int): Le montant de la modification de la statistique.
            damage_type (str): Le type de statistique à modifier (health, attack, defense).
        """
        if damage_type == "health" :
            new_health = max(self.stat["health"] + amount, 0)
            if new_health > self.max_hp:
                new_health = self.max_hp

            if amount < 0:
                dialog.naration(f"La santé de {self.name} descend de {-amount} ({self.stat['health']} -> {new_health})")
            else:
                dialog.naration(f"La santé de {self.name} augmente de {amount} ({self.stat['health']} -> {new_health})")
            
            self.stat["health"] = new_health

        elif damage_type == "attack" :
            new_attack = max(self.stat["attack"] + amount, 0)
            
            if amount < 0:
                dialog.naration(f"L'attaque de {self.name} descend de {-amount} ({self.stat['attack']} -> {new_attack})")
            else:
                dialog.naration(f"L'attaque de {self.name} augmente de {amount} ({self.stat['attack']} -> {new_attack})")
            
            self.stat["attack"] = new_attack
        elif damage_type == "defense" :
            new_defense = max(self.stat["defense"] + amount, 0)
            
            if amount < 0:
                dialog.naration(f"La défense de {self.name} descend de {-amount} ({self.stat['defense']} -> {new_defense})")
            else:
                dialog.naration(f"La défense de {self.name} augmente de {amount} ({self.stat['defense']} -> {new_defense})")
            
            self.stat["defense"] = new_defense

class Monster(Entity):
    """
    Représente un monstre dans le jeu.
    """
    def __init__(self, name: str, description: str, level: int, attack_list: list, dropable_items: list, boss: bool = False):
        """
        Initialise un monstre avec des attributs spécifiques.
        
        Args:
            name (str): Le nom du monstre.
            description (str): Une description du monstre.
            level (int): Le niveau du monstre.
            attack_list (list): La liste des attaques que le monstre peut effectuer.
            dropable_items (list): La liste des objets que le monstre peut laisser tomber.
            boss (bool): Indique si le monstre est un boss ou non.
        """
        stats = {
            "health": 50 + 20 * level,
            "attack": 5 + 2 * level,
            "defense": 3 + 1 * level
        } if not boss else {
            "health": 200 + 100 * level,
            "attack": 20 + 10 * level,
            "defense": 10 + 5 * level
        }

        super().__init__(name, description, level, 0, stats, attack_list)
        self.dropable_items = dropable_items

    def calculate_drops(self):
        """
        Calcule les objets laissés tomber par le monstre.
        
        Returns:
            list: La liste des objets laissés tomber.
        """
        dropped_items = []
        for item in self.dropable_items:
            if random.randint(0, 100) <= item.drop_rate:
                dropped_items.append(item)
        return dropped_items

class Player(Entity):
    """
    Représente un joueur dans le jeu.
    """
    def __init__(self, name: str, level: int, xp: float, attack_list: list, place, inventory: list = [], equipped_items: list = []):
        """
        Initialise un joueur avec des attributs spécifiques.
        
        Args:
            name (str): Le nom du joueur.
            level (int): Le niveau du joueur.
            xp (float): Les points d'expérience du joueur.
            stats (dict): Les statistiques du joueur.
            attack_list (list): La liste des attaques que le joueur peut effectuer.
            place (Place): Le lieu actuel du joueur.
            inventory (list): L'inventaire du joueur.
            equipped_items (list): La liste des objets équipés du joueur.
        """
        stats = {
            "health": 100 + 20 * level,
            "attack": 10 + 2 * level,
            "defense": 5 + 1 * level
        }
        super().__init__(name, "", level, xp, stats, attack_list)
        self.inventory = inventory
        self.place = place
        self.equipped_items = equipped_items

    def use_item(self, item_index):
        """
        Utilise un objet de l'inventaire.
        
        Args:
            item_index (int): L'index de l'objet à utiliser.
        
        Returns:
            bool: Indique si l'objet a été utilisé avec succès ou non.
        """
        if 0 <= item_index < len(self.inventory):
            item = self.inventory[item_index]
            if hasattr(item, "use"):
                item.use(self)
                self.inventory.pop(item_index)
                dialog.naration(f"{self.name} utilise {item.name}")
                return True
            else:
                dialog.naration(f"Vous ne pouvez pas utiliser {item.name} sur vous")
                return False
        else:
            dialog.naration(f"L'item à l'index {item_index} n'est pas dans votre inventaire.")
            return False

    def equip_item(self, item_index):
        """
        Équipe un objet de l'inventaire.
        
        Args:
            item_index (int): L'index de l'objet à équiper.
        
        Returns:
            bool: Indique si l'objet a été équipé avec succès ou non.
        """
        if 0 <= item_index < len(self.inventory):
            item = self.inventory[item_index]
            if isinstance(item, Equipable):
                if len(self.equipped_items) < 3:
                    item.equip(self)
                    self.equipped_items.append(item)
                    dialog.naration(f"{self.name} a équipé {item.name} !")
                else:
                    dialog.naration("Vous avez déjà 3 items équipés. Choisissez celui que vous voulez remplacer :")
                    choices = [f"{i} - {equipped_items.name}" for i, equipped_items in enumerate(self.equipped_items)]
                    choices.append("back - Ne pas remplacer")
                    choice = Prompt.ask(f"Choisissez un item à remplacer :\n{'\n'.join(choices)}", choices=[str(i) for i in range(len(self.equipped_items))] + ["back"])

                    if choice != "back":
                        self.equipped_items[int(choice)].unequip(self)
                        self.equipped_items[int(choice)] = item
                        item.equip(self)
                        dialog.naration(f"Vous avez remplacé un item par : {item.name}")
            else:
                dialog.naration(f"{item.name} ne peut pas être équipé")
                return False
        else:
            dialog.naration(f"L'item à l'index {item_index} n'est pas dans votre inventaire.")
            return False
    
    def add_item_to_inventory(self, item):
        """
        Ajoute un objet à l'inventaire du joueur.
        
        Args:
            item (Item): L'objet à ajouter.
        """
        self.inventory.append(item)
        dialog.naration(f"{self.name} a obtenu {item.name}")

    def interact_with_inventory(self, combat_mode=False):
        """
        Interagit avec l'inventaire du joueur.
        
        Args:
            combat_mode (bool): Indique si l'interaction se fait pendant un combat ou non.
        
        Returns:
            bool: Indique si l'interaction a été réussie ou non.
        """
        choices = [str(index) for index, item in enumerate(self.inventory)]
        choices.append("back")
        item_choice = Prompt.ask(f"Choisissez un item avec lequel intéragir :\n{'\n'.join([f'{index} - {item.name} : {item.description}' for index, item in enumerate(self.inventory)])}\nback - Revenir en arrière", choices=choices)

        if item_choice == "back":
            return False
        else:
            if combat_mode:
                return self.use_item(int(item_choice))
            else:
                action_choice = Prompt.ask("Voulez-vous consommer ou équiper cet item ?\n1 - Consommer\n2 - Équiper\nback - Revenir en arrière", choices=["1", "2", "back"])
                if action_choice == "1":
                    return self.use_item(int(item_choice))
                elif action_choice == "2":
                    return self.equip_item(int(item_choice))

    def add_xp(self, amount: float):
        """
        Ajoute des points d'expérience au joueur.
        
        Args:
            amount (float): La quantité de points d'expérience à ajouter.
        """
        self.xp += amount
        while self.xp >= self.xp_calculation_to_level_up():
            self.xp -= self.xp_calculation_to_level_up()
            self.level_up()

    def xp_calculation_to_level_up(self):
        """
        Calcule le seuil de points d'expérience pour monter de niveau.
        
        Returns:
            float: Le seuil de points d'expérience.
        """
        base_xp = 100
        growth_rate = 1.5
        return base_xp * (growth_rate ** (self.level - 1))

    def level_up(self):
        """
        Fait monter le joueur de niveau et augmente ses statistiques.
        """
        self.level += 1
        dialog.naration(f"Vous venez de passer au niveau {self.level} !")
        level_up_stats_text = []
        for stat, value in self.stat.items():
            increase = int(value * 0.2) if stat != "health" else int(self.max_hp * 0.2)
            new_stat_value = value + increase if stat != "health" else self.max_hp + increase
            level_up_stats_text.append(f"{stat.capitalize()} : {self.stat[stat]} -> {new_stat_value}")
            self.stat[stat] = new_stat_value
        dialog.naration("\n".join(level_up_stats_text))

        self.max_hp = self.stat["health"]

    def gain_attack(self, new_attack):
        """
        Ajoute une nouvelle attaque à la liste des attaques du joueur.
        
        Args:
            new_attack (Attack): La nouvelle attaque à ajouter.
        """
        if len(self.attack_list) < 3:
            self.attack_list.append(new_attack)
            dialog.naration(f"Vous avez appris une nouvelle attaque : {new_attack.name}")
        else:
            choices = [f"{index} - {attack.name} : {attack.description}" for index, attack in enumerate(self.attack_list)]
            choices.append("back - Ne pas remplacer")
            choice = Prompt.ask(f"Vous avez déjà 3 attaques. Choisissez une attaque à remplacer :\n{'\n'.join(choices)}\n", choices=[str(i) for i in range(len(self.attack_list))] + ["back"])

            if choice != "back":
                self.attack_list[int(choice)] = new_attack
                dialog.naration(f"Vous avez remplacé une attaque par : {new_attack.name}")

    def move(self, place):
        """
        Déplace le joueur vers un nouveau lieu.
        
        Args:
            place (Place): Le nouveau lieu vers lequel se déplacer.
        """
        dialog.place_changement(place.name)
        self.place = place
        self.place.interact(self)

    def display_stats(self):
        """
        Affiche les statistiques du joueur.
        """
        console.print(f"Niveau: {self.level}\nSanté: {self.stat['health']}/{self.max_hp}\nAttaque: {self.stat['attack']}\nDéfense: {self.stat['defense']}\n\n")

class Place:
    """
    Représente un lieu dans le jeu.
    """
    def __init__(self, name: str, description: str, monsters: list, interaction=None, places_around=None):
        """
        Initialise un lieu avec des attributs spécifiques.
        
        Args:
            name (str): Le nom du lieu.
            description (str): Une description du lieu.
            monsters (list): La liste des monstres dans le lieu.
            interaction (function): La fonction d'interaction pour le lieu.
            places_around (dict): Les lieux autour de ce lieu.
        """
        self.name = name
        self.description = description
        self.places_around = places_around or {}
        self.monsters = monsters
        self.exploration = False
        self.interaction = interaction or {}

    def interact(self, player):
        """
        Interagit avec le joueur dans le lieu.
        
        Args:
            player (Player): Le joueur avec lequel interagir.
        """
        player.display_stats()
        self.interaction(self)

class Combat:
    """
    Représente un combat entre un joueur et un adversaire.
    """
    def __init__(self, player, opponent):
        """
        Initialise un combat avec un joueur et un adversaire.
        
        Args:
            player (Player): Le joueur dans le combat.
            opponent (Monster): L'adversaire dans le combat.
        """
        self.turn_number = 0
        self.player = player
        self.opponent = opponent
        self.status = "Combat" #Fuite pour s'enfuire
        self.active_player = random.randint(0, 1) # 0 = Player /  1 = Monster // Détermine celui qui commence en premier

    #Début du combat
    def start(self):
        """
        Démarre le combat.
        """
        dialog.naration(f"Vous vous apprêtez à vous battre contre {self.opponent.name}...\nQUE LE COMBAT COMMENCE !")
        system("clear")

        while self.player.stat["health"] > 0 and self.opponent.stat["health"] > 0:
            dialog.naration(f"{self.player.name} a {self.player.stat['health']} PV.\n{self.opponent.name} a {self.opponent.stat['health']} PV.")
            self.turn()

            if self.status == "Fuite":
                break

        self.end()

    #Alternateur de tours
    def turn(self):
        """
        Alterne les tours entre le joueur et l'adversaire.
        """
        if self.active_player == 0:
            self.player_turn()
        else:
            self.opponent_turn()

        self.active_player = 1 - self.active_player
        self.turn_number += 1

    #Tour du PLayer
    def player_turn(self):
        """
        Exécute le tour du joueur.
        """
        action = Prompt.ask("Choisissez une action\n1 - Attaquer\n2 - Inventaire\n3 - Fuir", choices=["1", "2", "3"])

        if action == '1':
            return self.player.attack(self.opponent)
        elif action == '2':
            if not self.player.interact_with_inventory(combat_mode=True):
                return self.player_turn()
        elif action == '3':
            self.status = "Fuite"
            return "Vous avez réussi à vous enfuir !"

    #Tour de l'adversaire
    def opponent_turn(self):
        """
        Exécute le tour de l'adversaire.
        """
        #Appel de la méthode self.attack de la class Entity
        return self.opponent.attack(self.player)

    #Fin du combat
    def end(self):
        """
        Termine le combat et gère le résultat.
        """
        #Si l'adversaire est à 0 PV
        if self.opponent.stat["health"] <= 0 :
            #Drop du monstre, dropable_items = la liste des drops du monstre / Appel de la méthode self.calculate_drops de la class Entity
            drop_items = []
            if self.opponent.dropable_items:

                drop_items = self.opponent.calculate_drops()
                for item in drop_items:
                    self.player.add_item_to_inventory(item)

            amount_xp = 20 * self.opponent.level

            dialog.naration(f"Le combat est terminé !\nVous avez vaincu {self.opponent.name} et gagné {amount_xp} XP.\nIl vous manque {self.player.xp_calculation_to_level_up() - self.player.xp} XP pour monter de niveau.")

            self.player.add_xp(amount_xp)
            self.handle_attack_drops()
            self.reset_attack_durability()
            return True

        #Si le Player est à 0 PV
        elif self.player.stat["health"] <= 0 :

            #Le player perd le combat, retour à la base
            dialog.naration("Vous avez été vaincu comme un Looser que vous êtes ! Vous retournez au spawn bredouille !")
            self.player.stat["health"] = self.player.max_hp
            self.reset_attack_durability()
            return False

        #Le joueur s'enfuit du combat
        else:
            dialog.naration("Vous avez réussi à vous enfuir !")
            self.reset_attack_durability()
            return False
            # PEUT ETRE TP AU SPAWN

    def reset_attack_durability(self):
        # Reset la durabilité de l'attaque
        for attack in self.player.attack_list:
            if attack.max_durability != -1:
                attack.durability = attack.max_durability

    def handle_attack_drops(self):
        """
        Gère les attaques laissées tomber par l'adversaire.
        """
        dropped_attacks = []
        for attack in self.opponent.attack_list:
            if random.randint(0, 100) <= attack.drop_rate:
                dropped_attacks.append(attack)
        if dropped_attacks:
            dialog.naration("Vous avez la possibilité d'apprendre de nouvelles attaques :")
            for attack in dropped_attacks:
                choice = Prompt.ask(f"Voulez-vous apprendre l'attaque {attack.name} ?", choices=["oui", "non"])
                if choice == "oui":
                    self.player.gain_attack(attack)

class Item:
    """
    Représente un objet dans le jeu.
    """
    def __init__(self, name: str, description: str, effect: dict, drop_rate:int = 100):
        """
        Initialise un objet avec des attributs spécifiques.
        
        Args:
            name (str): Le nom de l'objet.
            description (str): Une description de l'objet.
            effect (dict): L'effet de l'objet.
            drop_rate (int): Le taux de drop de l'objet.
        """
        self.name = name
        self.description = description
        self.drop_rate = drop_rate
        self.effect = effect
        effect = {
            "health": 10
        }
        effect = {
            "attack": 10,
            "defense": 10
        }
    def __repr__(self):
        return self.name

class Equipable(Item):
    """
    Représente un objet équipable dans le jeu.
    """
    def __init__(self, name: str, description: str, effect: dict, drop_rate:int=100):
        """
        Initialise un objet équipable avec des attributs spécifiques.
        
        Args:
            name (str): Le nom de l'objet.
            description (str): Une description de l'objet.
            effect (dict): L'effet de l'objet.
            drop_rate (int): Le taux de drop de l'objet.
        """
        super().__init__(name, description, effect, drop_rate)
        self.equipped = False

    def equip(self, target):
        """
        Équipe l'objet à la cible.
        
        Args:
            target (Entity): La cible à équiper.
        """
        if not self.equipped:
            for stat, value in self.effect.items():
                if stat == "health":
                    target.max_hp += value
                target.stat[stat] += value
            self.equipped = True
            dialog.naration(f"{self.name} est maintenant équipé !")
        else:
            dialog.naration(f"{self.name} est déjà équipé.")

    def unequip(self, target):
        """
        Déséquipe l'objet de la cible.
        
        Args:
            target (Entity): La cible à déséquiper.
        """
        if self.equipped:
            for stat, value in self.effect.items():
                if stat == "health":
                    target.max_hp -= value
                target.stat[stat] -= value
            self.equipped = False
            dialog.naration(f"{self.name} a été déséquipé.")

class Consomable(Item):
    """
    Représente un objet consommable dans le jeu.
    """
    def __init__(self, name: str, description: str, effect: dict, drop_rate:int=100):
        """
        Initialise un objet consommable avec des attributs spécifiques.
        
        Args:
            name (str): Le nom de l'objet.
            description (str): Une description de l'objet.
            effect (dict): L'effet de l'objet.
            drop_rate (int): Le taux de drop de l'objet.
        """
        super().__init__(name, description, effect, drop_rate)
        self.active = False

    def use(self, target):
        """
        Utilise l'objet consommable sur la cible.
        
        Args:
            target (Entity): La cible sur laquelle utiliser l'objet.
        """
        for stat, value in self.effect.items():
            if stat in target.stat:
                target.change_stats(value, stat)

class Attack:
    """
    Représente une attaque dans le jeu.
    """
    def __init__(self, name: str, description: str, battle_cry: str, durability: int, damage: int, drop_rate:int = 100):
        """
        Initialise une attaque avec des attributs spécifiques.
        
        Args:
            name (str): Le nom de l'attaque.
            description (str): Une description de l'attaque.
            battle_cry (str): Le cri de guerre de l'attaque.
            durability (int): La durabilité de l'attaque.
            damage (int): Les dégâts de l'attaque.
            drop_rate (int): Le taux de drop de l'attaque.
        """
        self.name = name
        self.description = description
        self.battle_cry = battle_cry
        self.durability = durability
        self.max_durability = durability if durability != -1 else -1
        self.damage = damage
        self.drop_rate = drop_rate

class Dialog:
    """
    Représente un dialogue dans le jeu.
    """
    def dialog(self, dialog: list):
        """
        Affiche un dialogue.
        
        Args:
            dialog (list): La liste des lignes de dialogue.
        """
        for speaker, text in dialog:
            if speaker == "-":
                self.naration(text)
            else:
                self.talk(speaker, text)

    def place_changement(self, new_place: str):
        """
        Affiche un message de changement de lieu.
        
        Args:
            new_place (str): Le nom du nouveau lieu.
        """
        system("clear")
        Prompt.ask(f"[bold][green]Vous changez d'endroit...\nBienvenue dans [underline]{new_place}[/underline][/green][/bold]")

    def talk(self, speaker:str, text: str):
        """
        Affiche un message de discussion.
        
        Args:
            speaker (str): L'interlocuteur du message.
            text (str): Le texte du message.
        """
        system("clear")
        Prompt.ask(f"[blue]{speaker} >[/blue] {text}\n\nAppuyez sur enter pour continuer..")

    def naration(self, text):
        """
        Affiche un message de narration.
        
        Args:
            text (str): Le texte de la narration.
        """
        system("clear")
        Prompt.ask(f"[yellow]VOIX OFF >[/yellow] {text}\n\nAppuyez sur enter pour continuer..")

class Dialog:
    """
    Représente un dialogue dans le jeu.
    """
    def dialog(self, dialog: list):
        """
        Affiche un dialogue.
        
        Args:
            dialog (list): La liste des lignes de dialogue.
        """
        for speaker, text in dialog:
            if speaker == "-":
                self.naration(text)
            else:
                self.talk(speaker, text)

    def place_changement(self, new_place: str):
        """
        Affiche un message de changement de lieu.
        
        Args:
            new_place (str): Le nom du nouveau lieu.
        """
        system("clear")
        Prompt.ask(f"[bold][green]Vous changez d'endroit...\nBienvenue dans [underline]{new_place}[/underline][/green][/bold]")

    def talk(self, speaker:str, text: str):
        """
        Affiche un message de discussion.
        
        Args:
            speaker (str): L'interlocuteur du message.
            text (str): Le texte du message.
        """
        system("clear")
        Prompt.ask(f"[blue]{speaker} >[/blue] {text}\n\nAppuyez sur enter pour continuer..")

    def naration(self, text):
        """
        Affiche un message de narration.
        
        Args:
            text (str): Le texte de la narration.
        """
        system("clear")
        Prompt.ask(f"[yellow]VOIX OFF >[/yellow] {text}\n\nAppuyez sur enter pour continuer..")


if __name__ == "__main__":
    dialog = Dialog()
    game = Game("Mon RPG")
    game.start()
