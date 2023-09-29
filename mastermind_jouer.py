from mastermind_reussi import Mastermind_reussi

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
