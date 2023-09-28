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
		
		
		
# Stade begin
class Mastermind_begin(Mastermind_state):
	
	def __init__(self, data) :
		Mastermind_state.__init__(self, data)
		
	def run(self) :
		self.data.running = False
		return Mastermind_begin(self.data)






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
