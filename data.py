from couleur import Couleurs

#
# Donnees de l'application
#
class Mastermind_data:
	
	def __init__(self) :
		self.running = True
		
		self.reponse_acceptee = {'rouge': Couleurs.Rouge, 'jaune': Couleurs.Jaune, 'bleu': Couleurs.Bleu, 'vert': Couleurs.Vert, 'mauve': Couleurs.Mauve, 'orange': Couleurs.Orange, 'r': Couleurs.Rouge, 'j': Couleurs.Jaune, 'b': Couleurs.Bleu, 'v':Couleurs.Vert, 'm': Couleurs.Mauve, 'o': Couleurs.Orange}
		
		self.combinaison_secrete = (Couleurs.Rouge, Couleurs.Rouge, Couleurs.Rouge, Couleurs.Rouge, Couleurs.Rouge)
		
		self.entree_divisee = (0)
		self.nb_essais = 1
