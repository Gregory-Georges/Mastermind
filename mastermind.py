#
# Donnees de l'application
#
class Mastermind_data:
	
	def __init__(self) :
		self.running = True






#
# Stade de l'applicaton (State machine)
#


# Classe base
class Mastermind_state:
	
	def __init__(self, data) :
		self.data = data
		
	def run(self) :
		pass
		
		

# Stade jeu
class Mastermind_jouer(Mastermind_state):
	def __init__(self, data) :
		Mastermind_state.__init__(self, data)
		
	def run(self) :
		return self

		
				
# Stade begin
class Mastermind_begin(Mastermind_state):
	
	def __init__(self, data) :
		Mastermind_state.__init__(self, data)
		
	def run(self) :
		self.afficher_intro() 
		state = self.demander_continuer_quitter()
		return state
		
	
	
	def afficher_intro(self) :
		print(' __  __    __    ___  ____  ____  ____  __  __  ____  _  _  ____  ')
		print('(  \/  )  /__\  / __)(_  _)( ___)(  _ \(  \/  )(_  _)( \( )(  _ \ ')
		print(' )    (  /(__)\ \__ \  )(   )__)  )   / )    (  _)(_  )  (  )(_) )')
		print('(_/\/\_)(__)(__)(___/ (__) (____)(_)\_)(_/\/\_)(____)(_)\_)(____/ ')
		print('')
	
	
	
	def demander_continuer_quitter(self) :
		entree_valide = False
		while not entree_valide :
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
