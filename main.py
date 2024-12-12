from rich.console import Console
from rich.prompt import Prompt
import random
from os import system

console = Console()

# Class représentant le jeu entier
class Game:
    def __init__(self, name: str):
        self.name = name
        self.main_player = None

        # Le joueur spawn dans le Tutoriel du jeu
        def spawn_interaction(place):
            naration = [
                ("-", "Vous vous réveillez lentement, déboussolé vous entendez des bruits peu reconnaissables…"),
                ("-", "Vos yeux s'ouvrent lentement..."),
                ("Vous dans vos pensées", "Ou suis-je…? Quels sont ces bruits...?"),
                ("...", f"... ? ... !? {self.main_player.name} !!!?"),
                ("Vous, déboussolé", "Ou.. Ou suis-je..? Et qui êtes vous..?"),
                ("...", "Ah ! J'ai bien cru que vous étiez morte !"),
                ("Vous, lentement", "Mais qui..."),
                ("...", "Chut ! Laissez moi me présenter, je me nome Loic et je serais ton guide tout au long de cette aventure !"),
                ("Vous, encore confus", "Une aventure ? Mais de quoi parlez-vous ?"),
                ("Loic, avec un sourir énigmatique", f"Ah, {self.main_player.name} ! Vous avez tant à découvrir. Vous vous trouvez dans un monde extraordinaire, rempli de magie et de mystères."),
                ("Vous, en vous redressant lentement", "Je ne comprends pas... Comment suis-je arrivée ici ?"),
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
                ["Vous", "Apprentissage ? Que suis-je censée apprendre ici ?"],
                ["Loic", "Les bases. Comment vous défendre, comment survivre, et comment devenir suffisamment forte pour affronter ce qui vous attend. La quête que vous portez ne sera pas facile. Mais avec chaque épreuve, vous deviendrez plus puissante."],
                ["-", "Soudain, un mouvement furtif attire votre attention. Une petite créature, mi-lapin, mi-reptile, bondit hors d’un buisson. Elle vous fixe avec des yeux curieux."],
                ["Loic", f"Regardez, {self.main_player.name}. La nature vous offre déjà votre premier défi. Ces créatures, les ‘Écho-lapins’, sont faibles, mais rapides. Attrapez-en un pour commencer. Vous devez vous familiariser avec le maniement de vos compétences."],
                ["Vous", "Mais… je ne sais même pas comment faire ça."],
                ["Loic (riant doucement)", "C’est pourquoi je suis là. Regardez dans votre sac. Vous y trouverez une arme rudimentaire – un bâton, mais suffisant pour débuter. Maintenant, concentrez-vous."],
                ["-", "Vous ouvrez un petit sac en toile suspendu à votre ceinture. Un bâton, usé mais solide, repose à l’intérieur. Vous le saisissez avec hésitation."],
                ["Loic", "Bien. Maintenant, tenez-vous prête. Ces créatures sont petites, mais elles peuvent mordre si vous n’êtes pas rapide. Concentrez votre énergie sur leur mouvement… et frappez !"],
                ["-", "Un tutoriel interactif commence. Vous apprenez à utiliser les commandes de base pour attaquer."],
            ]
            dialog.dialog(naration)
            
            #Présentation de l'objectif principal, drop et xp
            tutorielCombat = Combat(self.main_player, Monster(name="Écho-lapin", description="Tutorial Mob", level=0, stats={"health": 10}, dropable_items=[], attack_list=[Attack(name="Cris du fauve", description="Le cris d'un lapin", battle_cry="Miaou 🥺", durability=100, effect={})]))
            tutorielCombat.start()

            naration = [
                ["Vous", "Je l’ai eu !"],
                ["Loic", f"Très bien, {self.main_player.name}. Chaque créature ici vous offre une leçon. Continuez ainsi, et bientôt, vous serez prête à affronter bien plus que des lapins."],
                ["-", "Alors que vous continuez votre exploration, Loic vous explique les mécaniques du jeu."],
                ["Loic", "Dans cette forêt, vous allez apprendre les fondamentaux. Voici ce que vous devez savoir pour progresser :\n1 - Expérience et Niveaux : Chaque créature vaincue vous rapporte de l’expérience. Plus vous en accumulez, plus vous montez en niveau, débloquant de nouvelles compétences et renforçant vos capacités."],
                ["Loic", "Dans cette forêt, vous allez apprendre les fondamentaux. Voici ce que vous devez savoir pour progresser :\n2 - Équipement : Vous trouverez des matériaux dans les environs. Utilisez-les pour améliorer votre arme ou vous soigner."],
                ["Loic", "Dans cette forêt, vous allez apprendre les fondamentaux. Voici ce que vous devez savoir pour progresser :\n3 - Quête principale : Vous devrez récupérer 4 clés avant de pouvoir vous confronter au boss final se trouvant a HETIC (NABIL)."],
            ]
            dialog.dialog(naration)
            
            #Téléportation dans la zone de farm         
            self.places["Souflis Forest"].interact()
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
                    monster_possibility = [monster_data for monster_data in self.monsters.values() if player_level - 2 <= monster_data["level"] <= player_level + 2]
                    
                    #Rencontre d'un monstre choisi aléatoirement parmis la liste monster_possibility
                    if monster_possibility :
                        monster_fight = random.choice(monster_possibility)
                        
                        #Appel de la méthode self.start de la Class Combat
                        combat = Combat(self.main_player, Monster(**monster_fight))
                        combat.start()
                    else:
                        combat = Combat(self.main_player, Monster(**self.monsters["Hamid"]))
                        combat.start()
                    place.interact()
                case "2":
                    pass
                case "3":
                    self.main_player.move(self.places["La Foire aux Illusions Perdues"])
                case "4":
                    self.main_player.move(self.places["Domaine des Souflis"])
                case "5":
                    self.main_player.move(self.places["Hetic"])
                case "6":
                    self.main_player.move(self.places["Le Casino Zoologique"])
                case "7":
                    self.main_player.move(self.places["Le temple des 1 000 moines"])
                case _:
                    pass
        def la_foire_aux_illusions_perdues_interaction(place):
            pass

            dialog.dialog(naration)

            choice = Prompt.ask("Choisissez un objet :\n1 - Les boucles d’oreilles de la mère de Mathieu\n2 - Le bonnet légendaire de Laurent\n3 - Un orbe magique scintillant\n", choices=["1","2","3"])
            monster = Monster(**self.monsters["Kevin"])
            match choice:
                case "1":
                    monster.stats["health"] += 20
                    self.main_player.stats["health"] -= 20
                case "2":
                    monster.stats["defense"] += 20
                    self.main_player.stats["attack"] -= 20
                case "3":
                    monster.stats["defense"] += 20
                    self.main_player.stats["defense"] -= 20
                case _:
                    pass

            naration = [
                ("-", "Vous hésitez, mais finissez par faire un choix. La vieille femme esquisse un sourire énigmatique avant de disparaître dans un nuage de fumée."),
                ("-", "Une fois la femme disparue, vous ressentez un étrange frisson. En fouillant votre inventaire, vous réalisez que l’objet choisi n’est pas là. Pire encore, vous sentez une partie de votre force vous quitter. Les statistiques que vous venez de perdre semblent avoir été volées, comme si elles s’étaient volatilisées dans l’air… ou transférées à quelqu’un d’autre."),
                ("-", "Malgré cette expérience troublante, vous continuez votre chemin et entrez dans ce qui reste de la fête foraine. Mais l’ambiance y est complètement différente de ce que vous aviez perçu de loin : tout est inerte, silencieux. Plus un bruit, plus un mouvement. Les lumières des attractions vacillent, les ombres dansent, et un sentiment d’abandon vous envahit. Vous frissonnez à nouveau."),
                ("-", "Une lumière vive attire votre attention. Vous vous retournez et découvrez une grande structure, effrayante et imposante : le Palais des Glaces. Le bâtiment semble presque vivant, et une énergie sinistre s’en dégage. Vous comprenez que c’est votre seule option pour avancer. Résolu, vous pénétrez dans ce lieu étrange, vos pas résonnant dans un silence oppressant."),
                ("-", "L’intérieur est encore plus déroutant : des miroirs déformants renvoient des images grotesques et inquiétantes de vous-même. Chaque reflet semble amplifié, chaque pas résonne comme un coup de tonnerre. Alors que vous progressez dans ce labyrinthe brillant et oppressant, un rire lointain résonne soudain. Il est à la fois malveillant et amusé, semblant venir de partout à la fois."),
                ("???", "Bienvenue dans MON domaine, intrus."),
                ("-", "Vous tournez frénétiquement la tête, cherchant l’origine de cette voix, mais tout ce que vous voyez, ce sont des ombres mouvantes et des éclats de lumière. Soudain, une silhouette bondit devant vous. Un homme masqué, vêtu comme un clown sinistre, avec un immense marteau posé nonchalamment sur son épaule."),
                ("Kévin", "Tu crois pouvoir défier le Souverain des Rires Perdus ? HAHAHA ! Prépare-toi à souffrir, petit joueur. Ce lieu est mon royaume, et ici, je fixe les règles."),
                ("-", "Kévin brandit son marteau et se jette sur vous. Vous esquivez de justesse et comprenez que vous n’avez pas d’autre choix que de vous battre.")
            ]

            dialog.dialog(naration)

            combat = Combat(self.main_player, monster)

            if combat:
                self.main_player.inventory.append(self.artefact[""])

            self.places["Ici tout le monde perd"].interact()
        def domaine_des_souflis_interaction(place):
            choice = Prompt.ask("Choices :\n1 - Interact with the curent zone\n2 - Open the inventory\n3 - Go to the south-west (Domaine des Souflis)\n", choices=["1","2","3"])
            match choice:
                case "1": # Lancement du donjon
                    naration = [
                        ("-", "Vous franchissez les portes massives du Domaine des Souflis. Le lieu est à la fois majestueux et intimidant, avec des sculptures imposantes et des fresques murales racontant des légendes anciennes. Au centre, une immense salle trône sous un ciel artificiel éclairé par des cristaux lumineux. Vous ressentez une étrange tension dans l'air, comme si chaque pierre murmurait des avertissements."),
                        ("Loic", f"Nous sommes arrivés, {self.main_plyer.name}. Voici le Domaine des Souflis. Mais restez sur vos gardes… Nous ne sommes pas seuls."),
                        ("-", "Soudain, un bruit sourd résonne. Une silhouette imposante s’avance, sortant de l’ombre. C’est Anjalou, le fils du maître du Casino Zoologique, Anjara, et actuel protecteur de Mathieu Souflis."),
                        ("-", f"{self.main_plyer.name} entre dans la maison et glisse légèrement sur le sol bien poli. Anjalou apparaît soudainement, vêtu d’un costume élégant, son crâne parfaitement lustré. Il lève les yeux et ajuste son chapeau avec un air supérieur."),
                        ("Anjalou", "Ah, ma chère, vous avez enfin décidé de faire acte de présence. Mais faites attention, ce sol n’est pas là pour être sali !"),
                        ("-", f"Anjalou jette un coup d'œil à {self.main_plyer.name}, inspecte son propre reflet dans un miroir et se recoiffe en attendant sa réponse."),
                        ("Anjalou (S'approchant)", "Je suis Anjalou, le garde du corps du Seigneur Souflis. Si vous avez l’intention de vous aventurer plus loin, je conseille vivement de respecter le code de la mode et de l’élégance... ainsi que de vous préparer à affronter le véritable luxe.")
                    ]
                    dialog.dialog(naration)
                    combat = Combat(self.main_player, Monster(**self.monsters["Anjalou"]))
                    naration = [
                        ("-", f"Anjalou, en plein combat, esquive avec grâce avant de s'arrêter un instant pour polir son crâne. Puis, d'un coup, {self.main_plyer.name} réussit à le déstabiliser avec un coup décisif. Anjalou tombe à genoux, un dernier éclat de lumière se reflétant sur son crâne brillant."),
                        ("Anjalou", "Même la perfection doit un jour céder... Mais... mon crâne... il était encore si... éclatant..."),
                        ("-", "Il s'effondre doucement, lissant encore une fois son crâne avant de sombrer dans l'obscurité."),
                        ("-", "Vous entre dans une pièce richement décorée. Au fond, un homme se tient là, entouré de tableaux et de meubles luxueux. Il porte des habits amples et une attitude décontractée, mais quelque chose semble étrange, comme s'il dissimulait une puissance inouïe derrière cette apparence tranquille."),
                        ("Mathieu", "Ah, une nouvelle venue... Vous devez vous demander pourquoi un homme tel que moi se trouve ici, non ? Ne vous inquiétez pas, ce n'est pas la richesse qui vous intéressera ici. Vous vous apprêtez à rencontrer la véritable force."),
                    ]
                    dialog.dialog(naration)
                    combat = Combat(self.main_player, Monster(**self.monsters["Mathieu"]))
                    naration = [
                        ("-", f"Après une bataille intense, Mathieu se tient encore debout, son corps gravement blessé, mais une lueur de défi dans ses yeux. Il soulève son bras et regarde {self.main_plyer.name} avec une expression résolue."),
                        ("Mathieu", "Vous pensiez que la richesse était ma véritable arme ? Vous vous êtes trompée. J’ai plus que ça sous cette couche de confort."),
                        ("-", "Il lève son poing, prêt à frapper une dernière fois, mais vous lui donnez un coup fatal avant qu'il ne puisse attaquer. Son corps s’effondre lentement sur le sol, son sourire s'effaçant doucement, mais une lueur de respect dans ses yeux."),
                        ("Mathieu", "La... puissance... est... tout..."),
                    ]
                    dialog.dialog(naration)
                    self.main_player.inventory.append(self.artefact["Ecran du mac"])
                    self.places["Souflis Forest"].interact()
                case "2":
                    pass
                case "3":
                    self.main_player.move(self.places("Souflis Forest"))
                case _:
                    pass

        def le_casino_du_cartier_des_plaisirs_interaction(place):
            choice = Prompt.ask("Choices :\n1 - Interact with the curent zone\n2 - Open the inventory\n3 - Go to the North (La Foret des Souflis)\n", choices=["1","2","3"])
            match choice:
                case "1": # Lancement d'un combat + re envoi de l'interface a la fin du combat'
                    naration = [
                        ("-", "Après avoir traversé la jungle dense et sauvage, vous découvrez enfin une clairière dissimulée par une végétation luxuriante. Une lumière vacillante brille à travers les feuillages : c'est l'entrée du mystérieux Casino Zoologique. Une arche massive faite de lianes et de bois sculpté marque le passage vers ce lieu de vice et de hasard."),
                        ('-', "Deux imposants gorilles en costards, bras croisés, montent la garde devant une porte dorée ornée de pierres précieuses. Leur allure imposante et leur regard perçant suffisent à dissuader quiconque de s’approcher imprudemment."),
                        ("Garde Gorille 1 (ton grave et méfiant)", "Hé toi, petit humain. Bienvenue au Casino Zoologique, le repaire des âmes audacieuses."),
                        ("Garde Gorille 2 (d’un ton moqueur) ", "Connaîtras-tu la lumière de la gloire ou te perdras-tu dans l’obscurité ? Héhéhé…"),
                        ('-', "Vous semblez hésitant face à ces deux colosses, mais vous affichez votre détermination."),
                        ("Garde Gorille 1 (impressionné, mais narquois)", "Tu viens pour défier le Roi ? Tu as du cran, mais ne crois pas que ce sera aussi simple."),
                        ("Garde Gorille 2", "On pourrait juste te casser en deux, mais… les règles du casino sont claires. Ici, seule la chance décide de ton sort."),
                        ("Garde Gorille 1", "Voici notre test : ce dé pipé. Tout ce que tu as à faire, c’est obtenir un 12. Simple, non ?"),
                        ("Garde Gorille 2", "Bonne chance, humain… ou devrais-je dire, bonne patience. Tant que tu n’y arrives pas, tu restes là. Mwahaha !")
                    ]
                    dialog.dialog(naration)

                    number = 0

                    while number != 12:
                        choice = Prompt.ask("Choisissez une action :\n1 - Lancer un dé\n2 - Abandonner", choices=["1","2"])
                        if choice == 1:
                            number = random.randint(0, 12)
                            dialog.talk("-", f"Vous lancez un dé et tombez sur le numéro {number}")
                            if number != 12:
                                dialog.talk("Garde Gorille 1", "Hahaha, tu as raté ! Ré essaie si tu l'ose...")
                        else: # Choice == 2
                            dialog.talk("Garde Gorille 1", "Pff, comme prévu. Aucun humain ne peut rivaliser avec la jungle. Rentre chez toi, gamin.")
                            return self.places["Le casino du cartier des plaisirs"].interact()

                    naration = [
                        ("Garde Gorille 1 (étonné)", "Quoi ?! Tu as obtenu un 12 ? Eh bien, il semble que tu sois béni par la chance aujourd’hui."),
                        ("Garde Gorille 2", "Bonne chance avec le Roi. Il n’est pas aussi gentil que nous… Hé hé."),
                        ("-", "Une fois à l’intérieur, un monde flamboyant s’offre à vous : des chandeliers dorés suspendus au plafond, des tables de jeu illuminées par des néons verts et rouges, et une foule de primates en effervescence. Les chimpanzés, habillés comme des croupiers, font tourner les tables, tandis que des lémuriens occupés comptent des piles de jetons dans un coin sombre."),
                        ("-", "Au centre de la salle, sur un trône taillé dans un tronc d’arbre massif et recouvert de fourrure, trône le Roi Anjara. C’est un gorille massif au pelage d’un noir brillant, vêtu d’une cape en velours rouge. Un cigare pend mollement à sa lèvre, et une pile de cartes est posée à ses côtés."),
                        ("Roi Anjara (voix rauque et dominante)", "Qui ose troubler la paix de mon royaume ?"),
                        ("-", "Il vous dévisage avec intensité, puis se redresse lentement, écrasant son cigare dans une coupe dorée."),
                        ("Roi Anjara", "Ah, un humain… Tu veux te mesurer à moi ? Sache que je ne joue pas seulement avec les cartes, mais avec les destins. Prépare-toi, car ici, la triche est une vertu et la chance, un art.")
                    ]

                    dialog.dialog(naration)

                    combat = Combat(self.main_player, Monster(**self.monsters["Le Roi Singe"]))
                    combat.start()

                    self.main_player.inventory.append(self.artefact["Jeu de cartes"])
                    self.places["Le casino du cartier des plaisirs"].interact()
                case "2":
                    pass
                case "3":
                    self.main_player.move(self.places["Souflis Forest"])
                case _:
                    pass

        def le_temple_des_1000_moines_interaction(place):
            choice = Prompt.ask("Choices :\n1 - Interact with the curent zone\n2 - Open the inventory\n3 - Go to the North (La Foret des Souflis)\n", choices=["1","2","3"])
            match choice:
                case "1": # Lancement d'un combat + re envoi de l'interface a la fin du combat'
                    naration = [
                        ("-", "Vous arrivez au pied de la montagne qui abrite le légendaire Temple des 1000 Moines. Une double porte imposante en bois rouge écarlate se dresse devant vous, marquant l’entrée de ce sanctuaire ancien. Alors que vous vous approchez, les portes s’ouvrent lentement dans un grincement solennel. Une silhouette élancée se détache dans l’ombre du seuil."),
                        ('Leo', "Mes respects, jeune héros. Je suis Leo, humble serviteur de ce temple sacré. Bienvenue au sanctuaire du Temple des 1000 Moines."),
                        ("Leo (s'inclinant légèrement)", "Mon maître, Lao Ren, vous attendait avec impatience. Il dit que vous êtes l'Élu destiné à libérer la Forêt des Souflis de l’emprise de la guilde HETIC. Cependant…"),
                        ("Leo (serrant fortement un baton légèrement)", "…je dois m'assurer que vous êtes digne de rencontrer mon maître. Préparez-vous, jeune scarabée, car seul un esprit affûté peut franchir cette porte !"),
                    ]
                    dialog.dialog(naration)
                    # COMBAT CONTRE LEO

                    naration = [
                        ("-", "Vous gravissez péniblement l’escalier interminable. À chaque marche, la végétation luxuriante de la forêt des Souflis s’éloigne, offrant une vue à couper le souffle sur le paysage environnant. Enfin, au sommet, le temple se dévoile, majestueux. Les trois pavillons principaux scintillent sous le soleil, leurs toits dorés étincelant comme des joyaux. Les murs extérieurs racontent, à travers des fresques, l’histoire des 1000 moines qui atteignirent l’illumination en ces lieux.\nAlors que vous avancez, une voix grave et profonde résonne dans le vent, semblant provenir de toutes les directions à la fois."),
                        ("-", "Vous entendez une voix omniprésente. \"Vous avez donc réussi le défi de mon disciple… Suivez ma voix, héros, et venez à ma rencontre.\""),
                        ("-", "Vous atteignez la cour centrale, où le vent se fait plus vif. Soudain, un nuage de fumée s’élève devant vous. De cette brume émerge Lao Ren, le Gardien du Temple des 1000 Moines. Grand et imposant, vêtu d’un habit de soie orné de motifs dorés, il tient un bâton gravé de symboles mystiques."),
                        ("Maître Lao Ren", "Sacheburidana, héros-sama. Je sais pourquoi vous êtes là."),
                        ("-", "Le maître, vous salue lentement, puis plante son bâton au sol avec force."),
                        ("Maître Lao ren", "Mais avant d’accepter de vous remettre la relique sacrée, il est de mon devoir de tester votre force et votre volonté. Ne perdons pas de temps... Affrontez-moi !")
                    ]
                    dialog.dialog(naration)
                    combat = Combat(self.main_player, Monster(**self.monsters["Lao-ren"]))
                    self.places["Souflis Forest"].interact()
                case "2":
                    pass
                case "3":
                    self.main_player.move(self.places["Souflis Forest"])
                case _:
                    pass

        def hetic_interaction(place):
            pass

        # Initialisation des places sans les connexions
        spawn = Place(name="Spawn", description="Le point de départ du joueur", monsters=[], interaction=spawn_interaction)
        souflis_forest = Place(name="Souflis Forest", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=souflis_forest_interaction)
        la_foire_aux_illusions_perdues = Place(name="La Foire aux Illusions Perdues", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=la_foire_aux_illusions_perdues_interaction)
        domaine_des_souflis = Place(name="Le domaine des Souflis", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=domaine_des_souflis_interaction)
        casino = Place(name="Le Casino Zoologique", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=le_casino_du_cartier_des_plaisirs_interaction)
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
            "Bois de boulogne": Attack(name="Bois de boulogne", description="", battle_cry="", durability=100, damage=10),
            "Course rapide": Attack(name="Course rapide", description="", battle_cry="", durability=100, damage=10),
            "Souplesse du judoka": Attack(name="Souplesse du judoka", description="", battle_cry="Go muscu", durability=100, damage=10),
            "Poing de feu": Attack(name="Poing de feu", description="", battle_cry="Brule en enfer", durability=100, damage=10),
            "Coup de tonerre": Attack(name="Coup de tonerre", description="", battle_cry="Ça va piquer", durability=100, damage=10),
            "Grattage du délégué": Attack(name="Grattage du délégué", description="", battle_cry="Donne moi tes hp", durability=100, damage=10),
            "Lancé de talon": Attack(name="Lancé de talon", description="", battle_cry="Prend toi mon talon", durability=100, damage=10),
            "Griffure": Attack(name="Griffure", description="", battle_cry="Roarrrr", durability=100, damage=10),
            "Explosion": Attack(name="Explosion", description="", battle_cry="Araaaaa", durability=100, damage=10),
            "Vol rapide": Attack(name="Vol rapide", description="", battle_cry="Bismilah", durability=100, damage=10),
            "Charme": Attack(name="Charme", description="", battle_cry="Mouah 💋", durability=100, damage=10),
            "Chant brutal": Attack(name="Chant brutal", description="", battle_cry="Dès que je chanterais tu deviendras sourd.", durability=100, damage=10),
            "Kamehameha": Attack(name="Kamehameha", description="", battle_cry="Redonne mon couscous", durability=100, damage=10),
            "Malaka": Attack(name="Malaka", description="", battle_cry="Mange mon grec", durability=100, damage=10),
            "Control Mental": Attack(name="Control Mental", description="", battle_cry="Au hazard", durability=100, damage=10),
            "Gear 5": Attack(name="Gear 5", description="", battle_cry="Youhouu", durability=100, damage=10),
            "Fara 1": Attack(name="Fara 1", description="", battle_cry="", durability=100, damage=10),
            "Fara 2": Attack(name="Fara 2", description="", battle_cry="", durability=100, damage=10),
            "Amel 1": Attack(name="Amel 1", description="", battle_cry="", durability=100, damage=10),
            "Amel 2": Attack(name="Amel 2", description="", battle_cry="", durability=100, damage=10),
            "Marteau du Forain": Attack(name="Marteau du Forain", description="", battle_cry="Kévin abat son marteau avec fracas, déclenchant une onde de choc qui fait vibrer les miroirs autour de vous.", durability=100, damage=100),
            "Billes de Loterie Explosives": Attack(name="Billes de Loterie Explosives", description="", battle_cry="Il lance une poignée de billes colorées qui explosent en gerbes de lumière aveuglante.", durability=100, damage=100),
            "Claque de la Poigne Gigantesque": Attack(name="Claque de la Poigne Gigantesque", description="", battle_cry="Il prépare une claque chargée, des veines lumineuses pulsent sur la main, et un bruit sourd de tension monte dans l’air. L’impact crée une onde de choc qui soulève poussière et débris tout autour.", durability=1, damage=100),
            "Le Lasso de Soie": Attack(name="Le Lasso de Soie", description="Anjalou utilise un lasso en soie fine, qu'il fait briller comme une étoile. Il l’envoie avec élégance pour attraper ses ennemis et les ramener vers lui avec un mouvement fluide et gracieux.", battle_cry="TU M'ES ACCROCHÉ… ET J'AI UN CRÂNE À PRÉSERVER !", durability=100, damage=100),
            "La Roulade du Gentleman": Attack(name="La Roulade du Gentleman", description="Anjalou effectue une roulade parfaitement chorégraphiée, évitant les attaques ennemies tout en décochant un coup de pied agile, comme un maître de danse.", battle_cry="UNE DANSE AU RYTHME DU STYLE !", durability=100, damage=100),
            "Le Vent du Chapeau": Attack(name="Le Vent du Chapeau", description="Anjalou effectue un mouvement rapide, et son chapeau élégant se transforme en un projecteur de lumière qui éblouit temporairement les ennemis autour de lui.", battle_cry="MON STYLE, MA PUISSANCE !", durability=100, damage=100),
            "Le Crâne de Lumière": Attack(name="Le Crâne de Lumière", description="Anjalou se tient droit, prend une pause pour s'assurer que son crâne est parfaitement poli, puis libère une lumière aveuglante depuis son crâne chauve, envoyant une onde d'énergie brillante dans toute la zone. L'onde déstabilise ses ennemis, tout en rétablissant l’éclat de son apparence avec une touche de perfection.", battle_cry="VOUS NE POUVEZ PAS FAIRE CONCURRENCE AVEC LE CRÂNE DU MAÎTRE !", durability=1, damage=100),
            "Le Marteau de la Banque": Attack(name="Le Marteau de la Banque", description="Mathieu fait apparaître un énorme marteau doré en forme de lingot et le balance violemment sur le sol, créant une onde de choc étincelante.", battle_cry="TA BOURSE NE VA PAS AIMER ÇA !", durability=100, damage=100),
            "Le Lancer de Pièce Fétiche": Attack(name="Le Lancer de Pièce Fétiche", description="Il saisit une pièce dorée et la propulse à une vitesse fulgurante, frappant l’ennemi directement entre les yeux.", battle_cry="C’EST À MOI QUE TU LA DOIS, LA MONNAIE !", durability=100, damage=100),
            "Le Coup du Pantalon Traître": Attack(name="Le Coup du Pantalon Traître", description="Mathieu arrache un pan de ses vêtements et le fait tournoyer, créant un vent si puissant qu’il emporte ses adversaires.", battle_cry="CES FRINGUES NE SONT PAS JUSTE POUR LE STYLE !", durability=100, damage=100),
            "L’Écran Noir de la Dette": Attack(name="L’Écran Noir de la Dette", description="Mathieu tend les bras, et un immense écran translucide apparaît au-dessus de l’arène, projetant une lumière éblouissante. Sur cet écran, une facture gigantesque s’affiche avec des chiffres astronomiques qui clignotent, plongeant ses ennemis dans une terreur indescriptible.", battle_cry="ET SI TU PAYAIS TES IMPÔTS ?!", durability=1, damage=100),
            "Low Kick du Kangourou": Attack(name="Low Kick du Kangourou", description="", battle_cry="", durability=100, damage=100),
            "Bouclier du lémurien": Attack(name="Bouclier du lémurien", description="", battle_cry="", durability=100, damage=100),
            "Déferlante de la jungle": Attack(name="Déferlante de la jungle", description="", battle_cry="", durability=1, damage=100),
            "Coup du Lotus Brisé": Attack(name="Coup du Lotus Brisé", description="Un coup puissant et ciblé, imitant l’éclosion brutale d’un lotus.", battle_cry="", durability=100, damage=100),
            "Sillage d’Encens": Attack(name="Sillage d’Encens", description="Une série de mouvements fluides libérant une fumée toxique qui entrave les adversaires.", battle_cry="", durability=100, damage=100),
            "Colère des 1000 Âmes": Attack(name="Colère des 1000 Âmes", description="Le boss invoque les esprits des moines qui l’entourent pour déchaîner une tempête spirituelle dévastatrice.", battle_cry="", durability=1, damage=100),
        }

        self.items = {
            "Clé du casino" : Item(name="Clé du casino", description="Cette clé t'aidera a acceder au boss final !", effect={}),
            "Clé de la fête foraine" : Item(name="Clé de la fête foraine", description="Cette clé t'aidera a acceder au boss final !", effect={}),
            "Clé du temple" : Item(name="Clé du temple", description="Cette clé t'aidera a acceder au boss final !", effect={}),
            "Clé du Domaine" : Item(name="Clé du casino", description="Cette clé t'aidera a acceder au boss final !", effect={}),
            "Petite potion rouge": Consomable(name="Petite potion rouge", description="Potion donné par la déesse Gaïa (soigne)", effect={"hp": 5}, durability=1)
        }

        self.artefact = {
            "Ecran du mac": Equipable(name="Ecran du Mac", description="Utilisé comme bouclier, c'est le fameu écran du Mac de Mathieu", effect={"defense": 10}),
            "Maxi Phô Boeuf": Equipable(name="Maxi Phô Boeuf", description="", effect={"damage":10}),
            "Jeu de cartes": Equipable(name="Jeu de cartes", description="", effect={})
        }

        self.monsters = {
            "Amelie": {
                "name":"Amelie",
                "description":"",
                "level":2,
                "stats":{},
                "attack_list":[self.attacks["Amel 1"], self.attacks["Amel 2"]],
                "dropable_items":[self.items["Petite potion rouge"]]},
            "Fara": {
                "name":"Fara",
                "description":"",
                "level":4,
                "stats":{},
                "attack_list":[self.attacks["Fara 1"], self.attacks["Fara 2"]],
                "dropable_items":[self.items["Petite potion rouge"]]},
            "Imen": {
                "name":"Imen",
                "description":"",
                "level":6,
                "stats":{},
                "attack_list":[self.attacks["Control Mental"], self.attacks["Gear 5"]],
                "dropable_items":[self.items["Petite potion rouge"]]},
            "Nazim": {
                "name":"Nazim",
                "description":"",
                "level":8,
                "stats":{},
                "attack_list":[self.attacks["Kamehameha"], self.attacks["Malaka"]],
                "dropable_items":[self.items["Petite potion rouge"]]},
            "Nana la renarde": {
                "name":"Nana la renarde",
                "description":"",
                "level":10,
                "stats":{},
                "attack_list":[self.attacks["Charme"], self.attacks["Chant brutal"]],
                "dropable_items":[self.items["Petite potion rouge"]]},
            "Youva": {
                "name":"Youva",
                "description":"",
                "level":12,
                "stats":{},
                "attack_list":[self.attacks["Explosion"], self.attacks["Vol rapide"]],
                "dropable_items":[self.items["Petite potion rouge"]]},
            "Carglass": {
                "name":"Carglass",
                "description":"",
                "level":14,
                "stats":{},
                "attack_list":[self.attacks["Lancé de talon"], self.attacks["Griffure"]],
                "dropable_items":[self.items["Petite potion rouge"]]},
            "Cherif": {
                "name":"Cherif",
                "description":"",
                "level":16,
                "stats":{},
                "attack_list":[self.attacks["Coup de tonerre"], self.attacks["Grattage du délégué"]],
                "dropable_items":[self.items["Petite potion rouge"]]},
            "Noa": {
                "name":"Noa",
                "description":"",
                "level":18,
                "stats":{},
                "attack_list":[self.attacks["Souplesse du judoka"], self.attacks["Poing de feu"]],
                "dropable_items":[self.items["Petite potion rouge"]]},
            "Hamid": {
                "name":"Hamid",
                "description":"",
                "level":20,
                "stats":{},
                "attack_list":[self.attacks["Bois de boulogne"], self.attacks["Course rapide"]],
                "dropable_items":[self.items["Petite potion rouge"]]},
            "Kevin": {
                "name":"Kevin",
                "description":"Souverain des rires perdus",
                "level":1000,
                "stats":{},
                "attack_list":[self.attacks["Marteau du Forain"], self.attacks["Billes de Loterie Explosives"], self.attacks["Claque de la Poigne Gigantesque"]],
                "dropable_items":[self.items["Clé de la fête foraine"]]},
            "Anjaro": {
                "name":"Anjaro",
                "description":"Fils du Roi Singe",
                "level":1000,
                "stats":{},
                "attack_list":[self.attacks["Le Lasso de Soie"], self.attacks["La Roulade du Gentleman"], self.attacks["Le Vent du Chapeau"], self.attacks["Le Crâne de Lumière"]],
                "dropable_items":[]},
            "Mathieu": {
                "name":"Mathieu",
                "description":"Riche investisseur",
                "level":1000,
                "stats":{},
                "attack_list":[self.attacks["Le Marteau de la Banque"], self.attacks["Le Lancer de Pièce Fétiche"], self.attacks["Le Coup du Pantalon Traître"], self.attacks["L’Écran Noir de la Dette"]],
                "dropable_items":[self.items["Clé du Domaine"]]},
            "Le Roi Singe": {
                "name":"Le Roi Singe",
                "description":"Dirigeant de la confrérie singeresque",
                "level":1000,
                "stats":{},
                "attack_list":[self.attacks["Low Kick du Kangourou"], self.attacks["Bouclier du lémurien"], self.attacks["Déferlante de la jungle"]],
                "dropable_items":[self.items["Clé du casino"]]},
            "Lao-ren": {
                "name":"Lao-ren",
                "description":"Maître Shaolin",
                "level":1000,
                "stats":{},
                "attack_list":[self.attacks["Coup du Lotus Brisé"], self.attacks["Sillage d’Encens"], self.attacks["Colère des 1000 Âmes"]],
                "dropable_items":[self.items["Clé du temple"]]},
        }

    def start(self):
        console.print(f"[bold blue]Bienvenue dans {self.name}[/bold blue]")
        choice = Prompt.ask(
            "Faites un choix :\n0 - Créer un monde\n1 - Charger un monde\n",
            choices=["0", "1"]
        )

        system("clear")

        if choice == "0":
            console.print("[green]Création du personnage...[/green]")
            player_name = Prompt.ask("Quel nom souhaitez-vous donner à votre personnage ?")
            system("clear")
            self.main_player = Player(
                name=player_name,
                level=1,
                xp=0,
                stats={"health": 100, "attack": 10, "defense": 5},
                attack_list=[],
                place= self.places["Spawn"]
            )

            self.main_player.place.interact()


