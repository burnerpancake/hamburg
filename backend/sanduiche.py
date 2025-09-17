### Classe ###
class Lanche:
	def __init__(self, nome, preco, ingredientes):
		self.nome = nome
		self.preco = float(preco)
		self.ingredientes = ingredientes

	# Fim do construtor __init__()

	def exibirLanche(self):
		"""
		Exibe os dados do lanche cadastrado
		"""
		print(f"Sanduíche: {self.nome}\nPreço: {self.preco}\nIngredientes: {self.ingredientes}")
		
# Fim da Classe