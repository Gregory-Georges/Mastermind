from couleur import Couleurs

#
# Donnees de l'application
#
class Mastermind_data:
	
	def __init__(self) :
		self.running = True
		self.reponse_acceptee = {'rouge': Couleurs.Rouge, 'jaune': Couleurs.Jaune, 'bleu': Couleurs.Bleu, 'vert': Couleurs.Vert, 'mauve': Couleurs.Mauve, 'orange': Couleurs.Orange, 'r': Couleurs.Rouge, 'j': Couleurs.Jaune, 'b': Couleurs.Bleu, 'v':Couleurs.Vert, 'm': Couleurs.Mauve, 'o': Couleurs.Orange}
		self.combinaison_secrete = (Couleurs.Rouge, Couleurs.Rouge, Couleurs.Rouge, Couleurs.Rouge, Couleurs.Rouge)
		self.entree_divisee = (0) * 5
		self.nb_essais = 1






#
# Stades de l'applicaton (State machine)
#



class Mastermind_state:
	
	def __init__(self, data) :
		self.data = data
		
	def run(self) :
		pass;
		
		
		
class Mastermind_reussi:
	
	def __init__(self, data) :
		self.data = data
		
	def run(self) :
		print('Vous avez devine la bonne combinaison')
		return self
		
		

# Stade jeu
class Mastermind_jouer:
	def __init__(self, data) :
		Mastermind_state.__init__(self, data)
		
	def run(self) :
		self.entrer_combinaison()
		return self.verifier_entree()
		
	def entrer_combinaison(self) :
		print("entrez une combinaison de 5 couleurs separees d'un espace (ex: b vert r jaune o)")
		entree = input()
		self.data.entree_divisee = entree.split(' ')
				
	def verifier_entree(self) :
	
		# Verifier le nombre de couleurs
		if(len(self.data.entree_divisee) > 5):
			print("Trop d'entrees")
			return self
		if(len(self.data.entree_divisee) < 5):
			print("Pas assez d'entrees")
			return self
			
		# Verifier que toutes les entrees sont bonnes
		for element in self.data.entree_divisee:
			if element not in self.data.reponse_acceptee:
				print("Au moins une entree est invalide")
				return self
				
		# Construire la combinaison en nombres
		combinaison_en_nombres = (self.data.reponse_acceptee[self.data.entree_divisee[0]], self.data.reponse_acceptee[self.data.entree_divisee[1]], self.data.reponse_acceptee[self.data.entree_divisee[2]], self.data.reponse_acceptee[self.data.entree_divisee[3]], self.data.reponse_acceptee[self.data.entree_divisee[4]])
				
		# Verifier que la combinaison est bonne
		if(self.data.combinaison_secrete != combinaison_en_nombres) :
			self.data.nb_essais = self.data.nb_essais + 1
			return self
				
				
		return Mastermind_reussi(self.data)

		
				
# Stade begin
class Mastermind_begin:
	
	def __init__(self, data) :
		Mastermind_state.__init__(self, data)
		
	def run(self) :
		self.afficher_intro() 
		return self.demander_continuer_ou_quitter()
		
	
	
	def afficher_intro(self) :
		print(' __  __    __    ___  ____  ____  ____  __  __  ____  _  _  ____  ')
		print('(  \/  )  /__\  / __)(_  _)( ___)(  _ \(  \/  )(_  _)( \( )(  _ \ ')
		print(' )    (  /(__)\ \__ \  )(   )__)  )   / )    (  _)(_  )  (  )(_) )')
		print('(_/\/\_)(__)(__)(___/ (__) (____)(_)\_)(_/\/\_)(____)(_)\_)(____/ ')
		print('')
	
	
	
	def demander_continuer_ou_quitter(self) :
	
		print("Commencer le jeu ? (o / n)")
		entree = input().lower()
		
		if entree != 'o' and entree != 'n' :
			print('Entree invalide')
			return self
			
		if entree == 'o' :
			return Mastermind_jouer(self.data)
		
		if entree == 'n' :
			self.data.running = False
			return self






#
# Classe application
#

class Mastermind:
	
	def __init__(self) :
		self.data = Mastermind_data()
		self.state = Mastermind_begin(self.data)
	
	def run(self) :
		data = self.data
		while data.running :
			self.state = self.state.run()