class Entity:
    def __init__(self, name: str, description: str, level: int, xp: float, stats: dict, attack_list: list) :
        self.name = name
        self.description = description
        self.level = level
        self.xp = xp
        self.stat = stats or {"health" : 100, "attack": 10, "defense": 5}
        self.max_hp = self.stat["health"]
        self.attack_list = attack_list or []

    def attack(self, target) -> None:
        if not self.attack_list:
            console.print(f"{self.name} n'a aucune attaque disponible")
        
        attack_chosen = None
        if type(target) is  Player:
            attack_chosen = random.choice(self.attack_list)
        elif type(target) is Monster :
            choices = "\n".join([f"{i} - {attack.name}" for i, attack in enumerate(self.attack_list)])
            attack_chosen = self.attack_list[int(Prompt.ask(f"Choisissez votre attaque :\n{choices}\n", choices=[str(i) for i in range(len(self.attack_list))]))]
            
        damage = max(attack_chosen.damage + self.stat["attack"] - self.stat["defense"], 0)
        console.print(f"{self.name} attaque {target.name} avec {attack_chosen['name']} et inflige {damage}.")
        target.take_damage(-damage, "attack")

    def change_stats(self, amount: int, damage_type: str) -> None:

        if damage_type == "health" :
            self.stat["health"] += amount
            self.stat["health"] = max(self.stat["health"], 0)

            console.print(f"La santé de {self.name} {"augmente" if amount > 0 else "descend"} de {amount}. Santé : {self.stat['health']}")
            if self.stat["health"] <= 0:
                console.print(f"{self.name} est vaincu")
        elif damage_type == "attack" :
            self.stat["attack"] += amount
            self.stat["attack"] = max(self.stat["attack"], 0)
            console.print(f"L'attaque de {self.name} {"augmente" if amount > 0 else "descend"} de {amount}. Attaque : {self.stat['attack']}")
        elif damage_type == "defense" :
            self.stat["defense"] += amount
            self.stat["defense"] = max(self.stat["defense"], 0)
            console.print(f"La défense de {self.name} {"augmente" if amount > 0 else "descend"} de {amount}. Défense : {self.stat['defense']}")


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
    def __init__(self, name: str, level: int, xp: float, stats: dict, attack_list: list, place ):
        super().__init__(name, "", level, xp, stats, attack_list)
        self.inventory = []
        self.place = place

    def show_inventory(self):
        if len(self.inventory) <= 0:
            return console.print(f"\L'inventaire de {self.name} est vide")
        else : 
            console.print(f"\ L'inventaire de {self.name}")
            for index, item in enumerate(self.inventory):

                item_details = f"{index}. {item.name} - {item.description}" if hasattr(item,"description") else f"{index}.{item.name}"
                console.print(item_details)
                console.print(f"Nombre d'item : {len(self.inventory)}")

    def use_item(self, item_index):
        for index, item in enumerate(self.inventory):
            if index == item_index:
                if hasattr(item, "use"):
                    console.print(f"{self.name} utilise {item.name}")
                    item.use(self)
                    self.inventory.pop(item_index)
                else:
                    console.print(f"(Vous ne pouvez pas utiliser {item.name} sur vous)")
                return
        console.print(f"{item.name} n'est pas dans votre inventaire")

    def add_xp(self, amount : float):
        self.xp += amount
        while self.xp >= self.level_up_threshold():
            self.xp -= self.level_up_threshold()
            self.level_up()
        console.print(f"Vous venez de gagner {amount} XP !")
    
    def level_up_threshold(self):
        base_xp = 100
        growth_rate = 1.5
        return base_xp * (growth_rate ** (self.level - 1))

    def move(self, place):
        pass

    def level_up(self):
        self.level += 1
        print(f"Vous venez de passer au niveau {self.level}")

        for stat, value in self.stats.items():
            increase = int(value*0.1)
            self.stats[stat] += increase
            console.print(f"vos statistiques sont augmentées de {increase} pour {self.stats[stat]} !")
        
        #On débloque des nouvelles attaques ?

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


