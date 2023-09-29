from mastermind_begin import Mastermind_begin


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
