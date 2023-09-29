from mastermind_jouer import Mastermind_jouer

# Stade begin
class Mastermind_begin:
	
	def __init__(self, data) :
		self.data = data
		
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