class Combat:
    def __init__(self, player, opponent):
        self.turn_number = 0 
        self.player = player
        self.opponent = opponent
        self.active_player = random.randint(0 , 1) # 0 = Player /  1 = Monster // Détermine celui qui commence en premier 
    #Début du combat
    def start(self):
        console.print(f"[red]Vous vous apprêtez à vous battre contre {self.opponent.name}...\n QUE LE COMBAT COMMENCE[/red]")
        
        #Boucle des tours du combat    
        while self.player.stat["health"] != 0 and self.opponent.stat["health"] != 0 :
                          
            #Affichage des PV à chaque début de tour
            console.print(f"[bold]Vous avez {self.player.stat["health"]} PV. \n {self.opponent.name} a {self.opponent.stat["health"]} PV.") 
            self.turn()
        
        #Termine le combat si l'un des deux Entity tombe à 0 PV.    
        self.end()

    #Alternateur de tours        
    def turn(self):
        if self.active_player == 0:
            console.print(f"[cyan]Tour {self.turn_number}: {self.player.name}, à vous de jouer![/cyan]")
            self.player_turn()
        else:
            console.print(f"[magenta]Tour {self.turn_number}: {self.opponent.name} attaque![/magenta]")
            self.opponent_turn() 
        
                
        #Inversion de active_player après chaque tour (alterne entre 0 et 1)
        self.active_player = 1 - self.active_player
        
        #Compteur de tours
        self.turn_number += 1

    #Tour du PLayer
    def player_turn(self):
        
            #Menu principal du tour de combat
            action = Prompt.ask("Choisissez une action\n1 - Attaquer\n2 - Inventaire\n3 - Fuir", choices = ["1","2","3"],)

            #Le Player choisit d'attaquer
            if action == '1':
                #Appel de la méthode self.attack de la class Entity
                self.player.attack(self.opponent)
            #Le Player choisit d'ouvrir son Inventaire pour le REGARDER    
            elif action == '2' :
                #Appel de la méthode self.show_inventory de la class Entity  
                self.player.show_inventory()

                choices = [index for index, item in enumerate(self.player.inventory) if isinstance(item, Consomable)]
                choices.append("Back")
                item_choice = Prompt.ask(f"Choisissez un item a utiliser:\n{"\n".join([f"{index} - {item} : {item.description}" for index, item in enumerate(self.player.inventory) if isinstance(item, Consomable)])}\nBack - Re venir en arière", choices=choices)

                if item_choice == "Back":
                    return self.player_turn()
                else:
                    self.player.use_item(int(item_choice))
                #Le player choisit de s'enfuir
            elif action == '3' :
                #Appel de le fonction self.escape pour 
                    self.end()
    
    #Tour de l'adversaire        
    def opponent_turn(self):

        #Appel de la méthode self.attack de la class Entity
        self.opponent.attack(self.player)
    
    #Fin du combat
    def end(self):
        
        #Si l'adversaire est à 0 PV
        if self.opponent.stat["health"] <= 0 :
            
            #Ajoute l'xp au héro, 10 * Le niveau du monstre
            amount_xp = 10 * self.opponent.level
            self.player.add_xp(amount_xp)
            
            #Drop du monstre, dropable_items = la liste des drops du monstre / Appel de la méthode self.calculate_drops de la class Entity
            drop_items = self.opponent.calculate_drops(self.dropable_items)
            for item in drop_items:
                self.player.inventory.append(item)

            Console.print("Le combat est terminé !")
            Console.print(f"[cyan]Vous avez vaincu {self.opponent.name} \n vous avez gagne {amount_xp} xp, il vous manque ... xp pour augmenter de niveau \n Vous avez trouvé {drop_items}[/cyan]")
     
        #Si le Player est à 0 PV   
        elif self.player.stat["health"] <= 0 :
            
            #Le player perd le combat, retour à la base    
            Console.print("[red]Vous avez été vaincu comme un Looser que vous êtes ! Vous retournez au spawn bredouille ![/red]")          
            # PEUT ETRE TP AU SPAWN
    
        #Le joueur s'enfuit du combat
        else:
            Console.print("[cyan]Vous arrivez à vous enfuir comme un lâche ![/cyan]")
            # PEUT ETRE TP AU SPAWN

