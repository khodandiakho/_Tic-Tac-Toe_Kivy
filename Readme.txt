Développé par : EL IDRISSI OUSSAMA & BOUMAHDI YASSINE

__TicTacToe Game__
Le jeu est développé en Python en utilisant la bibliotheque Kivy.
1-Dans Fichier main.py :
	Class TicTacToeApp : permet de definir toutes les elements graphiques et les initialisations de:
				-la table (board) .
				-le titre.
				-winning_combos : qui represente les indices des elements Horizontal,vertical et diagonal de la table , ce tableau va permet apres à faciliter l'identification des cas pour ganger le jeu.
				-choices : tableau de choix soit le joueur X ou le joueur O.
				- game_over :  au debut initialiser false . si un joueur gagne cet attribut change de valaur à true et le jeu s'arrete.
				 
	les methodes de la classe :
			- build () : permet d'initialiser les elements graphiques du jeu sous forme de 9 boutons 
			- on_start () : au lancé du jeu il fait appel à la methode init_players() qui va determiner le premier qui va jouer (soit le bot , soit l'utilisateur) d'une maniere aleatoire en utilisant la fonction randint
			- btn_pressed () : lorsque le joueur choisi une case il l'a remplie avec son choix si il est vide apres il fait appel à la methode make_move() dans la classe GamePlayer qui represente l'action de l'autre joueur(BOT) et puis il fait appel à check_winner().
			- check_winner() : il permet de verifier si on est arrivé à l'état but (état final) , si oui le jeu s'arrete est affiche le joueur gangnant .


2-Dans Fichier gameplayer.py:
	Class GamePlayer : permet de definir les actions du joueur (BOT) qui va esseyer de ganger s'il peut sinon il va jouer d'une maniere aléatoire.
				 
	les methodes de la classe :
			- make_random_move() : le joueur BOT au debut il joue au centre de la table si il est vide , sinon il cherche dans toutes les autres boutons vides si il peut ganger le jeu à l'aide du tableau winning_combos deja definie sinon il va jouer d'une maniere aleatoire.
			
			______________________________________________________
			
			
			Please Download the zip file in order to bypass all errors , Thanks ;)
