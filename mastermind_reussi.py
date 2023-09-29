from mastermind_begin import Mastermind_begin

class Mastermind_reussi:
	
	def __init__(self, data) :
		self.data = data
		
	def run(self) :
		print('Vous avez devine la bonne combinaison')
		return Mastermind.begin(self.data)