class Item:
    def __init__(self, name: str, description: str, effect: dict):
        self.name = name
        self.descritpion = description
        self.effect = effect
        effect = {
            "health": 10
        }
        effect = {
            "attack": 10,
            "defense": 10
        }

class Equipable(Item):
    def __init__(self, name: str, description: str, effect: dict):
        super().__init__(name, description, effect)
        self.equiped = False
    def equip(self, target):
        #  A MODIFIER
        if not self.equipped:
            for stat, value in self.effect.items():
                target.stat[stat] += value
            self.equipped = True
            console.print(f"{self.name} est maintenant équipé !")
        else:
            console.print(f"{self.name} est déjà équipé.")



class Consomable(Item):
    def __init__(self, name: str, description: str, effect: dict, durability: int):
        super().__init__(name, description, effect)
        self.active = False
        self.durability = durability

    def use(self, target):
        if "health" in self.effect and target.max_health > target.stats["health"]:
               if self.effect["health"] < target.max_health - target.stats["health"] :
                   target.stats["health"] += self.effect["health"]
               else :
                   target.stats["health"] = target.max_health
        elif "attack" in self.effect:
            target.stats["attack"] += self.effect["attack"]
        else :
            target.stats["defense"] += self.effect["defense"]

    def use(self, target):
        for stat, value in self.effect.items():
            if stat in target.stat:
                target.change_stats(value, stat)
        console.print(f"{self.name} a été utilisé avec succès !")
class Attack:
    def __init__(self, name: str, description: str, battle_cry: str, durability: int, damage: int):
        self.name = name
        self.description = description
        self.battle_cry = battle_cry
        self.durability = durability
        self.damage = damage

class Dialog:
    def dialog(self, dialog: list):
        for speaker, text in dialog:
            if speaker == "-":
                self.naration(text)
            else:
                self.talk(speaker, text)

    def place_changement(self, new_place: str):
        system("clear")
        Prompt.ask(f"[bold][green]Vous changez d'endroit...\nBienvenue dans [underline]{new_place}[/underline][/green][/bold]")

    def talk(self, speaker:str, text: str):
        system("clear")
        Prompt.ask(f"[blue]{speaker} >[/blue] {text}\n\nAppuyez sur enter pour continuer..")

    def naration(self, text):
        system("clear")
        Prompt.ask(f"[yellow]VOIX OFF >[/yellow] {text}\n\nAppuyez sur enter pour continuer..")

class Dialog:
    def dialog(self, dialog: list):
        for speaker, text in dialog:
            if speaker == "-":
                self.naration(text)
            else:
                self.talk(speaker, text)

    def place_changement(self, new_place: str):
        system("clear")
        Prompt.ask(f"[bold][green]Vous changez d'endroit...\nBienvenue dans [underline]{new_place}[/underline][/green][/bold]")

    def talk(self, speaker:str, text: str):
        system("clear")
        Prompt.ask(f"[blue]{speaker} >[/blue] {text}\n\nAppuyez sur enter pour continuer..")

    def naration(self, text):
        system("clear")
        Prompt.ask(f"[yellow]VOIX OFF >[/yellow] {text}\n\nAppuyez sur enter pour continuer..")


if __name__ == "__main__":
    dialog = Dialog()
    game = Game("Mon RPG")
    game.start()

